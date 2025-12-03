import os
import sqlite3
from tkinter import messagebox

from load_data import load_csv


#returns database connection to sqlite db, to be used later by any functions querying/using the database
def get_connection():
    try:
        base_directory = os.path.dirname(os.path.dirname(__file__)) #go one level up from current file's file path, for example if in /gui sub folder
        db_path = os.path.join(base_directory, 'students.db')
        return sqlite3.connect(db_path)

        # return sqlite3.connect(r"data/student_grades.db") #r used to treat as a raw string, avoids things like \n being treated as a new line
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

#create a database/table in a database, if one is present then replace it
def create_database():
    try:
        df = load_csv() #load dataframe from load_data.py into a dataframe "df" here
        with get_connection() as conn: #using our function above to get a database connection
            #use sql to create table with our connection, replace any existing table of same name, do not add an index column
            df.to_sql("tbl_student_grades", conn, if_exists="replace", index=False)
    except Exception as e:
        print(f"Error: {e}")