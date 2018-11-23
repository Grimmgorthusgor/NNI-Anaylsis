# NNI-Anaylsis
Group Project ID: 61 - Using an excel (data from World Bank) file that shows NNI (Net National Income) from 2007-16 per country , the user is able to run different types of analysis per country and per year.

--------------------

PROJECT DESCRIPTION

--------------------
This is a mandatory group project part of the course "Programming with Advanced Computer Languages" supervised by Dr. Mario Silic. 

The group project was done individually by Adrien Fesselet (Student-ID: 14-605-521) with the pseudonym "Grimmgorthusgor" to accomplish tasks in the course.

The coding was done using jupyter notebook and importing pandas and NumPy libraries. 

The goal was to give simple analysis tools to a user for a definite file with data from World Bank which was accessed here: https://data.worldbank.org/indicator/NY.ADJ.NNTY.CD

The file was then modified to only cover the last accessible years (2007 - 16) and eliminated pack of countries (European Union etc.) to only have individual countries.

The user can first choose one of the 162 countries and get several information (such as year with max. NNI and its value, year with min. NNI and its value, average of its NNI over 2007-16, median of its NNI over 2007-16, as well as the CAGR of its NNI's development over 2007-16).

The user can then choose an individual year (2007-16) to display other information (such as the country with the max. NNI and its value in that year, the country with the min. NNI and its value in that year, the mean NNI value of all countries in that year, as well as the median NNI value of all countries in that year).

NNI stands for Net National Income and is an economics term used in the accounting of national income. It is the difference between what is earned by nationals living inside and outside the country put together and non-nationals living in the country. It can be defined as NNI = C + I + G + (NX) + net foreign factor income - indirect taxes - manufactured capital depreciation where C = Consumption, I = Investments, G = Government spending and NX = Net exports (exports minus imports).

--------------------

HOW TO USE AND TEST THE CODE

--------------------

Four files are distributed within this repository. 

This file (README.md) is used for a project description as well as insutrctions on how to use and test the code done by the student.

Two files contain code (AF_proj.py) and (AF_proj.ipynb). (AF_proj.py) is the file that is binding and shall be tested and used by the professor, whereas (AF_proj.ipynb) only provides the professor with an example of how the student functioned in the development of his code writing and testing.

A last file (NNI_Index.csv) is a modified file taken directly from the World Bank's website (shared above) which is read in the (AF_proj.py) file.

The file containing the code (AF_proj.py) also contains extensive comments for all or most of the coding lines. The comments should be read to gain deeper insight into the functioning of the code and logic used.

To test the project: The excel file (NNI_Index.csv) and (AF_proj.py) have to be downloaded and put in the same folder. The user then has to make sure she/he has functioning and latest python3 as well as pandas and NumPy libraries. By using the terminal, the user then open the file by accessing the folder (writing "cd ") and by sliding the folder which contains the files in the terminal and by then writing (AF_proj.py) if that is still the code file's name. Displayed will be an exemplary of the first 10 countries (alphabetically) in the list with corresponding values in some years. The user will then be prompted to enter a country's name (refer to line 19 - 22 of this file for explanations on what the code asks for inputs and expected outputs).



Hope you will enjoy the coding experience :)

Adrien Fesselet - Grimmgorthusgor
