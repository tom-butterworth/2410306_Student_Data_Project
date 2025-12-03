import tkinter as tk
from tkinter import messagebox
from db_conn import get_connection
from calculations import calculate_average_grade_sql, calculate_average_attendance_sql

conn = get_connection()

win_statistics = tk.Tk()

#create labels to display results when a button is clicked to do so, not .pack yet so it doesn't show and create empty space
lblResultTitle = tk.Label(win_statistics, text="Results:")
lblDisplayResult = tk.Label(win_statistics, text="")


#function to change the value of lblDisplayResult, will be called when a button is clicked
#if result part protects against errors when no data is returned
def show_result(text, result):
    try:
        lblResultTitle.pack(padx=10, anchor="w")
        lblDisplayResult.config(text=f"{text}: {result:.2f}" if result else "No data found")
        lblDisplayResult.pack(padx=10, anchor="w")
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
