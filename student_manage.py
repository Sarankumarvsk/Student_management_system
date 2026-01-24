import pymysql
import datetime
# ---------------- DATABASE CONNECTION ----------------
try:
    mysql = pymysql.connect(
        host="localhost",
        user="root",
        password="root",     
        database="student_management"
    )
    print("Database Connected Successfully!")
except mysql.connector.Error as err:
    print("Connection Error:", err)
    exit()

# ---------------- COMMON EXECUTE FUNCTION ----------------
def execute(query, values):
    try:
        cursor = mysql.cursor()
        cursor.execute(query, values)
        mysql.commit()
    except mysql.connector.Error as e:
        mysql.rollback()
        print("Database Error:", e)
    finally:
        cursor.close()

# ---------------- ADD STUDENT ----------------
def add_Student():
    print("\n--- ADD STUDENT ---")
    try:
        s_id = int(input("Student ID: "))
        name = input("Student Name: ")
        dept = input("Department: ")
        s_type = input("Student Type: ")
        dob = input("DOB (YYYY-MM-DD): ")
        mail = input("Mail ID: ")
        phone = input("Phone Number: ")
        location = input("Locality: ")
        city = input("City: ")
        pin = int(input("PIN Code: "))

        execute(
            "INSERT INTO studentdetails VALUES (%s,%s,%s,%s)",
            (s_id, name, dept, s_type)
        )

        execute(
            "INSERT INTO details VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
            (s_id, name, dob, mail, phone, location, city, pin)
        )

        print("Student Added Successfully!")
    except ValueError:
        print("Invalid Input! ID & PIN must be numbers.")

# ---------------- UPDATE STUDENT ----------------
def update_Student():
    print("\n--- UPDATE STUDENT ---")
    s_id = int(input("Student ID: "))
    print("1. Update Mail\n2. Update Phone\n3. Update Location")
    choice = int(input("Choice: "))

    if choice == 1:
        mail = input("New Mail: ")
        execute("UPDATE details SET Mail_id=%s WHERE S_id=%s", (mail, s_id))
    elif choice == 2:
        phone = input("New Phone: ")
        execute("UPDATE details SET Phone_No=%s WHERE S_id=%s", (phone, s_id))
    elif choice == 3:
        location = input("New Locality: ")
        city = input("New City: ")
        pin = int(input("New PIN: "))
        execute(
            "UPDATE details SET Locality=%s, City=%s, Pincode=%s WHERE S_id=%s",
            (location, city, pin, s_id)
        )
    else:
        print("Invalid Choice")
        return

    print("Student Details Updated!")

# ---------------- VIEW STUDENTS ----------------
def view_Student():
    s_type = input("Enter Student Type: ")
    cursor = mysql.cursor()
    cursor.execute("SELECT * FROM studentdetails WHERE Type=%s", (s_type,))
    rows = cursor.fetchall()
    cursor.close()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No Records Found")

# ---------------- FIND STUDENT ----------------
def find_Student():
    print("\n--- FIND STUDENT ---")
    print("1. By ID\n2. By City\n3. By Mail")
    choice = int(input("Choice: "))
    cursor = mysql.cursor()

    if choice == 1:
        s_id = int(input("Student ID: "))
        cursor.execute("SELECT * FROM details WHERE S_id=%s", (s_id,))
    elif choice == 2:
        city = input("City: ")
        cursor.execute("SELECT * FROM details WHERE City=%s", (city,))
    elif choice == 3:
        mail = input("Mail ID: ")
        cursor.execute(
            "SELECT S_id, Name, Phone_No FROM details WHERE Mail_id=%s",
            (mail,)
        )
    else:
        print("Invalid Choice")
        cursor.close()
        return

    for row in cursor.fetchall():
        print(row)

    cursor.close()

# ---------------- DELETE STUDENT ----------------
def delete_Student():
    s_id = int(input("Student ID to Delete: "))
    execute("DELETE FROM details WHERE S_id=%s", (s_id,))
    execute("DELETE FROM studentdetails WHERE S_id=%s", (s_id,))
    print("Student Deleted Successfully!")

# ---------------- ATTENDANCE ----------------
def attendance():
    cursor = mysql.cursor()
    cursor.execute("SELECT S_id, S_name FROM studentdetails")
    students = cursor.fetchall()
    cursor.close()

    date = datetime.date.today().strftime("%Y-%m-%d")
    print("\nAttendance Date:", date)

    for sid, name in students:
        status = input(f"{name} (P/A): ").strip().upper()
        if status not in ("P", "A"):
            status = "A"
        execute(
            "INSERT INTO attendance VALUES (%s,%s,%s,%s)",
            (sid, name, date, status)
        )

    print("Attendance Updated!")

# ---------------- ATTENDANCE REPORT ----------------
def att_Report():
    cursor = mysql.cursor()
    cursor.execute("SELECT S_id, S_name FROM studentdetails")
    students = cursor.fetchall()

    cursor.execute("SELECT S_id, Status FROM attendance")
    records = cursor.fetchall()
    cursor.close()

    print("\n--- ATTENDANCE REPORT ---")
    for sid, name in students:
        present = sum(1 for r, s in records if r == sid and s == "P")
        absent = sum(1 for r, s in records if r == sid and s == "A")
        print(f"{sid} | {name} | Present: {present} | Absent: {absent}")

# ---------------- MAIN MENU ----------------
while True:
    print("""
--- STUDENT MANAGEMENT SYSTEM ---
1. Add Student
2. Update Student
3. View Students
4. Find Student
5. Delete Student
6. Attendance Entry
7. Attendance Report
8. Exit
""")

    try:
        choice = int(input("Enter Choice: "))
        if choice == 1:
            add_Student()
        elif choice == 2:
            update_Student()
        elif choice == 3:
            view_Student()
        elif choice == 4:
            find_Student()
        elif choice == 5:
            delete_Student()
        elif choice == 6:
            attendance()
        elif choice == 7:
            att_Report()
        elif choice == 8:
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice")
    except ValueError:
        print("Enter valid number!")

# ---------------- CLOSE CONNECTION ----------------
if mysql.is_connected():
    mysql.close()
