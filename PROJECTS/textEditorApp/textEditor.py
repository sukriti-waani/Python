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
# ---------------- File Menu Commands ----------------
file_menu.add_command(label="New", command=new_file)      # Add "New" option to File menu → runs new_file()
file_menu.add_command(label="Open", command=open_file)    # Add "Open" option → runs open_file()
file_menu.add_command(label="Save", command=save_file)    # Add "Save" option → runs save_file()
file_menu.add_separator()                                 # Add a horizontal separator line in File menu
file_menu.add_command(label="Exit", command=root.quit)    # Add "Exit" option → closes the application

# ---------------- Text Area Setup ----------------
# Create a text widget for writing text
# wrap=tk.WORD → breaks lines at word boundaries instead of cutting words in half
# font=("Helvetica", 12) → sets the font style to Helvetica, size 12
# fg="blue" → sets text color to blue
text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="blue")

# Place the text widget inside the main window
# expand=tk.YES → allows the text area to grow when window is resized
# fill=tk.BOTH → fill available space both horizontally and vertically
text.pack(expand=tk.YES, fill=tk.BOTH)

# ---------------- Run the Application ----------------
root.mainloop()   # Starts the Tkinter event loop → keeps window open and responsive
