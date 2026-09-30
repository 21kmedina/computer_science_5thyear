import sqlite3

db_connection = sqlite3.connect("iris_cv_db")

cursor = db_connection.cursor()

create_table="""
create table if not exists nombre_tabla (
Sepal_length FLOAT NOT NULL,
Sepal_width  FLOAT NOT NULL,
Petal_length FLOAT NOT NULL,
Petal_width  FLOAT NOT NULL,
Class  INTEGER NOT NULL
)

"""

cursor.execute(create_table)
db_connection.commit()