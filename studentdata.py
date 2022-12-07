import csv


def student():
    Csvfile = open('Studentdata.csv', 'w', newline='')
    C =csv.writer(Csvfile)
    Lines=[]
    fields=["STUDENT ID","NAME","CLASS ROLL NUMBER","BATCH ID"]
    while True:
        Studentid = input("Student ID:")
        Name = input(" Name:")
        classroll=int(input("enter class roll number:"))
        batchid=input("enter batch id:")
        Lines.append([Studentid,Name,classroll,batchid])
        Ch = input("More(Y/N)?")
        if Ch == 'N':
            break
    C.writerow(fields)
    C.writerows(Lines)
    Csvfile.close() 
     
    
    
       
    
def Display():
    Csvfile = open('Studentdata.csv', 'r', newline='')
    C = csv.reader(Csvfile)
    for Line in C:
        print(Line)
    Csvfile.close() 
print("choose from the following options:")
while True:
    Option = input("1:CREATE STUDENT TABLE 2:DISPLAY RECORD  ")
    
    if Option == "1":
        student()
    elif Option == "2":
        Display()
   
    else:
        break

