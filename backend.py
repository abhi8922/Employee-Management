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


