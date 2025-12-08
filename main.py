from db_conn import create_database #returns database connection so we can query it
from load_data import load_csv #to be used to create dataframe used when calling calculations etc
from gui.gui_main_menu import open_main_menu

#create a dataframe from the student grades csv file
df = load_csv()

#create a database containing student grades table
create_database()

#open the main menu window
open_main_menu()

