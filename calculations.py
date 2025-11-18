#load csv data into a dataframe
from load_data import load_csv
df = load_csv()

#get mean grade
def calculate_average_grade(df):
    return df["grade"].mean()

#get mean attendance
def calculate_average_attendance(df):
    return df["attendance"].mean()

#get number of passes (grades above 40)
def get_number_of_passes(df):
    return len(df[df["grade"] >= 40])

#get number of fails (grades below 40)
def get_number_of_fails(df):
    return len(df[df["grade"] < 40])

#get number of As (grades > 70)
def get_number_of_As(df):
    return len(df[df["grade"] >= 70])

#get number of Bs (grades between 60 and 70)
def get_number_of_Bs(df):
    return len(df[df["grade"].between(60, 70, inclusive="left")]) #inclusive left means lower bound is inclusive, upper bound is exclusive

#get number of Cs (grades between 40 and 60)
def get_number_of_Cs(df):
    return len(df[df["grade"].between(40, 60, inclusive="left")])

#gets the average grade for each country
def get_average_grade_per_country(df):
    return df.groupby("country")["grade"].mean()

def get_correlation_attendance_and_grade(df):
    return df["attendance"].corr(df["grade"])

def get_general_correlation(df):
    return df.corr()