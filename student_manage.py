import mysql.connector
import datetime
mysql=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="student_management"
)

def execute(query,users):
    mycursor = mysql.cursor()
    mycursor.execute(query, users)
    mysql.commit()

def add_Student():
    print("Adding a Student needs a following Details:")
    s_id=int(input("Enter Student ID:"))
    name=str(input("Enter Student Name:"))
    phone=str(input("Enter Student Phone Number:"))
    dob=str(input("Enter Student DOB: DD/MM/YYYY "))
    dept=str(input("Enter Student Department:"))
    s_type=str(input("Enter Student Type:"))
    mail=str(input("Enter Student Mail:"))
    location=str(input("Enter Student Locality:"))
    city=str(input("Enter Student City:"))
    pin=int(input("Enter Student PIN:"))
    user1=(s_id,name,dept,s_type)
    user2=(s_id,name,dob,mail,phone,location,city,pin)
    sql="insert into studentdetails values(%s,%s,%s,%s)"
    sql2="insert into details values(%s,%s,%s,%s,%s,%s,%s,%s)"
    execute(sql,user1)
    execute(sql2,user2)
    print("Student Details Added Successfully")

def update_Student():
    print("Updating a Student Details:")
    s_id=int(input("Enter Student ID:"))
    print("1. Mail_id change")
    print("2. Phone Number change")
    print("3. Location change")
    choice = int(input("Enter Choice:"))
    if choice == 1:
        mail=str(input("Enter new Student Mail:"))
        user=(mail,s_id)
        sql="update details set Mail_id=%s where S_id=%s"
        execute(sql,user)
        print("Student Details Updated Successfully")
    elif choice==2:
        phone=str(input("Enter new Phone Number:"))
        user=(phone,s_id)
        sql="update details set Phone_No=%s where S_id=%s"
        execute(sql,user)
        print("Details Updated Successfully")
    elif choice==3:
        location=str(input("Enter New Location:"))
        city=str(input("Enter New City:"))
        pin=int(input("Enter New PinCode:"))
        user=(location,city,pin,s_id)
        sql="update details set Locality=%s ,City=%s ,Pincode=%s where S_id=%s"
        execute(sql,user)
        print("Details Updated Successfully")
    else:
        print("Invalid Choice")

def view_Student():
    s_type=str(input("Enter type to View Student Details By type:"))
    mycursor=mysql.cursor()
    user=(s_type,)  ## need to give ',' to make it tuple otherwise it shows error
    sql="select * from studentdetails where Type=%s"
    mycursor.execute(sql, user)
    myresult=mycursor.fetchmany()
    for row in myresult:
        print(row)

def find_Student():
    print("Finding a Student Details:")
    print("1. By ID")
    print("2. By City")
    print("3. By Mail_id")
    choice = int(input("Enter Choice:"))
    if choice == 1:
        s_id=int(input("Enter Student ID:"))
        mycursor=mysql.cursor()
        user=(s_id,)
        sql="select * from details where S_id=%s"
        mycursor.execute(sql,user)
        myresult=mycursor.fetchall()
        for row in myresult:
            print(row)
    elif choice==2:
        city=str(input("Enter City:"))
        mycursor = mysql.cursor()
        user = (city,)
        sql = "select * from details where City=%s"
        mycursor.execute(sql, user)
        myresult = mycursor.fetchall()
        for row in myresult:
            print(row)
    elif choice==3:
        mail=str(input("Enter new Student Mail:"))
        mycursor = mysql.cursor()
        user = (mail,)
        sql = "select S_id,Name,Phone_No from details where Mail_id=%s"
        mycursor.execute(sql, user)
        myresult = mycursor.fetchone()
        for row in myresult:
            print(row)

def delete_Student():
    print("Deleting a Student Details:")
    s_id=int(input("Enter Student ID:"))
    user=(s_id,)
    sql="delete from details where S_id=%s"
    sql2="delete from studentdetails where S_id=%s"
    execute(sql,user)
    execute(sql2,user)
    print("Student Details Deleted Successfully")

def attendance():
    mycursor=mysql.cursor()
    sql="select S_id,S_name from studentdetails"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for r,s in myresult:
        print(r," ",s,end=" ")
        status=str(input("Enter Status:"))
        status=status[0]
        status.upper()
        dat=datetime.date.today()
        dat=dat.strftime("%d/%m/%Y")
        user=(r,s,dat,status)
        sql="insert into attendance values(%s,%s,%s,%s)"
        execute(sql,user)
        print()
    print("Attendance Updated Successfully")

def att_Report():
    mycursor=mysql.cursor()
    sqls="select S_id,S_name from studentdetails"
    mycursor.execute(sqls)
    myresults=mycursor.fetchall()
    sql="select S_id,Status from attendance"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for row in myresults:
        present = 0
        absent = 0
        id=row[0]
        name=row[1]
        for r,s in myresult:
            if r==id and s=="P":
                present+=1
            elif r==id and s=="A":
                absent+=1
        print(id,name,"Present",present,"Absent",absent)

while True:
    print("1. Add student")
    print("2. Update Student Details")
    print("3. View Students Details")
    print("4. Find Student information")
    print("5. Delete Student")
    print("6. Attendance Entry")
    print("7. View Report")
    print("8. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        add_Student()
    elif choice==2:
        update_Student()
    elif choice==3:
        view_Student()
    elif choice==4:
        find_Student()
    elif choice==5:
        delete_Student()
    elif choice==6:
        attendance()
    elif choice==7:
        att_Report()
    elif choice==8:
        break
    else:
        print("Invalid Choice")