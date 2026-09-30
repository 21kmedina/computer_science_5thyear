import sqlite3

db_connection = sqlite3.connect("iris_cv.db")
# CURSOR OBJECT
cursor = db_connection.cursor()

read_data = """
select sepal_length,sepal_width,petal_length,petal_width,Class
from flower_info
"""
cursor.execute(read_data)
db_data=cursor.fetchall()
db_connection.commit()

add_sepal_l=0
add_sepal_w=0
for flower_row in db_data:
    add_sepal_l+=float(flower_row[0])
    add_sepal_w+=float(flower_row[1])

print('add_sepal_l: ' + str(add_sepal_l))
print('add_sepal_w: ' + str(add_sepal_w))
