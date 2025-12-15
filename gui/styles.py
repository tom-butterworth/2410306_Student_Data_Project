from tkinter import ttk
import sv_ttk

def setup_styles(theme="light"):
    sv_ttk.set_theme(theme)
    style = ttk.Style() #needed for if you want to use custom styles. Applies automatically to any TopLevel windows

    # style.configure(
    #     "Treeview",
    #     background="#2b2b2b", #dark grey background
    #     foreground="white", #white text
    #     fieldbackground="#2b2b2b", #for empty space
    #     rowheight=25 #makes rows bigger
    # )
    #
    # style.configure(
    #     "Treeview.Heading",
    #     background="#2b2b2b",
    #     foreground="white",
    #     fieldbackground="#2b2b2b",
    # )


    #Example of how to configure a custom tkinter style
    # style.configure(
    #     "Title.TLabel",
    #     font=("Arial", 12, "bold"),
    #     foreground="blue",
    #     background="F0F0F0",
    # )