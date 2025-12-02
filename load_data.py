import pandas as pd

#Create a dataframe from the data in the csv file
def load_csv(filepath = r"data/student_grades.csv"):
    return pd.read_csv(filepath)