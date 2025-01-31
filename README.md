# EC530_HW1
Objective for the Assignment:  If the user gives you two arrays of geo location, match each point in the first array to the closest one in the second array. 

Code is written in Python and uses a KDtree library as the data structure of choice to solve the problem. Originally, I used a nested for loop in pair with the haversine formula in order to calculate the shortest distance between points. This method is straightfoward but the time complexity is not great, O(n^2). To handle larger inputs, such as CSV files, using a KD tree is very beneficial. The code works for 3 different formats: using csv files, manually inputting data in dms format and manually inputting using latitude and longitude format. The algorithm paired with the KD tree is Kth nearest neighbor which also improves upon the original code.

I utilized Chat-GPT for aiding in writing test cases and debugging my code. 

The code also has comments throughout in order to aid in undestanding the purpose of each function and how they interact with one another. 
