# Employee-Management
Creating an Employment Management System using Python can be a great project. Here's a brief explanation of why, what, and how:

Why:
1. Organizational Efficiency: Streamlining employment-related processes enhances overall efficiency within an organization.
2. Automation:  Automation reduces manual workload, minimizing errors and ensuring consistency in data management.
3. Data Security: A centralized system helps in maintaining data security and access control, protecting sensitive employee information.

What:
Employment Management System Features:*
1. Employee Information Database: Store and manage employee details, such as personal information, job history, and contact details.
2. Attendance Tracking: Record and monitor employee attendance, facilitating payroll and performance analysis.
3. Leave Management: Implement a system to request, approve, and track employee leaves.
4. Performance Evaluation: Create a module for assessing and managing employee performance.
5. Payroll System: Automate payroll processes, including salary calculations, deductions, and tax withholdings.
6. User Authentication: Implement secure login systems to control access based on user roles.

How:
1. Choose a Database: Select a database system like SQLite or MySQL to store employee information securely.
2. GUI Development: Use a GUI library like Tkinter or PyQt to create an intuitive interface for users to interact with the system.
3. Data Validation: Implement robust data validation to ensure accuracy and prevent errors in the system.
4. Backend Logic: Develop the backend logic for processing requests, managing databases, and handling business rules.
5. User Authentication: Implement a secure authentication system to control access levels for different users.
6. Documentation: Provide clear documentation for users and developers, explaining how to use the system and its underlying structure.

				PYTHON
1.	Create a virtual environment
2.	Activate the virtual environment every time use it
3.	Install the package mysql-connector-python
4.	mydb=mysql.connector.connect(host="localhost",user="root",password="Abhishek.8922",database="employeemanagement")
5.	print(mydb)
6.	c=mydb.cursor()
7.	c.execute("select * from prformance")
8.	for r in c:
9.	    print(r)
10.	c2=mydb.cursor()
11.	c.execute("select * from employees")
12.	for r in c2:
13.	    print(r)
14.	c3=mydb.cursor()
15.	c.execute("select * from admins")
16.	for r in c3:
17.	    print(r)
import mysql.connector
import datetime
mydb=mysql.connector.connect(host="localhost",user="root",password="Abhishek.8922",database="employeemanagement")
employeeID=input("Enter epmloyeeID")
employeename=input("Enter employee Name")
employeepwd=input("Enter Password")
employeelogin=str(datetime.datetime.now())
c=mydb.cursor()
c.execute("insert into employeelogin values(%s,%s,%s)",(employeeID,employeename,employeepwd))
mydb.commit()
print("Employee login succesfully")


