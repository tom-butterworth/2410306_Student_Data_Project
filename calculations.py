#load csv data into a dataframe
from load_data import load_csv
df = load_csv()

#get mean grade using pandas
def calculate_average_grade(df):
    return df["grade"].mean()

#get mean grade from sql
def calculate_average_grade_sql(conn):
    cur = conn.cursor()
    #if fetchone not present, execute() returns a cursor object rather than the actual results. [0] as fetchone returns tuple (because sql is rows), so [0] gives us the actual value
    return cur.execute("SELECT AVG(grade) FROM tbl_student_grades").fetchone()[0]

#get mean attendance
def calculate_average_attendance(df):
    return df["attendance"].mean()

#get mean attendance from sql
def calculate_average_attendance_sql(conn):
    cur = conn.cursor()
    return cur.execute("SELECT AVG(attendance) FROM tbl_student_grades").fetchone()[0] #again, fetchone used as above

#get number of passes (grades above 40)
def get_number_of_passes(df):
    return len(df[df["grade"] >= 40])

#get number of passes from sql
def get_number_of_passes_sql(conn):
    cur = conn.cursor()
    return cur.execute("SELECT COUNT(grade) FROM tbl_student_grades WHERE grade > 40").fetchone()[0]

#get number of fails (grades below 40)
def get_number_of_fails(df):
    return len(df[df["grade"] < 40])

#get number of fails from sql
def get_number_of_fails_sql(conn):
    cur = conn.cursor()
    return cur.execute("SELECT COUNT(grade) FROM tbl_student_grades WHERE grade < 40").fetchone()[0]

#get number of As (grades >= 70)
def get_number_of_As(df):
    return len(df[df["grade"] >= 70])

#get number of As from sql (grade >= 70)
def get_number_of_As_sql(conn):
    cur = conn.cursor()
    return cur.execute("SELECT COUNT(grade) FROM tbl_student_grades WHERE grade >= 70").fetchone()[0]

#get number of Bs (grades between 60 and 70)
def get_number_of_Bs(df):
    return len(df[df["grade"].between(60, 70, inclusive="left")]) #inclusive left means lower bound is inclusive, upper bound is exclusive

#get number of Bs from sql (60 <= grade < 70)
def get_number_of_Bs_sql(conn):
    cur = conn.cursor()
    return cur.execute("SELECT COUNT(grade) FROM tbl_student_grades WHERE grade >= 60 and grade < 70").fetchone()[0]

#get number of Cs (grades between 40 and 60)
def get_number_of_Cs(df):
    return len(df[df["grade"].between(40, 60, inclusive="left")])

#get number of Cs from sql (40 <= grade < 60)
def get_number_of_Cs_sql(conn):
    cur = conn.cursor()
    return cur.execute("SELECT COUNT(grade) FROM tbl_student_grades WHERE grade >= 40 and grade < 60").fetchone()[0]

#gets the average grade for each country
def get_average_grade_per_country(df):
    return df.groupby("country")["grade"].mean()

#get average grade per country from sql. returns list of tuples [(country, avg), (country, avg), (country, avg)]
def get_average_grade_per_country_sql(conn):
    cur = conn.cursor()
    return cur.execute("SELECT COUNTRY, AVG(grade) FROM tbl_student_grades GROUP BY country").fetchall()

#gets a correlation between attendance and grade. .corr returns between -1 (exact negative correlation) and 1 (exact positive correlation). 0 means no correlation.
def get_correlation_attendance_and_grade(df):
    return df["attendance"].corr(df["grade"])