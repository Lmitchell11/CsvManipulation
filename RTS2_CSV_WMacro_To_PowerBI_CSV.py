#Tim Richmond, Liam Mitchell
#Nexteer RTS2-CSV + Macro formula = CSV for PowerBI
#6/27/2019
#End of this document contains information for the user when running the program

"""This program was made by Liam Mitchell, and Tim Richmond to assist with tedious data manipulation from RTS2 csv before it is entered into PowerDB, 
because excel is not good enough with its memory/macro functions on largescale files."""

import os #imports functions/tools that allow the program to access user/OS file directory
import re #imports functions/tools that allow the program to read/write files
import csv #imports functions/tools that allow the program to read/write .csv files, and some other behind the scenes stuff


fileNames = []                      #initializes array list that will hold file names in the following folder
for root, dirs, files in os.walk(r'C:\Users\nzy5hy\OneDrive - NEXTEER AUTOMOTIVE\Desktop\Programming\Python Programs\Actual Program Test'): #reads all of the files in the folder path
    for file in files:              #for loop reads file by file in folder
        if file.endswith('.csv'):   #only reads .csv files
            fileNames.append(file)  #adds file name to list for later content-appending


k1 = 0
k2 = 0
k3 = 0
j = 0                               #initializes j counter for setting previous date in for loop
daysCounter = 0                     #initializes dayCounter for iterating amount of days/(24h periods)
fileContent= []                     #initializes array that will read lines in file and temporarily store them for writing function. 
for file in fileNames:              #Reads file                        
    i = 0                           #initializes i counter for iterating through arrays/lines
    if (k1 < 1):
        k1 = 1
        k2 = 1
    with open(file, "r+") as f:
        if (k2 == 1):
            for line in f:
                currentLine = line.split(",")
                if (i < 4):                         #Reads/skips first 4 lines while adding a comma to keep good csv format
                    currentLine.append(",")         #adds comma to end of lines
                    fileContent.append(currentLine) #adds line to end of fileContent array for later output
                if (i == 4):                        #Line for headers in the file
                    currentLine.append("New Time")  #adds new header to end of headers
                    fileContent.append(currentLine)
                if (i >=5):
                    break
                i = i + 1
        if (k2 > 1):
            for k3 in range(1):
                next(f)
        for line in f:              #for loop reads line by line in the file
            currentLine = line.split(",")       #splits up line into array, seperates based off commas (CSV format)
            if (i >= 5):                            #All lines after the 5th line are for data
                if (j < 1):                         #Uses j counter
                    previousDate = currentLine[0]   #sets first date
                    j = j + 1
                    
                if (previousDate in currentLine[0]):    #Checks to see if date is the same as the last lines
                    newTime = currentLine[1]            #Takes Time out of line, [1] is the cell in the line.split array
                    newTime1 = newTime[1:3]             #takes first 2 ints out of string Time, [1:3] because(') is used/stored to denote time in RTS2
                    newTime1 = ("!" + (str(int(newTime1) + (daysCounter)*(24)))[0:len(newTime)] + newTime[3:13]) #uses math to add 24 hours according to how many days the counter is at, then prepends it back.
                    currentLine.append(newTime1)        #adds the new time format to the end of the line
                    fileContent.append(currentLine)     #stores the line in the temporary file contents for later output

                if (previousDate not in currentLine[0]):#if date is not the same as last lines, add 24 hours to daysCounter
                    daysCounter = daysCounter + 1       #adds 1 to days counter
                    previousDate = currentLine[0]       #Changes date to new date
                    newTime = currentLine[1]             
                    newTime1 = newTime[1:3]
                    newTime1 = ("!" + (str(int(newTime1) + (daysCounter)*(24)))[0:len(newTime)] + newTime[3:13])
                    currentLine.append(newTime1)
                    fileContent.append(currentLine)
            i = i + 1               #iterates once line is read, counting for if statements
    f.close()                       #closes file once all lines are read, "required"
    k2 = 2

i = 0                               #resets i counter for iterating to the next value in fileContent array while writing                     
with open("All_Data_Appended_With_New_Time.csv", "w+") as f:
    for line in fileContent:
        if (i < 4):                 #writes first 4 lines
            f.write(str(fileContent[i]))
            f.write("\n")
        if (i == 4):                #writes new header line
            f.write(str(fileContent[i]))
            f.write("\n")
        if (i >= 5):                #writes all data cells, including new cells
            f.write(str(fileContent[i]))
            f.write("\n")
        i = i + 1                   #iterates to the next line in array, and if statements
f.close()                           #closes file once all lines are read, "required"                    

"""Ensure that you have "All_Data_Appended_With_New_Time" csv file deleted out of the folder directory
before you launch the python program, or else it will throw an error like:
(((invalid literal for int() with base 10: '.1')))"""

"""Find + Replace All chars in the parenthesis ('), ("), ([) with () <--- nothing
Add the following chars back in using replace all, replacing (!) with (') <--Time"""
