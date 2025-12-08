import tkinter as tk #used to create gui
from gui.gui_helpers import centre_window, safe_close_window
from gui.gui_statistics import open_statistics_gui
from tkinter import ttk #use for widgets if possible, modern widgets have more formatting and features than older tk widgets
from sv_ttk import get_theme, set_theme  # will be used to set a gui theme (windows 11 like theme with light and dark variants)


def open_main_menu(root):
    win_main_menu = tk.Toplevel(root) #creates a toplevel window on top of the current window, attached to the root window from main.py
    win_main_menu.title("Main Menu")
    centre_window(win_main_menu, 600, 150) #call function to centre the window
    #below: columnspan and rowspan used to make content span multiple cells of a grid. tk.Label rather than ttk.Label as ttk.Label applies a grey background and is awkward with themes applied
    tk.Label(win_main_menu, text="SID - Student Information Data", font=("Arial", 15, "bold")).grid(row=0, column=0, columnspan=3, pady=20)



    def open_graphs_gui():
        pass

    def open_student_search_gui():
        pass


    ttk.Button(win_main_menu, text="Display Statistics", command=open_statistics_gui).grid(row=1, column=0, padx=10, pady=15)
    ttk.Button(win_main_menu, text="Display Graphs", command=open_graphs_gui).grid(row=1, column=1, padx=10, pady=15)
    ttk.Button(win_main_menu, text="Search Students", command=open_student_search_gui).grid(row=1, column=2, padx=10, pady=15)

    win_main_menu.grid_columnconfigure(0, weight=1)
    win_main_menu.grid_columnconfigure(1, weight=1)
    win_main_menu.grid_columnconfigure(2, weight=1)


    set_theme("light") #sets sun valley light theme
    root.mainloop()