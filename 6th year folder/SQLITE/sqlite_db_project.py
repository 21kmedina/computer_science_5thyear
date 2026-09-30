import sqlite3

db_connection = sqlite3.connect("iris_cv.db")
# CURSOR OBJECT
cursor = db_connection.cursor()

create_table="""
create table if not exists flower_info(
sepal_length FLOAT NOT NULL,
sepal_width  FLOAT NOT NULL,
petal_length FLOAT NOT NULL,
petal_width  FLOAT NOT NULL,
Class  INTEGER NOT NULL
)

"""

cursor.execute(create_table)
db_connection.commit()