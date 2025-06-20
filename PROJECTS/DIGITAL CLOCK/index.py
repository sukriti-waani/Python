# Importing the tkinter module and giving it the alias 'tk'.
# 'tkinter' is used to create GUI (Graphical User Interface) applications.
import tkinter as tk  

# Importing the 'strftime' function from the 'time' module.
# 'strftime' formats time as a string based on the specified format codes.
from time import strftime  

# Creating the main window of the GUI application.
# 'Tk()' creates a root window where all widgets will be placed.
root = tk.Tk()  

# Setting the title (text in the window's title bar) of the main window to "Digital Clock".
root.title("Digital Clock")  

# Defining a function named 'time' that updates the clock display.
def time():  
    # 'strftime' formats current time into a string.
    # "%H" - hour (24-hour format), "%M" - minute, "%S" - second.
    # "%p" - AM/PM marker.
    # "\n" - newline character, so date appears below the time.
    # "%D" - date in MM/DD/YY format.
    string = strftime("%H:%M:%S %p \n %D")  
    
    # 'config' is a method that updates widget options.
    # Here, it updates the 'text' property of the label to show the current time string.
    label.config(text=string)  
    
    # 'after' is a method that schedules the 'time' function to be called again after 1000 milliseconds (1 second).
    # This keeps the clock updating every second.
    label.after(1000, time)  

# Creating a Label widget inside 'root'.
# 'tk.Label' creates a text display area in the window.
# 'font' sets the font type ('Calibri'), size (50), and style ('bold').
# 'background' sets the background color of the label (pink).
# 'foreground' sets the text color (brown).
label = tk.Label(root, font=('Calibri', 50, 'bold'), background='pink', foreground='brown')  

# Packing the label into the window.
# 'pack' automatically places the widget.
# 'anchor="center"' centers the label in the window.
label.pack(anchor='center')  

# Calling the 'time' function for the first time to start the clock update loop.
time()  

# 'mainloop' starts the GUI event loop.
# This keeps the window open and responsive to events (like updates or user actions).
root.mainloop()  
