import tkinter as tk
from tkinter import messagebox
import random

# Functionality
def check_guess():
    try:
        user_guess = int(entry_guess.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    if user_guess < number_to_guess:
        lbl_feedback.config(text="Too Low! Try Again.")
    elif user_guess > number_to_guess:
        lbl_feedback.config(text="Too High! Try Again.")
    else:
        lbl_feedback.config(text=f"Correct! You guessed it in {attempts[0]} attempts.")
        btn_check.config(state="disabled")
        btn_reset.config(state="normal")
        return

    attempts[0] += 1
    lbl_attempts.config(text=f"Attempts: {attempts[0]}")

def reset_game():
    global number_to_guess
    number_to_guess = random.randint(1, 100)
    lbl_feedback.config(text="Guess a number between 1 and 100.")
    lbl_attempts.config(text="Attempts: 0")
    entry_guess.delete(0, tk.END)
    btn_check.config(state="normal")
    btn_reset.config(state="disabled")
    attempts[0] = 0

# Initial Setup
root = tk.Tk()
root.title("Number Guessing Game")

number_to_guess = random.randint(1, 100)
attempts = [0]  # To keep track of the number of attempts

# GUI Elements
lbl_title = tk.Label(root, text="Number Guessing Game", font=("Arial", 14))
lbl_title.pack(pady=10)

lbl_instruction = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 10))
lbl_instruction.pack(pady=5)

entry_guess = tk.Entry(root, font=("Arial", 10), justify="center")
entry_guess.pack(pady=5)

btn_check = tk.Button(root, text="Check Guess", font=("Arial", 10), command=check_guess)
btn_check.pack(pady=5)

lbl_feedback = tk.Label(root, text="Guess a number between 1 and 100.", font=("Arial", 10))
lbl_feedback.pack(pady=10)

lbl_attempts = tk.Label(root, text="Attempts: 0", font=("Arial", 10))
lbl_attempts.pack(pady=5)

btn_reset = tk.Button(root, text="Reset Game", font=("Arial", 10), command=reset_game, state="disabled")
btn_reset.pack(pady=10)

# Run the Application
root.mainloop()