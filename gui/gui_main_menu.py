import tkinter as tk #used to create gui
from gui.gui_helpers import centre_window
from gui.gui_statistics import open_statistics_gui
from tkinter import ttk #use for widgets if possible, modern widgets have more formatting and features than older tk widgets
from sv_ttk import get_theme, set_theme  # will be used to set a gui theme (windows 11 like theme with light and dark variants)


def open_main_menu():
    #set up a tkinter window
    #from research, it's convention to use root as the name of the window/root for a tkinter gui, so I'll use that for my main menu
    root = tk.Tk()
    root.title("Student Data")
    centre_window(root, 600, 150) #call function to centre window
    ttk.Label(root, text="SID - Student Information Data", font=("Arial", 15, "bold")).grid(row=0, column=0, columnspan=3, pady=20) #columnspan and rowspan used to make content span multiple cells of a grid



    def open_graphs_gui():
        pass

    def open_student_search_gui():
        pass


    ttk.Button(root, text="Display Statistics", command=open_statistics_gui).grid(row=1, column=0, padx=10, pady=15)
    ttk.Button(root, text="Display Graphs", command=open_graphs_gui).grid(row=1, column=1, padx=10, pady=15)
    ttk.Button(root, text="Search Students", command=open_student_search_gui).grid(row=1, column=2, padx=10, pady=15)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)


    set_theme("light") #sets sun valley light theme
    root.mainloop()