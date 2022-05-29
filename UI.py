import tkinter as tk
from wordlist import words, save
from random import choice

# Constants
BACKGROUND_COLOR = "#B1DDC6"
current_pair = {}
timer = None


# Functions
def update_flashcard():
    global current_pair, timer
    if timer:
        window_main.after_cancel(timer)
    current_pair = choice(words)
    canvas_flashcard.itemconfig(card_image, image=image_card_f)
    canvas_flashcard.itemconfig(language_text, text="French", fill="black")
    canvas_flashcard.itemconfig(word_text, text=current_pair["French"], fill="black")
    timer = window_main.after(3000, reverse_flashcard)


def reverse_flashcard():
    global current_pair
    canvas_flashcard.itemconfig(card_image, image=image_card_b)
    canvas_flashcard.itemconfig(language_text, text="English", fill="white")
    canvas_flashcard.itemconfig(word_text, text=current_pair["English"], fill="white")


def learn_flashcard():
    global words, current_pair
    words.remove(current_pair)
    update_flashcard()


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
canvas_flashcard = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas_flashcard.create_image(400, 263)
language_text = canvas_flashcard.create_text(400, 150, font=("Arial", 40, "italic"))
word_text = canvas_flashcard.create_text(400, 263, font=("Arial", 60, "bold"))
canvas_flashcard.grid(column=0, row=0, columnspan=2)
update_flashcard()

# Buttons
button_y = tk.Button(image=image_button_y, bd=0, highlightthickness=0, relief="flat", command=learn_flashcard)
button_y.grid(column=1, row=1)

button_n = tk.Button(image=image_button_n, bd=0, highlightthickness=0, relief="flat", command=update_flashcard)
button_n.grid(column=0, row=1)

window_main.mainloop()
save()
