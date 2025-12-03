import tkinter as tk
from tkinter import messagebox
from db_conn import get_connection
from calculations import calculate_average_grade_sql, calculate_average_attendance_sql
from gui_helpers import centre_window

#open and display the window. Everything related to building and using this window needs to be in the function.
#this presents things like database connections happening at import time and also prevents scope errors
def open_statistics_gui():
    win_statistics = tk.Toplevel() #creates new window on top of the current/main one
    win_statistics.title("Statistics")
    centre_window(win_statistics, 400, 300)

    #connect to database
    conn = get_connection()

    #create labels to display results when a button is clicked to do so, not applying .pack method yet so it doesn't show and create empty space before any results are requested/displayed
    lblResultTitle = tk.Label(win_statistics, text="Results:")
    lblDisplayResult = tk.Label(win_statistics, text="")


    #function to change the value of lblDisplayResult, will be called when a button is clicked
    #if result part protects against errors when no data is returned
    def show_result(text, result):
        try:
            lblResultTitle.pack(padx=10, anchor="w")
            lblDisplayResult.config(text=f"{text}: {result:.2f}" if result else "No data found")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")


    """
    Creating buttons with lambda functions in the command arg, without these it would run show_result as soon as the button was created, rather than when it was clicked.
    This is because command= wants a function reference (i.e. command=show_result) which says here's the function to use when clicked, not a function call (i.e. command=show_result(x, y)) ...
    ... which says run the function show_result with arguments x and y. Lambda essentially creates a callable function that we can use. This means that tkinter has a function reference, rather than a function call.
    You can think of it like a recipe vs making the finished food. Tkinter wants the recipe for later, so wrapping it in a lambda function gives tkinter a reference to this recipe, rather than ...
    ... telling it to make the food straight away.
    """
    tk.Button(win_statistics, text="Average Grade", command=lambda: show_result("Average Grade", calculate_average_grade_sql(conn))).pack( padx=10, pady=5, anchor="w")
    tk.Button(win_statistics, text="Average Attendance", command=lambda: show_result("Average Attendance", calculate_average_attendance_sql(conn))).pack(padx=10, pady=5, anchor="w")

    #function to be called when the window is closed, handles closing db connection and destroying the window
    def on_close():
        try:
            conn.close() #close db connection before closing/destroying window
            win_statistics.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    win_statistics.protocol("WM_DELETE_WINDOW", on_close) #WM_DELETE_WINDOW is the event triggered by clicking the close button. When this is triggered, call on_close() allowing cleanup before destroying the window