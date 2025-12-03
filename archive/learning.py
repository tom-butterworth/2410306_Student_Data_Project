import tkinter as tk #package I will use for gui
from calculations import * #import all functions from calculations.py for us to use and display later
from db_conn import get_connection #needed for calling sql calculation functions

conn = get_connection() #in this module, I keep a connection open for the duration of the gui, meaning I don't need to worry about with blocks etc.

#Set up a window
root = tk.Tk()
root.title("Learning")
root.geometry("500x400")

#Title label
lblTitle = tk.Label(root, text='Welcome to my app').pack(pady=10)

#initialise a label to display calculation results
lblDisplayValue = tk.Label(root, text="")
lblDisplayValue.pack()

#function to change the value of lblDisplayValue, will be called when a button is clicked
def show_result(text, result):
    text = f"{text}: {result}" if result else "No data found"
    lblDisplayValue.config(text=text)


"""
Creating buttons with lambda functions in the command arg, without these it would run show_result as soon as the button was created, rather than when it was clicked.
This is because command= wants a function reference (i.e. command=show_result) which says here's the function to use when clicked, not a function call (i.e. command=show_result(x, y)) ...
... which says run the function show_result with arguments x and y. Lambda essentially creates a callable function that we can use. This means that tkinter has a function reference, rather than a function call.
You can think of it like a recipe vs making the finished food. Tkinter wants the recipe for later, so wrapping it in a lambda function gives tkinter a reference to this recipe, rather than ...
... telling it to make the food straight away.
"""
tk.Button(root, text="Average Grade", command=lambda: show_result("Average Grade", calculate_average_grade_sql(conn))).pack( padx=10, pady=5, anchor="w")
tk.Button(root, text="Average Attendance", command=lambda: show_result("Average Attendance", calculate_average_attendance_sql(conn))).pack(padx=10, pady=5, anchor="w")

# def show_average_grade_on_click():
#     newLabel = tk.Label(root, text=f"Average grade: {calculate_average_grade_sql(conn)}")
#     newLabel.pack()


# def show_avg():
#     try:
#         result = calculate_average_grade_sql(conn)
#         text = f"Average grade: {result}" if result else "No data"
#     except Exception as e:
#         print(f"Error: {e}")


# with get_connection() as conn:
#     averageGrade = tk.Button(root, text="Average grade", command = show_avg)
#     averageGrade.pack()


root.mainloop() #always needed for the running of a tkinter gui
conn.close() #close database connection