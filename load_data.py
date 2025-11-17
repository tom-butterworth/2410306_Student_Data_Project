import pandas as pd

#Create a dataframe from the data in the csv file
def load_csv():
    return pd.read_csv("student_grades.csv")