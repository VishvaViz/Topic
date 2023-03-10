import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Boogieman@1",
    database="world",
)

#create the table
#mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE example (id int auto_increment primary key, name VARCHAR(255), address VARCHAR(255))")
#print("table created")


#insert value in table

mycursor=mydb.cursor()
sql="insert into example(name,address)values(%s,%s)"
name=input("Enter Your name:")
address=input("Enter the Address:")
val=(name,address)
mycursor.execute(sql,val)
mydb.commit()
print("row instered")

