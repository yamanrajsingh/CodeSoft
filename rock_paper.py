import tkinter as tk
import random
from tkinter import messagebox

# Function to determine the winner of the game
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return " Congratulations You win!"
    else:
        return "Computer wins!"
    
# Function to handle button clicks
def play(choice):
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer choose {computer_choice} \n {result}")
     # Update the scoreboard
    if result == " Congratulations You win!":
        player_score_var.set(player_score_var.get() + 1)
    elif result == "Computer wins!":
        computer_score_var.set(computer_score_var.get() + 1)
    else:
        tie_score_var.set(tie_score_var.get() + 1)

def quit_game():
    player_score = player_score_var.get()
    computer_score = computer_score_var.get()
    if player_score > computer_score:
        winner = "Player"
    elif player_score < computer_score:
        winner = "Computer"
    else:
        winner = "It's a tie!"

    messagebox.showinfo("Game Over", f"The winner is: {winner}")
    root.destroy()
    
def reset_scores():
    player_score_var.set(0)
    computer_score_var.set(0)
    tie_score_var.set(0)

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

background_image = tk.PhotoImage(file="logopunch.png")

# Create a label with the background image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Make the label cover the entire window

# Customize button size, color, and background
button_style = {"font": ("Helvetica", 14), "width": 10, "height": 2}
button_colors = {"rock": "orange", "paper": "green", "scissors": "blue"}

# Create a frame for buttons and result label
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=20)

# Create a scoreboard
score_frame = tk.Frame(root)
score_frame.pack(side=tk.TOP, pady=10)

player_score_var = tk.IntVar()
computer_score_var = tk.IntVar()
tie_score_var = tk.IntVar()

player_score_var.set(0)
computer_score_var.set(0)
tie_score_var.set(0)

player_score_label = tk.Label(score_frame, text="Player: ", font=("Helvetica", 22))
player_score_label.grid(row=0, column=0, padx=10)
player_score_display = tk.Label(score_frame, textvariable=player_score_var, font=("Helvetica", 22))
player_score_display.grid(row=0, column=1, padx=10)

computer_score_label = tk.Label(score_frame, text="Computer: ", font=("Helvetica", 22))
computer_score_label.grid(row=0, column=2, padx=10)
computer_score_display = tk.Label(score_frame, textvariable=computer_score_var, font=("Helvetica", 22))
computer_score_display.grid(row=0, column=3, padx=10)

tie_score_label = tk.Label(score_frame, text="Ties: ", font=("Helvetica", 22))
tie_score_label.grid(row=0, column=4, padx=10)
tie_score_display = tk.Label(score_frame, textvariable=tie_score_var, font=("Helvetica", 22))
tie_score_display.grid(row=0, column=5, padx=10)


# Create the result label
result_label = tk.Label(root, text="", font=("TimesRoman", 36))
result_label.pack(side=tk.TOP, pady=40)
result_label.configure( fg="green")  # Set background and text color

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play("rock"), **button_style, bg=button_colors["rock"], fg="white")
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play("paper"), **button_style, bg=button_colors["paper"], fg="white")
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play("scissors"), **button_style, bg=button_colors["scissors"], fg="white")
scissors_button.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(button_frame, text="Reset Scores", command=reset_scores, **button_style, bg="navy", fg="white")
reset_button.pack(side=tk.RIGHT, padx=10)

quit_button = tk.Button(button_frame, text="Quit", command=quit_game, **button_style, bg="red", fg="white")
quit_button.pack(side=tk.RIGHT, padx=10)


root.mainloop()