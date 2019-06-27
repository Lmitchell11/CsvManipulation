This program was made by Liam Mitchell, and Tim Richmond on 6/27/2019 to assist with tedious data manipulation from RTS2 csv before it is entered into PowerDB,
because excel is not good enough with its memory/macro functions on largescale files.
This programs appends all the files (day-to-day test results) in a folder, into one large file, while also adding an extra column which contains the new timeline data.


You can launch this program by double clicking the .py file in the folder, or by pressing F5 or run in IDLE.
If you want to modify this program or view the code, open it in "Python IDLE"

Instruction Steps:

1.	Make sure all of the files are in the same folder directory as this program.

2.	Make sure that all of the files name's in the folder directory are in numerical order from the date they were created.

3.	Modify the code in line 15, or the one that says: "for root, dirs, files in os.walk(r'C:\Users\....'):" ensuring that it leads to (Step 1) folder PATH.

4.	Ensure that you have "All_Data_Appended_With_New_Time" csv file deleted out of the folder directory before you launch the python program, or it will throw error: (((invalid literal for int() with base 10: '.1')))

5.	Launch the program

6.	The file "All_Data_Appended_With_New_Time" shall be created and needs to be modified because of added in delimiters due to .csv manipulation in arrays.

7. 	Using the (CTRL + F) Find & Replace All function in some type of program similar to notepad++, find and replace all following chars in the parenthesis ('), ("), ([), (]) with () <--- Nothing.

8. 	Add the following chars back in using Find + Replace All function like in (Step 7), replacing (!) with (') <--Time denotation.

9.	Save "All_Data_Appended_With_New_Time" after making changes to the file.

10.	The file "All_Data_Appended_With_New_Time" is now ready for input into PowerDB.

