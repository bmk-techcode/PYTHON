import csv 
file=open(r"C:\Users\mca16\demo3.csv","r")
content=csv.reader(file)

for i in content:
    print(i)
file.close()
