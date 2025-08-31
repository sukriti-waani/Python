# Tkinter is Python's standard library for creating Graphical User Interfaces (GUIs).
# It allows us to build windows, buttons, labels, message boxes, etc.

import tkinter as tk  # Import tkinter and give it a short alias 'tk'
from tkinter import messagebox  # Import the messagebox module for pop-up alerts

# Function to check if a player has won the game
def check_winner():
    global winner  # mark that this can change winner
    # Define all possible winning combinations: 3 rows, 3 columns, 2 diagonals
    for combo in [[0,1,2], [3,4,5], [6,7,8],   # rows
                  [0,3,6], [1,4,7], [2,5,8],   # columns
                  [0,4,8], [2,4,6]]:           # diagonals
        
        # Check if all three buttons in this combo have the same symbol (X or O) and not empty
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != ""):
            
            # Highlight the winning buttons in green
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            
            # Show a popup message announcing the winner
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            root.quit()  # Close the game window after win

# Function to handle button click event
def button_click(index):
    global winner, current_player  # allow changes to these globals
    # If the clicked button is empty and there is no winner yet
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player  # Set current player's symbol (X or O)
        check_winner()  # Check if this move won the game
        if not winner:
            toggle_player()  # Switch to the other player

# Function to switch players after each turn
def toggle_player():
    global current_player  # Allow modification of global variable
    # Switch between X and O
    current_player = "X" if current_player == "O" else "O"
    # Update the label to show the next player's turn
    label.config(text=f"Player {current_player}'s turn")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create 9 buttons for the board using a list comprehension
# Here, we are creating 9 buttons (for the 3x3 Tic-Tac-Toe board).
# - tk.Button(...) creates a button with:
#     text="" → button starts empty (no X or O)
#     font=("normal", 25) → makes text large for visibility
#     width=6, height=2 → sets button size
#     command=lambda i=i: button_click(i) → when clicked, it calls button_click() with that button's index
buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

# Place buttons in a 3x3 grid
# - enumerate(buttons) gives (index, button)
# - button.grid(...) places each button in a specific row & column of the GUI
# - Row number = i // 3 → integer division groups into 3 rows
# - Column number = i % 3 → remainder gives column (0,1,2)
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

# Initialize game state
# - current_player → starts as "X" (first player)
# - winner → False means no winner at beginning
current_player = "X"
winner = False

# Create a label to show which player's turn it is
# - tk.Label(...) creates a text label
# - Shows "Player X's turn" initially
# - font=("normal", 16) sets readable text size
# - .grid(row=3, column=0, columnspan=3) → places label below buttons, spanning all 3 columns
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# Run the GUI loop
# - root.mainloop() keeps the window open
# - Listens for user interactions (button clicks)
root.mainloop()
