#This file will be used for common gui functions/helpers that I might want to apply to several gui windows
#This will help with the DRY principle in software development (Don't Repeat Yourself)

from tkinter import messagebox

#Function to centre a tkinter window using the middle as an anchor. Takes the window to centre, and its width and height
def centre_window(window, width, height):
    #get user's screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    #calculate position to use for centering
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    y -= 100 #windows appear visually low so moving up for ease of use

    #use .geometry method to set window position
    window.geometry(f"{width}x{height}+{x}+{y}")

#Function to safely close a tkinter window, handling any errors that might occur
def safe_close_window(win, conn=None, df=None, root=None):
    try:
        if conn: #if a database connection exists, close it
            conn.close()
        if df: #if a dataframe exists, delete it
            del df
        win.destroy()
        if root: #only relevant for the main menu closing, which destroys root and therefore ends the program
            root.destroy()
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")