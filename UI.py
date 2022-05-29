import tkinter as tk
from wordlist import words
from random import choice

# Constants
BACKGROUND_COLOR = "#B1DDC6"


# Functions
def random_pair():
    return choice(words)


def update_flashcard():
    global current_pair
    current_pair = random_pair()
    canvas_flashcard.itemconfig(word_text, text=current_pair[0])


# Main window
window_main = tk.Tk()
window_main.title("Flashcards")
window_main.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Image setup
image_card_f = tk.PhotoImage(file="images/card_front.png")
image_card_b = tk.PhotoImage(file="images/card_back.png")
image_button_y = tk.PhotoImage(file="images/right.png")
image_button_n = tk.PhotoImage(file="images/wrong.png")

# Canvas for the flashcard
current_pair = random_pair()
canvas_flashcard = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_flashcard.create_image(400, 263, image=image_card_f)
language_text = canvas_flashcard.create_text(400, 150, font=("Arial", 40, "italic"), text="French")
word_text = canvas_flashcard.create_text(400, 263, font=("Arial", 60, "bold"), text=current_pair[0])
canvas_flashcard.grid(column=0, row=0, columnspan=2)

# Buttons
button_y = tk.Button(image=image_button_y, bd=0, highlightthickness=0, relief="flat", command=update_flashcard)
button_y.grid(column=1, row=1)

button_n = tk.Button(image=image_button_n, bd=0, highlightthickness=0, relief="flat", command=update_flashcard)
button_n.grid(column=0, row=1)

window_main.mainloop()
