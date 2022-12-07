import csv


def batch():
    Csvfile = open('Batch.csv', 'w', newline='')
    C =csv.writer(Csvfile)
    Lines=[]
    fields=["BATCH ID","BATCH NAME","DEPARTMENT ID","COURSE ID","STUDENT ID"]
    while True:
        Studentid = input("Batch ID:")
        Name = input("Batch Name:")
        deptname=input("enter department ID:")
        courselist =input("course id:")
        liststudents=input("enter student id:")
        Lines.append([Studentid,Name,deptname,courselist,liststudents])
        Ch = input("More(Y/N)?")
        if Ch == 'N':
            break
    C.writerow(fields)
    C.writerows(Lines)
    Csvfile.close() 
     
    
    
       
    
def Display():
    Csvfile = open('Batch.csv', 'r', newline='')
    C = csv.reader(Csvfile)
    for Line in C:
        print(Line)
    Csvfile.close() 
print("choose from the following options:")
while True:
    Option = input("1:CREATE BATCH TABLE 2:DISPLAY RECORD")
    
    if Option == "1":
        batch()
    elif Option == "2":
        Display()
   
    else:
        break
