#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np


# Reads the excel file
df = pd.read_csv('NNI_Index.csv')

# Prints a sample of countries at the start just to give the user a brief overview of the dataframe
print("This is a sample of the first 10 countries out of 162")
print('\n', df.head(10))


# Asks the user for an input (country) with specified format
country = input("Choose a country (Format: Argentina): " )

# Loop that repeats itself when a value entered as input is not found in the column "Country Name" of the dataframe.
# Prints an error message and asks the user again for a country's name
while country not in df["Country Name"].values:
    print("Country not found")
    country = input("Choose a country (Format: Argentina): " )


# Compares the input above with the column "Country Name", returning true for the row of the country.
# Also selects the columns that contain values per year (2007-16)
country_row = df[ df["Country Name"] == country ].iloc[:,3:13]
# Takes out the values of the first row of the dataframe
yearly_nni_country = country_row.values[0]
# Finds the year for the corresponding minimum value
min_year_country = country_row.T.index[yearly_nni_country == yearly_nni_country.min()].values[0]
# Finds the year for the corresponding maximum value
max_year_country = country_row.T.index[yearly_nni_country == yearly_nni_country.max()].values[0]


# Prints the year which had lowest NNI value (and NNI value) for the country given as input
print("\n{} is the year with the min NNI at: {:.3E}".format(min_year_country,yearly_nni_country.min()))


# Prints the year which had highest NNI value (and NNI value) for the country given as input
print("\n{} is the year with the max NNi at: {:.3E}".format(max_year_country,yearly_nni_country.max()))


# Prints the average NNI for the country given as input in the time period 2007-16
print("\nThis is the average NNI over 10 years (2007-16): {:.3E}".format(yearly_nni_country.mean()))


# Prints the median NNI for the country given as input in the time period 2007-16
print("\nThis is the median NNI over 10 years (2007-16): {:.3E}".format(np.median(yearly_nni_country)))


# CAGR or compound annual growth rate measures the average yearly growth rate over a period (here 2007-16).
CAGR = "\nThis is the CAGR over 10 years (2007-16): {:.3f}%".format((yearly_nni_country[-1] / yearly_nni_country[0]) ** (1/10) - 1)
print(CAGR)


# Loop that repeats itself when a value entered as input is not found in the "year" column of the dataframe.
# Prints an error message and asks the user again for a country's name
year = input("\n\nChoose a year (Format: XXXX, between 2007-16): " )
while year not in country_row.columns.values:
    print("Year is not found")
    year = input("Choose a year (Format: XXXX, between 2007-16): " )


# Returns a dataframe which contains the country name and the year gotten in input
country_year_df = df[["Country Name", year]]
# Returns a dataframe consisting of the maximum value for the year gotten in input as well as the corresponding country,
# by comparing the maximum value in the dataframe's column of the specific year given in input.
max_year = country_year_df[df[year] == df[year].max()]
# Returns from the column "Country Name" the name of the single country in the list of values.
max_country = max_year["Country Name"].values[0]


# Prints the country with the max NNI (and the NNI's value) in the given year
print("\nThis is the country with the max NNI in this year: {}, {:.3E}".format(max_country, max_year[year].values[0]))


# Returns a dataframe consisting of the minimum value for the year gotten in input as well as the corresponding country,
# by comparing the minimum value in the dataframe's column of the specific year given in input.
min_year = country_year_df[df[year] == df[year].min()]
# Returns from the column "Country Name" the name of the single country in the list of values.
min_country = min_year["Country Name"].values[0]


# Prints the country with the min NNI (and the NNI's value) in the given year
print("\nThis is the country with the min NNI in this year: {}, {:.3E}".format(min_country, min_year[year].values[0]))


# Prints the mean NNI of all countries in the year given as input
print("\nThis is the mean: {:.3E}".format(df[year].mean()))


# Prints the median NNI of all countries in the year given as input
print("\nThis is the median: {:.3E}".format(df[year].median()))





