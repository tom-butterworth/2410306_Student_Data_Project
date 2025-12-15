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

    #Treeview to display search results
    columns = ("student_id", "first_name", "last_name")
    searchResultTree = ttk.Treeview(win_student_search, columns=columns, show="headings", height=10)
    for col in columns:
        searchResultTree.heading(col, text=col.replace("_", " ").title())
        searchResultTree.column(col, width=150)
    searchResultTree.pack(pady=10)




    full_search_results = []


    #Called when search button is clicked
    def search_student():
        search_value = search_box.get() #gets search box text value entered by the user
        if not search_value:
            return messagebox.showerror("Error", "Please enter a search value") #give an error if no text entered

        #below: gets all rows where first or last name contains user's search value. COLLATE NOCASE in sql means the query ignores case
        try:
            search_results = conn.execute(
                """
                SELECT *
                FROM tbl_student_grades
                WHERE first_name LIKE ? COLLATE NOCASE
                   OR last_name LIKE ? COLLATE NOCASE
                ORDER BY last_name, first_name
                """,
                (f"%{search_value}%", f"%{search_value}%")
            ).fetchall()
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {e}")

        #clear results box and full results array ready to display
        searchResultTree.delete(*searchResultTree.get_children())
        full_search_results.clear()

        #if no results found, display as such in treeview
        if not search_results:
            searchResultTree.insert("", tk.END, values=("No results", "", ""))
            return

        #for every row returned in search_results from sql query, add row to full_search_results and enter it into the treeview
        for row in search_results:
            full_search_results.append(row) #store the full row for if user double clicks on a record
            searchResultTree.insert("", tk.END, values=(row[0], row[1], row[2]))

    def on_result_double_click(event):
        selection = searchResultBox.curselection()
        if selection:
            student = searchResultBox.get(selection[0])
            messagebox.showinfo("Student Selected", f"You chose: {student}")

    searchResultBox.bind("<Double-Button-1>", on_result_double_click)

    #Search button
    search_button = ttk.Button(win_student_search, text="Search", command=search_student)
    search_button.pack()

    win_student_search.protocol("WM_DELETE_WINDOW", lambda: safe_close_window(win_student_search, conn=conn))