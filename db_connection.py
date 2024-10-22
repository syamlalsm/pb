from tabulate import tabulate
import mysql.connector
import tkinter as tk
from tkinter import *
con=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="1252",
                                   database="project")
def insert(name,age,city):
    res=con.cursor()
    res.execute("select name from users")
    names=res.fetchall()
    f=0
    for x in names:
        if x[0]==name:
            f=1
    if f==0:
        res=con.cursor()
        res.execute("insert into users (name,age,city) values (%s,%s,%s)",(name,age,city))
        con.commit()
        print("\ndata insert sucessfully...")
    else:
        print("already exist")
    
    
def update(name,age,city,id):
    res=con.cursor()
    sql="update users set name=%s,age=%s,city=%s where id=%s"
    user=(name,age,city,id)
    res.execute(sql,user)
    con.commit()
    print("\ndata update sucessfully...")

def display():
    res=con.cursor()
    sql="SELECT ID,NAME,AGE,CITY from users"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))

def delete(id):
    res=con.cursor()
    sql="delete from users where id=%s"
    user=(id,)
    res.execute(sql,user)
    con.commit()
    print("\ndata delete sucessfully...")
while True:
    window=Tk()
    window.title("my window")
    window.geometry("250x150")
    b=Label(window,text="PLEASE ENTER ANYTHING  ",background="black",foreground="yellow",font=("helvetica",12,"bold"),padx=5,pady=5)
    b.pack() 
    window.config(bg="green")
    window.mainloop()
    print("\n1.Insert \n2.Update \n3.Display \n4.Delete \n5.Exit")
    choice=int(input("enter your choice: "))
    if choice==1:
        name=input("enter your name: ")
        age=int(input("enter your age:"))
        city= input("enter your city: ")   
        insert(name,age,city)
        
    elif choice==2:
        id=int(input("enter id wants to update: "))
        name=input("enter your name: ")
        age=int(input("enter your age: "))
        city=input("enter your city: ")
        update(name,age,city,id)
    elif choice==3:
        display()
    elif choice==4:
        id=input("enter id to delect: ")
        delete(id)
    elif choice==5:
        print("\nexit sucessfully...")
        quit()
    else:
        print("\ninvalid entry...")