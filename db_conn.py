import sqlite3
from load_data import load_csv


#returns database connection to sqlite db, to be used later by any functions querying/using the database
def get_connection():
    return sqlite3.connect("student_grades.db")

#create a database/table in a database, if one is present then replace it
def create_database():
    df = load_csv() #load csv data into a dataframe "df"
    with get_connection() as conn: #using our function above to get a database connection
        #below: use sql to create table with our connection, replace any existing table of same name, do not add an index column
        df.to_sql("tbl_student_grades", conn, if_exists="replace", index=False)

# print every row from student grades table in db
# cur = get_connection()
# for row in cur.execute('SELECT * FROM tbl_student_grades'):
#     print(row)