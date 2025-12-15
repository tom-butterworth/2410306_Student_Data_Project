import tkinter as tk
from gui.gui_helpers import safe_close_window, centre_window
from tkinter import ttk
from gui.plots import plot_grade_vs_attendance, plot_average_grade_by_country, plot_boxplot_grades_by_country, plot_histogram_grade_distribution
from load_data import load_csv

#Get a dataframe from the csv file for us to use when calling plot functions
df = load_csv()


#open and display the window. Everything related to building and using this window needs to be in the function.
def open_graphs_gui():
    win_graphs = tk.Toplevel() #create a toplevel window
    win_graphs.title("Graphs")
    centre_window(win_graphs, 600, 400)

    #without lambda functions, graphs would show instantly when win_graphs opens, even if the user hasn't clicked a button yet
    ttk.Button(win_graphs, text="Grade vs Attendance", command=lambda: plot_grade_vs_attendance(df)).grid(row=0, column=0, padx=10, pady=10)
    ttk.Button(win_graphs, text="Average grade by country", command=lambda: plot_average_grade_by_country(df)).grid(row=1, column=0, padx=10, pady=10)
    ttk.Button(win_graphs, text="Boxplot - Average grade by country", command=lambda: plot_boxplot_grades_by_country(df)).grid(row=2, column=0, padx=10, pady=10)
    ttk.Button(win_graphs, text="Histogram - Grade distribution", command=lambda: plot_histogram_grade_distribution(df)).grid(row=3, column=0, padx=10, pady=10)



    win_graphs.protocol("WM_DELETE_WINDOW", lambda: safe_close_window(win_graphs))