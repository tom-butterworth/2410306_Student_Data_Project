from db_conn import get_connection
import tkinter as tk
from tkinter import ttk, messagebox
from gui.gui_helpers import centre_window, safe_close_window


def open_student_search_gui():
    win_student_search = tk.Toplevel()
    win_student_search.title("Student Search")
    centre_window(win_student_search, 500, 450)

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


    #If the user double clicks a record, they can see the student's full details
    def on_result_double_click(event):
        #for the first student the user double clicks, the window expands allowing room for the full results display
        if win_student_search.winfo_height() == 450:
            centre_window(win_student_search, 500, 750)

        selected_record = searchResultTree.selection()
        if selected_record:
            index = searchResultTree.index(selected_record) #gets the index of the record the user clicked on
            full_row = full_search_results[index] #gets the data for the selected record

            #clear previous details
            for widget in full_details_frame.winfo_children():
                widget.destroy()


            details_labels =["student_id", "first_name", "last_name", "age", "email", "country", "attendance", "assignment_completed", "grade"]
            full_details_frame.grid_columnconfigure(1, weight=1)
            for i, label in enumerate(details_labels):
                tk.Label(full_details_frame, text=f"{label}:", font=("Segoe UI", 10, "bold"), anchor="w").grid(row=i, column=0, sticky="w", padx=10, pady=2)
                tk.Label(full_details_frame, text=full_row[i], anchor="w").grid(row=i, column=1, sticky="ew", padx=10, pady=2)


    #When a record in the treeview is double clicked, call on_result_double_click
    searchResultTree.bind("<Double-Button-1>", on_result_double_click)

    #Search button
    search_button = ttk.Button(win_student_search, text="Search", command=search_student)
    search_button.pack()

    #Frame to contain full student details when double clicked
    full_details_frame = tk.Frame(win_student_search)
    full_details_frame.pack(fill="x", expand=True, padx=10)

    #Ensure window closes safely
    win_student_search.protocol("WM_DELETE_WINDOW", lambda: safe_close_window(win_student_search, conn=conn))