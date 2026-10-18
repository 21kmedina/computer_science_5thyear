import sqlite3

db_connection = sqlite3.connect("myowndatabase.db")

x=input('Enter your name:')
y=input
z=int(input('Enter your salery:'))

createTable = '''create table if not exists users(
id integer primary key autoincrement,
name text not null,
age integer  
) STRICT'''

cursor.execute(createTable)
db_connection.commit()

addData = '''insert into users (name,age) values (?,?,?)'''
cursor.execute(addData,(x,y,z))
