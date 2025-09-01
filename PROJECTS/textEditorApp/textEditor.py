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

def save_file():
    # Ask user where to save the file (default .txt)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files",".txt")])
    if file_path:  
        # Open file in write mode and save content of text widget
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))  
            # Show confirmation after saving
            messagebox.showinfo("Info", "File saves successfully!")

root = tk.Tk()                     # Create main application window
root.title("Simple Text Editor")   # Set window title
root.geometry("800x600")           # Set default size of the window

menu = tk.Menu(root)               # Create a menu bar
root.config(menu = menu)           # Attach menu bar to window
file_menu = tk.Menu(menu)          # Create a "File" menu
menu.add_cascade(label = "File", menu = file_menu)  # Add "File" menu to menu bar
