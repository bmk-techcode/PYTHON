#Write a python program to read specific column of a given CSV file and print the content of the columns

import csv 
file=open(r"C:\Users\mca16\demo3.csv","r")
content=csv.reader(file)
index=int(input("Enter the column_index to be read"))
for i in content:
    print(i[index])
file.close()
