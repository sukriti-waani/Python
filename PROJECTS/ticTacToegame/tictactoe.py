# Tkinter is Python's standard library for creating Graphical User Interfaces (GUIs).
# It allows us to build windows, buttons, labels, message boxes, etc.

import tkinter as tk  # Import tkinter and give it a short alias 'tk'
from tkinter import messagebox  # Import the messagebox module for pop-up alerts

# Function to check if a player has won the game
def check_winner():
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
            root.quit()  # Close the game window after win

# Function to handle button click event
def button_click(index):
    # If the clicked button is empty and there is no winner yet
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player  # Set current player's symbol (X or O)
        check_winner()  # Check if this move won the game
        toggle_player()  # Switch to the other player

# Function to switch players after each turn
def toggle_player():
    global current_player  # Allow modification of global variable
    # Switch between X and O
    current_player = "X" if current_player == "O" else "O"
    # Update the label to show the next player's turn
    label.config(text=f"Player {current_player}'s turn")
