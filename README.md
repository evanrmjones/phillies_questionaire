# phillies_questionaire

a. 
To improve this code, I would simplify the function down to one loop. The second loop in this function is not necessary. I would keep the first part of the function the same, creating a new string and adding all the characters of the string into the new string. Then, instead I would simply check if the input string is the same as the new string we created. If it is true, return True; else, return False. This will decrease the time complexity of the function from O(N^2) to O(N) and make the function more efficient on larger strings. The old function and the new function can be found in the document in folder named Question a. 



b. 
To find the qualifying offer, I downloaded the file of all salaries for 2016 and converted it to a csv file. Then, in excel I made all salaries into integers and "no salary data" values 0. I then downloaded it into a Python Ide and used a jupyter notebook to do analysis on the salaries. I then decided to use the Pandas library for Python to do my analysis on the data. First, I opened the data and put it into a DataFrame, a data type created by Pandas. I then solely selected the column that contained salary. Next, I dropped any values that were null. Then I put the data set into ascending order and used the head function to take the top 125 salaries. I then used the Pandas mean operation to find the value of the qualifying offer. The Jupyter Notebook file can be found under the name Question b as analysis.ipynb in this repository. 
