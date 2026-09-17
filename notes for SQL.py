

import sqlite3

#Connect to a database
#This will create an empty file on your computer with the name of the database
#if the file does not already exist
db_connection = sqlite3.connect("mydatabase.db")

x=input('Enter your name:')
y=int(input('Enter your age:'))

#create a cursor object, so python can talk to sqlite3
cursor = db_connection.cursor() # db connection is jst a name

#create a docstring which contains the SQL command for the cursor to run
createTable = '''create table if not exists users(
id integer primary key autoincrement,
name text not null,
age integer  
) STRICT'''

#Execute the SQL command 
#This will create an empty table in our database 
cursor.execute(createTable) #run the SQL command
db_connection.commit() #save the change to the database

#create a docstring which contains the SQL command for the cursor to run
addData = '''insert into users (name,age) values (?,?)''' #qsnt marks safe guard code
cursor.execute(addData,(x,y))
#save the changes to the database
db_connection.commit() #need to call commit or esle changes wont b changed

'''ths is only 1 way to reach info '''
#create a docstring which contains the SQL command for the cursor to run
fetchData = '''select * from users''' #star gets evrything
cursor.execute(fetchData)
#cursor.fetchall() retrieves all the remaining #rows of the table. If there are no 
#rows it #returns an empty list
rowsInTable = cursor.fetchall()
for row in rowsInTable:
    print(row)
