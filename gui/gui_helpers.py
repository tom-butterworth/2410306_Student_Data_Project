#This file will be used for common gui functions/helpers that I might want to apply to several gui windows

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