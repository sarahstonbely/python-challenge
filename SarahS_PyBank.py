
#figure out number of diff months (use an if statement; 
# if the one is the same to the next....find where we did this; 
# if y == the one before... else skip)

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('Documents', 'Rutgers\ DataViz\ course', 'RUTJC201904DATA3-master',
    'hw', 'week3', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')

# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:
     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

print(csvreader)

   # Read the header row first (skip this step if there is no header)
#csv_header = next(csvreader)
#print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader:
        #print(row)

#map out how to solve:
#1.figure out how many different months are represented (if statement + total #)
#2.add up all the profits
#3. add up all the losses
#4. subtract the losses from the profit for a net amount
#5. identify the highest profit and say which date it occurred
#6. identify the greatest loss and say which date it occurred on
#7. print the code to the terminal and upload the code and the results to the repo


#loop through all the rows
#for i = (2 to 88):
    
#if i == (i - 1)
