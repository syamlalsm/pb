import mysql.connector
con=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="1252",
                                   database="project")

def newsignup():
    res=con.cursor()
    sql="insert into signup values ('self.full_name','')"
def update():
    pass
def display():
    pass
def delete():
    pass
while True:
        print("1.")