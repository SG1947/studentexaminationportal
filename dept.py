import csv


def department():
    Csvfile = open('Department.csv', 'w', newline='')
    C =csv.writer(Csvfile)
    Lines=[]
    fields=["DEPARTMENT ID","DEPARTMENT NAME","BATCH ID"]
    while True:
        Studentid = input("Department ID:")
        
        deptname=input("enter department name:")
        batches=input("enter batch id:")
        Lines.append([Studentid,deptname,batches])
        Ch = input("More(Y/N)?")
        if Ch == 'N':
            break
    C.writerow(fields)
    C.writerows(Lines)
    Csvfile.close() 
     
    
    
       
    
def Display():
    Csvfile = open('Department.csv', 'r', newline='')
    C = csv.reader(Csvfile)
    for Line in C:
        print(Line)
    Csvfile.close() 
print("choose from the following options:")
while True:
    Option = input("1:CREATE DEPARTMENT TABLE 2:DISPLAY RECORD  ")
    
    if Option == "1":
        department()
    elif Option == "2":
        Display()
   
    else:
        break
