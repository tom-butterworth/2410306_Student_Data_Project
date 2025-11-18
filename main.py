from calculations import * #import all functions from calculations.py for us to use later
from plots import * #import everything from plots.py to display graphs later

#load csv data into a dataframe
# from load_data import load_csv
# df = load_csv()

print(f"Average grade: {calculate_average_grade(df)}")

print(f"Average attendance: {calculate_average_attendance(df)}")

print(f"Number of fails: {get_number_of_fails(df)}")

print(f"Number of passes: {get_number_of_passes(df)}")

print(f"Number of As: {get_number_of_As(df)}")

print(f"Number of Bs: {get_number_of_Bs(df)}")

print(f"Number of Cs: {get_number_of_Cs(df)}")

print(f"Average grade by country: {get_average_grade_per_country(df)}")

print(f"Correlation between attendance and grade: {get_correlation_attendance_and_grade(df)}")