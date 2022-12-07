fil=open("Marks.txt","w")
lst=[]
for i in range(3):
    
    rollno=int(input("roll no:"))   
    marks=int(input("marks:"))
    grade=input("enter grade:")
    remarks=input("remarks(P/F)")
    lst.append(str(rollno)+"  ,  "+str(marks)+"  ,  "+grade+"  ,  "+remarks+"\n")
fil.writelines(lst)
fil.close()

