import streamlit as st
import pandas as pd
import mysql.connector
import datetime
st.title("EMPLOYEE MANAGEMENT SYSTEM")
choice=st.sidebar.selectbox("Menu",("Home","Employee","Admin"))
if (choice=="Home"):
    st.image("https://img.freepik.com/free-vector/communication-flat-icon_1262-18771.jpg?size=626&ext=jpg&ga=GA1.1.1745394327.1711030421&semt=ais")
    
elif(choice=="Employee"):
    login=False
    if 'login' not in st.session_state:
        st.session_state['login'] = False
    employeeID = st.text_input("Enter employee ID")
    employeename = st.text_input("Enter Employee Name")
    employeepwd = st.text_input("Enter password",type = "password")
    btn = st.button("Login")
    if btn:
       mydb=mysql.connector.connect(host="localhost",user="root",password="Abhishek.8922",database="employeemanagement")
       c=mydb.cursor()
       c.execute("select * from employeelogin")
       for r in c:
           if (r[0] == employeeID ,r[1] == employeename and r[2] == employeepwd):
               login = True
               st.session_state['login'] = True
               break
       if(not st.session_state['login']):
           st.write("Incorrect ID or Password")
    if(st.session_state['login']):
        st.write("Login Succssfull")
        choice2=st.selectbox("Features",("None","View All Employees", "Make Attendence"))
        if(choice2=="View All Employees"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="Abhishek.8922",database="employeemanagement")
            df=pd.read_sql("select * from employees",mydb)
            st.dataframe(df)
        elif(choice2=="Make Attendence"):
             employeeID = st.text_input("Enter Employee ID")
             btn2=st.button("Make attendence")
             if btn2:
                 login_datetime=str(datetime.datetime.now())
                 mydb=mysql.connector.connect(host="localhost",user="root",password="Abhishek.8922",database="employeemanagement")
                 c=mydb.cursor()
                 c.execute("INSERT INTO attendence values( %s,%s)",(employeeID,login_datetime))
                 mydb.commit()
                 st.header("Attendence made Succesfully")
elif(choice=="Admin"):
    if 'alogin' not in st.session_state:
        st.session_state['alogin'] = False
    adminID = st.text_input("Enter Admin ID")
    admin_name = st.text_input("Enter Admin Name")
    admin_pwd = st.text_input("Enter password",type = "password")
    btn = st.button("Login")
    if btn:
       mydb=mysql.connector.connect(host="localhost",user="root",password="Abhishek.8922",database="employeemanagement")
       c=mydb.cursor()
       c.execute("select * from admins")
       for r in c:
           if (r[0] == adminID ,r[1] == admin_name and r[2] == admin_pwd):
               login = True
               st.session_state['alogin'] = True
               break
       if(not st.session_state['alogin']):
           st.write("Incorrect ID or Password")
    if(st.session_state['alogin']):
        st.write("Login Succssfull")
        choice2=st.selectbox("Features",("None","View Attendence", "Add New Employee"))
        if(choice2=="View attedence"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="Abhishek.8922",database="employeemanagement")
            df=pd.read_sql("select * from attendence",mydb)
            st.dataframe(df)
        elif(choice2=="Add New Employee"):
             employeeID = st.text_input("Enter Employee ID")
             Employeename = st.text_input("Enter Employee Name")
             age=st.text_input("Enter Employee age")
             Salary=st.text_input("Enter Employee Sallary")                                        
             btn2=st.button("Add New Employee")
             if btn2:
                 mydb=mysql.connector.connect(host="localhost",user="root",password="Abhishek.8922",database="employeemanagement")
                 c=mydb.cursor()
                 c.execute("insert into employees values(%s,%s,s%,s%)",(employeeID,Employeename,age,Salary))
                 mydb.commit()
                 st.header("Employee Added Succesfully")
        
                   
