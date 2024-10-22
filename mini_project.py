import tkinter as tk
from PIL import Image, ImageTk
from tabulate import tabulate
import random
import mysql.connector
con=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="1252",
                                   database="project")
"""
try:
   cursor = connection.cursor()
   cursor.execute(CREATE TABLE IF NOT EXISTS signup (
    Name VARCHAR(20) NOT NULL,
    Age INT NOT NULL,
    PhNo BIGINT,
    Place VARCHAR(20),
    Username VARCHAR(20) NOT NULL,
    Password VARCHAR(20) NOT NULL,
    AccountNo INT NOT NULL,
    PRIMARY KEY (Username)  -- Assuming Username is a unique identifier)
    );

    cursor = connection.cursor()
    cursor.execute(CREATE TABLE IF NOT EXISTS accbalance (
    Username VARCHAR(20) NOT NULL,
    Balance INT,
    FOREIGN KEY (Username) REFERENCES signup(Username))
    );
    print("Database created successfully (if it didn't exist).")

except as e:
    print("Tables are already created")
"""
class User:

    def __init__(self, full_name=None, dob=None, phone=None, place=None, username=None, password=None,accountno=None):
        self.full_name = full_name
        self.age = dob
        self.phone = phone
        self.place = place
        self.username = username
        self.password = password
        self.accountno=accountno
    
    def signup(self):
        self.username = input("ENTER YOUR USERNAME: ")
        res=con.cursor()
        res.execute("select Username from signup")
        signup=res.fetchall()
        con.commit()
        f=0
        for x in signup:
            if x[0]==self.username:
                f=1
        if f==1:
            print("sorry username is already exist please enter new one")
        else:
            print("'Username is available'... :)")
            self.full_name = input("ENTER YOUR FULL NAME: ")
            self.age = int(input("ENTER YOUR AGE: "))
            if self.age<18 or self.age>70:
                print("According to our policy you can't access our features sorry....:()")
            else:
                self.phone = input("ENTER YOUR PHONE NUMBER: ")
                length=len(self.phone)
                if length<10 or length>10: 
                    print("please enter valid '10' digit phone number")
                else:
                    self.place = input("ENTER YOUR PLACE: ")    
                    self.password = input("ENTER YOUR PASSWORD: ")
                    self.accountno= random.randint(999999,99999999)
                    res=con.cursor()
                    sql="insert into signup (Name,Age,PhNo,Place,Username,Password,AccountNo) values (%s,%s,%s,%s,%s,%s,%s)"
                    user=(self.full_name,self.age,self.phone,self.place,self.username,self.password,self.accountno)
                    res.execute(sql,user)
                    con.commit()
                    print("Account created successfully...!")
                    print(f"your accountno is '{self.accountno}' save this for further use")
            
    def login(self):
        uname = input("ENTER YOUR USERNAME: ")
        ps = input("ENTER YOUR PASSWORD: ") 
        res=con.cursor()
        res.execute("select Username,Password from signup")
        signup=res.fetchall()
        con.commit()
        f=0
        for x in signup:
            if x[0]==uname:
                if x[1]==ps:
                    f=1
        if f==1:
            res=con.cursor()
            query="select Name from signup where Username=%s"
            res.execute(query,(uname,))
            username=res.fetchall()
            con.commit()
            if username:
                s=username[0]
                p=''.join(s)
                print("Login successful! Welcome...",p,"\n")
                while True:
                    print("1.CREDIT \n2.DEBIT \n3.CHECKING BALANCE \n4.EXIT")
                    choice=int(input("enter your choice: "))
                    if choice==1:
                        cr_amount=int(input("enter your depositing amount: "))
                        if cr_amount>0:
                            res=con.cursor()
                            res.execute("select username from accbalance")
                            depo=res.fetchall()
                            con.commit()
                            d=0
                            for x in depo:
                                if x[0]==uname:
                                    d=1
                            if d==1:
                                con.cursor()
                                query1="select balance from accbalance where username=%s"
                                res.execute(query1,(uname,))
                                add_balance=res.fetchall()
                                if add_balance:
                                    ab=add_balance[0]
                                    acbal=int(''.join(map(str,ab)))
                                    credit=acbal+cr_amount
                                    res=con.cursor()
                                    bal_query="update accbalance set balance=%s where username=%s"
                                    bal_query1=(credit,uname)
                                    res.execute(bal_query,bal_query1)
                                    con.commit()
                                    root = tk.Tk()
                                    root.title("Cash Depositing")
                                    root.geometry("500x400")  
                                    image = Image.open("D:\syam\kinder\Deposit.png")
                                    image = image.resize((350, 300), Image.LANCZOS)  
                                    photo = ImageTk.PhotoImage(image)
                                    image_label = tk.Label(root, image=photo)
                                    image_label.pack(pady=(20, 10))  
                                    text_label = tk.Label(root, text="sucessfully deposited !", font=("Arial", 16))
                                    text_label.pack()
                                    root.mainloop()
                                    print("sucessfully deposited ",cr_amount," rupee...\n")
                            if d==0:
                                con.cursor()
                                res.execute("insert into accbalance (username,balance) values(%s,%s)",(uname,cr_amount))
                                con.commit()
                                root = tk.Tk()
                                root.title("Cash Depositing")
                                root.geometry("500x400")  
                                image = Image.open("D:\syam\kinder\Deposit.png")
                                image = image.resize((350, 300), Image.LANCZOS)  
                                photo = ImageTk.PhotoImage(image)
                                image_label = tk.Label(root, image=photo)
                                image_label.pack(pady=(20, 10))  
                                text_label = tk.Label(root, text="sucessfully deposited !", font=("Arial", 16))
                                text_label.pack()
                                root.mainloop()
                                print("sucessfully deposited ",cr_amount," rupee...\n")
                        else:
                            print("amount you entered is can't readable....\n")
                    elif choice==2:
                        wd_amount=int(input("enter amount wants to be withdraw: "))
                        if wd_amount>0:
                            res=con.cursor()
                            res.execute("select username from accbalance")
                            depo=res.fetchall()
                            con.commit()
                            w=0
                            for x in depo:
                                if x[0]==uname:
                                    w=1
                            if w==1:
                                con.cursor()
                                query1="select balance from accbalance where username=%s"
                                res.execute(query1,(uname,))
                                add_balance=res.fetchall()
                                if add_balance:
                                    ab=add_balance[0]
                                    acbal=int(''.join(map(str,ab)))
                                    withdraw=acbal-wd_amount
                                    if wd_amount>acbal:
                                        root = tk.Tk()
                                        root.title("Zero Balance")
                                        root.geometry("500x400")   
                                        image = Image.open("D:\syam\kinder\Zero balance.png")
                                        image = image.resize((350, 300), Image.LANCZOS)  
                                        photo = ImageTk.PhotoImage(image)
                                        image_label = tk.Label(root, image=photo)
                                        image_label.pack(pady=(20, 10))  
                                        text_label = tk.Label(root, text="Please Check Your Balance... !", font=("Arial", 16))
                                        text_label.pack()
                                        root.mainloop()
                                        print("withdrawing is not possible please check your balance...\n")
                                        break
                                    else:
                                        res=con.cursor()
                                        bal_query="update accbalance set balance=%s where username=%s"
                                        bal_query1=(withdraw,uname)
                                        res.execute(bal_query,bal_query1)
                                        con.commit()
                                        root = tk.Tk()
                                        root.title("Cash Withdrawel")
                                        root.geometry("500x400")   
                                        image = Image.open("D:\syam\kinder\Deposit.png")
                                        image = image.resize((350, 300), Image.LANCZOS)  
                                        photo = ImageTk.PhotoImage(image)
                                        image_label = tk.Label(root, image=photo)
                                        image_label.pack(pady=(20, 10))  
                                        text_label = tk.Label(root, text="sucessfully withdrawed !", font=("Arial", 16))
                                        text_label.pack()
                                        root.mainloop()
                                        print("sucessfully withdrawed ",wd_amount," rupee...\n")
                            if w==0:
                                root = tk.Tk()
                                root.title("Checking Balance")
                                root.geometry("500x400")   
                                image = Image.open("D:\syam\kinder\Zero balance.png")
                                image = image.resize((350, 270), Image.LANCZOS)  
                                photo = ImageTk.PhotoImage(image)
                                image_label = tk.Label(root, image=photo)
                                image_label.pack(pady=(20, 10))  
                                text_label = tk.Label(root, text="Sorry Your Account Balance Is 'ZERO'...", font=("Arial", 16))
                                text_label.pack()
                                root.mainloop()
                                print("\nsorry your account balance is '0'...\nplease deposit money...\nExiting to home page...\n")
                        else:
                            print("amount you entered is can't readable....\n")
                        
                    elif choice==3:
                        con.cursor()
                        query1="select balance from accbalance where username=%s"
                        res.execute(query1,(uname,))
                        balance=res.fetchall()
                        if balance:
                            b=balance[0]
                            bt=''.join(map(str,b))
                            print("\n-------------------------")
                            print("YOUR CURRENT BALANCE :",bt)
                            print("-------------------------\n")
                        else:
                            print("current balance = '0'" )
                    elif choice==4:
                        print("Exiting to home page...")
                        break
                    else:
                        print("please enter valid number")
        else:
            print("incorrect username/password")

    def ad_display(self):
        res=con.cursor()
        sql="SELECT Name,Age,PhNo,Place,Username,Password,Accountno from signup"
        res.execute(sql)
        result=res.fetchall()
        print(tabulate(result,headers=["NAME","AGE","PHONE.NO","PLACE","USERNAME","PASSWORD","ACCOUNT.NO"]))

    def ad_delete(self):
        dl_user=input("enter user name to delete: ")
        res=con.cursor()
        sql="delete from signup where Username=%s"
        user=(dl_user,)
        res.execute(sql,user)
        con.commit()
        print("\ndata delete sucessfully...")

    def ad_balance(self):
        print()
        res=con.cursor()
        sql="SELECT username,balance from accbalance"
        res.execute(sql)
        result=res.fetchall()
        print(tabulate(result,headers=["USERNAME","BALANCE"]))

    def ad_update(self):
        user_name = input("ENTER USERNAME for UPDATE: ")
        res=con.cursor()
        res.execute("select Username from signup")
        signup=res.fetchall()
        con.commit()
        f=0
        for x in signup:
            if x[0]==user_name:
                f=1
        if f==1:
            print("Username is matching you can change data...\n")
            newuser=input("ENTER EXISTING USERNAME: ")
            res=con.cursor()
            res.execute("select Username from signup")
            signup=res.fetchall()
            con.commit()
            b=0
            for x in signup:
                if x[0]==user_name:
                    b=0
            if b==1:
                print("USER NAME IS ALREADY EXIST")
            else:
                try:
                    new_full_name = input("ENTER YOUR FULL NAME: ")
                    new_age = int(input("ENTER YOUR AGE: "))
                    if new_age<18 or new_age>70:
                        print("According to our policy you can't access our features sorry....:()")
                    else:
                        new_phone = input("ENTER YOUR PHONE NUMBER: ")
                        len_phone=len(new_phone)
                        if len_phone<10 or len_phone>10: 
                            print("please enter valid '10' digit phone number")
                        else:
                            new_place = input("ENTER YOUR PLACE: ")  
                            new_user=newuser  
                            new_password = input("ENTER YOUR PASSWORD: ")
                            new_accountno= random.randint(999999,99999999)
                            res=con.cursor()
                            sql="update signup set Name=%s,Age=%s,PhNo=%s,Place=%s,Username=%s,Password=%s,AccountNo=%s where Username=%s"
                            user=(new_full_name,new_age,new_phone,new_place,new_user,new_password,new_accountno,user_name)
                            res.execute(sql,user)
                            con.commit()
                            print("Account created successfully...!")
                            print(f"your accountno is '{new_accountno}' save this for further use")
            
                except:
                    print("\nupdation is not possible\nuse existing username....")
        else:
           print("sorry your user name is wrong")
class PiggyBank:
    def __init__(self):
        self.user = None
    def start(self):
        window=tk.Tk()
        window.title("PIGGY BANK")
        # window.geometry("740x175")
        heading=tk.Label(window,text="PIGGY BANK SOFTWARE",background="cyan",foreground="red",font=("helvetica",14,"bold"),padx=5,pady=5)
        heading.pack() 
        des=tk.Label(window,text="Our Piggy Bank Software is a user-friendly, secure, and feature-rich\n"
                   "application designed for individuals to manage their savings efficiently. Authorized users can create\n"
                    "accounts, deposit, withdraw, and check balances while enjoying robust security and data privacy measures.",
                    foreground="black",font=("helvetica",10,"bold"),padx=5,pady=5)
        des.pack()
        f=tk.Label(window,text="Key Features:",foreground="black",font=("helvetica",12,"bold"),padx=5,pady=5)
        f.pack()
        features=tk.Label(window,text="User Account Management: Create, manage, and secure individual accounts.\n"
                       "Transaction Management: Deposit, withdraw, and check balances.\n"
                       "Strong Security: Authorized access with username/password authentication.\n"
                       "Admin Module: Comprehensive privileges for administrators.\n"
                       "User History: Track current transaction history.\n"
                       "Login Window: Secure access with correct username/password.",
                       foreground="black",font=("helvetica",10,"bold"),padx=5,pady=5)
        features.pack()
        b=tk.Label(window,text="Benefits:",foreground="black",font=("helvetica",12,"bold"),padx=5,pady=5)
        b.pack()
        benifits=tk.Label(window,text="Secure Savings: Protect your money with robust security measures.\n"
                       "Easy Management: Simplify savings tracking and transactions.\n"
                       "Personalized Accounts: Create and manage individual accounts.\n"
                       "Transparency: View transaction history and track spending.\n"
                       "Administrative Control: Monitor and manage all accounts.\n"
                       "Data Privacy: Ensure confidentiality of user information.\n"
                       "Convenience: Accessible and user-friendly interface.",
                       foreground="black",font=("helvetica",10,"bold"),padx=5,pady=5)
        benifits.pack()
        window.config()
        window.mainloop()
        print("\033[1;33m=>> PIGGY BANK <<=\033[0m")
        
        while True:
            print("\n1. LOGIN\n2. SIGNUP\n3. EXIT\n4. ADMIN PAGE")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.user=User()
                self.user.login()
            elif choice == 2:
                self.user = User()
                self.user.signup()
            elif choice == 3:
                print("Exiting...")
                break
            elif choice==4:
                self.ad_user=input("ENTER  admin's USERNAME: ")
                self.ad_pass=input("ENTER admin;s PASSWORD: ")
                inbuilt_user="admin"
                inbuilt_pass="123"
                if self.ad_user==inbuilt_user and self.ad_pass==inbuilt_pass:
                    print("welcome ADMIN......!\nNote - you can select one service at a time\n")
                    print("1. Display members \n2. Update the list \n3. Add new member \n4. Delete a member \n5. Bank balance \n6. Exit")
                    choice=int(input("enter your choice: "))
                    while True:
                        if choice==1:
                            self.user=User()
                            self.user.ad_display()
                            break
                        elif choice==2:
                            self.user = User()
                            self.user.ad_update()
                            break
                        elif choice==3:
                            self.user = User()
                            self.user.signup()
                            break
                        elif choice==4:
                            self.user = User()
                            self.user.ad_delete()
                            break
                        elif choice==5:
                            self.user = User()
                            self.user.ad_balance()
                            break
                        elif choice==6:
                            break
                        else:
                            print("Invalid choice.....")
                else:
                    print("invalid username/password....")
            else:
                print("Invalid choice.")
app = PiggyBank()
app.start()



 