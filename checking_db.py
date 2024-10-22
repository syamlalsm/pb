import mysql.connector

db=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="1252",
                                   database="project")
mycursor=db.cursor()
# mycursor.execute("CREATE TABLE sample (name varchar(20),age int, id int primary key auto_increment)")
# mycursor.execute("insert into sample (name, age) values (%s,%s)", ("syam",21)) 
# db.commit()

mycursor.execute("select name from sample")
for x in mycursor:
    if x[0]==21:
        print("file exist")
    else:
        print(x)

