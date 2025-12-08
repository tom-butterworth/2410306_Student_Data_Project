from db_conn import get_connection, create_database #returns database connection so we can query it
from load_data import load_csv #to be used to create dataframe used when calling calculations etc
from calculations import * #import all functions from calculations.py for us to use later
from gui.gui_main_menu import open_main_menu

#create a dataframe from the student grades csv file
df = load_csv()

#create a database containing student grades table
create_database()

#open the main menu window
open_main_menu()

#using our database connection, call functions to calculate and display information
with get_connection() as conn:
    # print(f"Average grade: {calculate_average_grade(df)}")
    print(f"Average grade from SQL: {calculate_average_grade_sql(conn)}\n")

    # print(f"Average attendance: {calculate_average_attendance(df)}")
    print(f"Average attendance from SQL: {calculate_average_attendance_sql(conn)}\n")

    # print(f"Number of passes: {get_number_of_passes(df)}")
    print(f"Number of passes from SQL: {get_number_of_passes_sql(conn)}\n")

    # print(f"Number of fails: {get_number_of_fails(df)}")
    print(f"Number of fails from SQL: {get_number_of_fails_sql(conn)}\n")

    # print(f"Number of As: {get_number_of_As(df)}")
    print(f"Number of As from SQL: {get_number_of_As_sql(conn)}\n")

    # print(f"Number of Bs: {get_number_of_Bs(df)}")
    print(f"Number of Bs from SQL: {get_number_of_Bs_sql(conn)}\n")

    # print(f"Number of Cs: {get_number_of_Cs(df)}")
    print(f"Number of Cs from SQL: {get_number_of_Cs_sql(conn)}\n")

    # print(f"Average grade by country:\n{get_average_grade_per_country(df)}")
    print(f"Average grade by country from SQL:\n{get_average_grade_per_country_sql(conn)}\n")

    print(f"Correlation between attendance and grade: {get_correlation_attendance_and_grade(df)}")