from db_conn import get_connection
import tkinter as tk
from tkinter import ttk, messagebox
from gui.gui_helpers import centre_window, safe_close_window


def open_student_search_gui():
    win_student_search = tk.Toplevel()
    win_student_search.title("Student Search")
    centre_window(win_student_search, 500, 500)

    conn = get_connection()  # connect to db so we can search it

    #Title label
    lblStudentSearchTitle = tk.Label(win_student_search, text="Search Students", font=("Segoe UI", 15, "bold"))
    lblStudentSearchTitle.pack(pady=10)

    #Search box
    search_box = tk.Entry(win_student_search, width=50) #input/search box for user to type in
    search_box.pack(pady=10)
    search_box.focus()
    search_box.bind("<Return>", lambda event: search_student())

    #Listbox to display search results
    searchResultBox = tk.Listbox(win_student_search, width=50, height=10)
    searchResultBox.pack(pady=10)


    #Called when search button is clicked
    def search_student():
        search_value = search_box.get() #gets search box text value entered by the user
        if not search_value:
            return messagebox.showerror("Error", "Please enter a search value") #give an error if no text entered

        #below: gets all rows where first or last name contains user's search value. COLLATE NOCASE in sql means the query ignores case
        search_results = conn.execute(
            """
            SELECT student_id, first_name, last_name
            FROM tbl_student_grades
            WHERE first_name LIKE ? COLLATE NOCASE
               OR last_name LIKE ? COLLATE NOCASE
            ORDER BY last_name, first_name
            """,
            (f"%{search_value}%", f"%{search_value}%")
        ).fetchall()

        searchResultBox.delete(0, tk.END) #clear the listbox ready to insert results
        if not search_results:
            searchResultBox.insert(tk.END, "No results found") #display message in listbox if no results found
        for student_id, first_name, last_name in search_results:
            searchResultBox.insert(tk.END, f"{student_id} - {first_name} {last_name}")

    def on_result_double_click(event):
        selection = searchResultBox.curselection()
        if selection:
            student = searchResultBox.get(selection[0])
            messagebox.showinfo("Student Selected", f"You chose: {student}")

    searchResultBox.bind("<Double-Button-1>", on_result_double_click)

    #Search button
    search_button = ttk.Button(win_student_search, text="Search", command=search_student)
    search_button.pack(pady=10)

    win_student_search.protocol("WM_DELETE_WINDOW", lambda: safe_close_window(win_student_search, conn=conn))