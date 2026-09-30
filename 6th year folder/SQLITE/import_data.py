import sqlite3
import csv


flower=[]
with open('Iris_data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
      flower.append(row)
      



db_connection = sqlite3.connect("iris_cv.db")
# CURSOR OBJECT
cursor = db_connection.cursor()

addData = """
insert into flower_info
(sepal_length,sepal_width,petal_length,petal_width,Class)
values(?,?,?,?,?)
"""
for flower_data in flower:    
    cursor.execute(addData, flower_data)
db_connection.commit()