import sqlite3

db_connection = sqlite3.connect("iris_cv.db")
# CURSOR OBJECT
cursor = db_connection.cursor()

addData = """
insert into flower_info
(sepal_length,sepal_width,petal_length,petal_width,Class)
values(2,3,4,3,1)
"""
cursor.execute(addData)
db_connection.commit()