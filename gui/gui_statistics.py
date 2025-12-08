import tkinter as tk
from gui.gui_helpers import safe_close_window
from tkinter import ttk
from db_conn import get_connection
from calculations import calculate_average_grade_sql, calculate_average_attendance_sql, get_number_of_passes_sql, get_number_of_fails_sql, get_number_of_As_sql, get_number_of_Bs_sql, get_number_of_Cs_sql
from gui.gui_helpers import centre_window

#open and display the window. Everything related to building and using this window needs to be in the function.
#this presents things like database connections happening at import time and also prevents scope errors
def open_statistics_gui():
    win_statistics = tk.Toplevel() #creates new window on top of the current/main one
    win_statistics.title("Statistics")
    centre_window(win_statistics, 400, 350)

    #connect to database
    conn = get_connection()

    #create labels to display results when a button is clicked to do so, not applying .pack method yet so it doesn't show and create empty space before any results are requested/displayed
    lblDisplayResult = tk.Label(win_statistics,text="", font=("Segoe UI", 12, "bold")) #using tk.Label rather than ttk.Label as ttk.Label applies a grey background and is awkward with themes applied


    #function to change the value of lblDisplayResult, will be called when a button is clicked
    #if result part protects against errors when no data is returned from relevant calculation function
    def show_result(text, result):
        text = f"{text}: {result}" if result else "No data found"
        lblDisplayResult.config(text=text)
        lblDisplayResult.pack(pady=10, padx=10, anchor="center")


    """
    Creating buttons with lambda functions in the command arg, without these it would run show_result as soon as the button was created, rather than when it was clicked.
    This is because command= wants a function reference (i.e. command=show_result) which says here's the function to use when clicked, not a function call (i.e. command=show_result(x, y)) ...
    ... which says run the function show_result with arguments x and y. Lambda essentially creates a callable function that we can use. This means that tkinter has a function reference, rather than a function call.
    Can think of it like a recipe vs making the finished food. Tkinter wants the recipe for later, so wrapping it in a lambda function gives tkinter a reference to this recipe, rather than ...
    ... telling it to make the food straight away.
    """
    ttk.Button(win_statistics, text="Average Grade", command=lambda: show_result("Average Grade", calculate_average_grade_sql(conn))).pack(padx=10, pady=5)
    ttk.Button(win_statistics, text="Average Attendance", command=lambda: show_result("Average Attendance", calculate_average_attendance_sql(conn))).pack(padx=10, pady=5)
    ttk.Button(win_statistics, text="Number of Passes", command=lambda: show_result("Number of Passes", get_number_of_passes_sql(conn))).pack(padx=10, pady=5)
    ttk.Button(win_statistics, text="Number of Fails", command=lambda: show_result("Number of Fails", get_number_of_fails_sql(conn))).pack(padx=10, pady=5)
    ttk.Button(win_statistics, text="Number of As", command=lambda: show_result("Number of As", get_number_of_As_sql(conn))).pack(padx=10, pady=5)
    ttk.Button(win_statistics, text="Number of Bs", command=lambda: show_result("Number of Bs", get_number_of_Bs_sql(conn))).pack(padx=10, pady=5)
    ttk.Button(win_statistics, text="Number of Cs", command=lambda: show_result("Number of Cs", get_number_of_Cs_sql(conn))).pack(padx=10, pady=5)

    win_statistics.protocol("WM_DELETE_WINDOW", on_close) #WM_DELETE_WINDOW is the event triggered by clicking the close button. When this is triggered, call on_close() allowing cleanup before destroying the window

#for testing
if __name__ == "__main__":
    root = tk.Tk() #create a root window
    root.withdraw() #hide it if you only want the statistics window
    open_statistics_gui()
    root.mainloop()