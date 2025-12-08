from db_conn import create_database #returns database connection so we can query it
from load_data import load_csv #to be used to create dataframe used when calling calculations etc
from gui.gui_main_menu import open_main_menu
from gui.styles import setup_styles
import tkinter as tk

def main():
    root = tk.Tk() #from research, it's convention to use root as the name of the window/root for a tkinter gui
    root.withdraw() #to hide the root, as it's only used to open the main menu straight away anyway
    setup_styles(root, theme="light") #sets sun valley light theme, and applies any of my custom styles to widgets


    df = load_csv() #create a dataframe from the student grades csv file
    create_database() #create a database containing student grades table

    open_main_menu(root) #open main menu gui

    root.mainloop()


if __name__ == "__main__":
    main()

