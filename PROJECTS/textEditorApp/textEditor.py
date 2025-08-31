import tkinter as tk                   # Import tkinter library and give it a short alias 'tk'
from tkinter import filedialog, messagebox  # Import specific modules for file dialogs & message boxes

# Function to create a new blank file (clear text area)
def new_file():
    text.delete(1.0, tk.END)           # Delete text from line 1, character 0 to the end of the text box

# Function to open an existing text file
def open_file():
    # Open a file dialog so the user can pick a text file
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",       # Default file extension is .txt
        filetypes=[("Text Files", "*.txt")]  # Allow only .txt files
    )
    
    if file_path:                       # Check if user actually selected a file (not cancelled)
        with open(file_path, 'r') as file:  # Open the selected file in read mode
            text.delete(1.0, tk.END)    # Clear existing content from text widget
            text.insert(tk.END, file.read())  # Insert file content into text widget
