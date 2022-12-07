import csv


def course():
    Csvfile = open('Course.csv', 'w', newline='')
    C =csv.writer(Csvfile)
    Lines=[]
    fields=["COURSE ID","COURSE NAME","NAME","MARKS OBTAINED"]
    while True:
        Studentid = input("Course ID:")
        Name = input("Course Name:")
        marks=int(input("enter marks:"))
        Studentname=input("enter student name:")
        Lines.append([Studentid,Name,Studentname,marks])
        Ch = input("More(Y/N)?")
        if Ch == 'N':
            break
    C.writerow(fields)
    C.writerows(Lines)
    Csvfile.close() 
     
    
    
       
    
def Display():
    Csvfile = open('Course.csv', 'r', newline='')
    C = csv.reader(Csvfile)
    for Line in C:
        print(Line)
    Csvfile.close() 
print("choose from the following options:")
while True:
    Option = input("1:CREATE COURSE TABLE 2:DISPLAY RECORD  ")
    
    if Option == "1":
        course()
    elif Option == "2":
        Display()
   
    else:
        break
