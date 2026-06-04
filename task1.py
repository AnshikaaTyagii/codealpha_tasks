import tkinter as tk
from tkinter import messagebox
import random

# Word list
words = ["PYTHON", "COMPUTER", "PROGRAM", "HANGMAN", "STUDENT"]
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("800x600")
root.configure(bg="#f4f4f4")

# Canvas for hangman drawing
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack(pady=20)

# Draw stand
canvas.create_line(50, 280, 250, 280, width=3)
canvas.create_line(100, 280, 100, 50, width=3)
canvas.create_line(100, 50, 200, 50, width=3)
canvas.create_line(200, 50, 200, 80, width=3)

# Word display
word_label = tk.Label(
    root,
    text=" ".join("_" * len(word)),
    font=("Arial", 24, "bold"),
    bg="#f4f4f4"
)
word_label.pack(pady=20)

def draw_hangman(step):
    if step == 1:
        canvas.create_oval(175, 80, 225, 130, width=3)
    elif step == 2:
        canvas.create_line(200, 130, 200, 200, width=3)
    elif step == 3:
        canvas.create_line(200, 150, 170, 180, width=3)
    elif step == 4:
        canvas.create_line(200, 150, 230, 180, width=3)
    elif step == 5:
        canvas.create_line(200, 200, 170, 240, width=3)
    elif step == 6:
        canvas.create_line(200, 200, 230, 240, width=3)

def update_word():
    display = [letter if letter in guessed_letters else "_" for letter in word]
    word_label.config(text=" ".join(display))

    if "_" not in display:
        messagebox.showinfo("Congratulations", "You Won!")
        disable_buttons()

def disable_buttons():
    for btn in buttons:
        btn.config(state=tk.DISABLED)

def guess(letter, button):
    global wrong_guesses

    button.config(state=tk.DISABLED)

    if letter in word:
        guessed_letters.append(letter)
        update_word()
    else:
        wrong_guesses += 1
        draw_hangman(wrong_guesses)

        if wrong_guesses >= max_wrong:
            disable_buttons()
            messagebox.showerror(
                "Game Over",
                f"You Lost!\nThe word was {word}"
            )

# Letter buttons
frame = tk.Frame(root, bg="#f4f4f4")
frame.pack()

buttons = []

for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    btn = tk.Button(
        frame,
        text=letter,
        width=4,
        height=2,
        font=("Arial", 10, "bold")
    )

    btn.config(command=lambda l=letter, b=btn: guess(l, b))
    btn.grid(row=i // 9, column=i % 9, padx=3, pady=3)

    buttons.append(btn)

# Restart game
def restart():
    root.destroy()

restart_btn = tk.Button(
    root,
    text="Exit Game",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    command=restart
)
restart_btn.pack(pady=20)

root.mainloop()