import pandas as pd
import matplotlib.pyplot as plt
def menu():
    print("1.read contents of student table")
    print("2.add record to student table")
    print("3. delete record of student table")
    print("4.read contents of course table")
    print("5.read contents of batch table")
    print("6.read contents of department table")
    print("7.view performance of course table")
    print("8.graph  of performance")
    print("9.report card")
    print("10.list of students")
    print("11.graph  of courses")
    print("12.pie chart of performance")
    print("12.list of batches")
    print("12.line plot of percentage")
    
menu()
def readstudent():
    
    df=pd.read_csv("studentdata.csv",index_col=0)
    print(df)
def readcourse():
    df=pd.read_csv("Course.csv",index_col=0)
    print(df)
def readbatch():
    df=pd.read_csv("Batch.csv",index_col=0)
    print(df)
def readdept():
    df=pd.read_csv("Department.csv",index_col=0)
    print(df)
def addrecord():
    print()
    df=pd.read_csv("studentdata.csv",index_col=0)
    print(df)
    print()
    print()
    df1=pd.Series(data={"STUDENT ID":'CSBS2204',"NAME":"Shreya Sen","CLASS ROLL NUMBER":'04',"BATCH ID":'CSBS22'},name='X')
    df=df.append(df1,ignore_index=True)
    print(df)
def deleterecord():
    print()
    df=pd.read_csv("studentdata.csv",index_col=0)
    print(df)
    print()
    print()
    STUDENTID=int(input("enter id to delete"))
    df.drop(STUDENTID,axis=0,inplace=True)
    
    print(df)
def reportcard():
    print("ROLLNO","MARKS","GRADE","REMARKS")
    fil=open("Marks.txt","r")
    s=fil.read()
    print(s)
    fil.close()

def performance():
    df=pd.read_csv("Course.csv",usecols=["MARKS OBTAINED"])
    print()
    print(df)
    print()
def histogram():
    df=pd.read_csv("Course.csv")
    print(df)
    x=df["NAME"]
    y=df["MARKS OBTAINED"]
    plt.title("GRAPH")
    plt.xlabel("NAME")
    plt.ylabel("MARKS OBTAINED")
    plt.bar(x,y,color="blue")
    plt.show()
def listofstudents():
    df=pd.read_csv("Batch.csv",usecols=["STUDENT ID"])
    print()
    print(df)
    print()
def listofcourses():
    df=pd.read_csv("Batch.csv",usecols=["COURSE ID"])
    print()
    print(df)
    print()
def piechart():
    plt.style.use('bmh')
    df=pd.read_csv("Course.csv")
    x=df["NAME"]
    y=df["MARKS OBTAINED"]
    plt.pie(y,labels=x)
    plt.show()
def listofbatches():
    df=pd.read_csv("Department.csv",usecols=["BATCH ID"])
    print()
    print(df)
    print()
def lineplot():
    csv1=pd.read_csv("Batch.csv")
    csv1.head()
    csv2=pd.read_csv("Course.csv")
    csv2.head()
    mergeddata=csv1.merge(csv2,on=["COURSE ID"])
    d=mergeddata.head()
    print(d)
    x=d["BATCH ID"]
    y=d["MARKS OBTAINED"]
    plt.plot(x,y)
    plt.show()

opt=""
opt=int(input("enter your choice:"))
if opt==1:
    readstudent()
elif opt==2:
    addrecord()
elif opt==3:
    deleterecord()
elif opt==4:
    readcourse()
elif opt==5:
    readbatch()    
elif opt==6:
    readdept()
elif opt==7:
    performance()
elif opt==8:
    histogram()
elif opt==9:
    reportcard()
elif opt==10:
    listofstudents()
elif opt==11:
    listofcourses()
elif opt==12:
    piechart()
elif opt==13:
    listofbatches()
elif opt==14:
    lineplot()
else:
    print("invalid operation")
    print("\a")
   

