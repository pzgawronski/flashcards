import tkinter as tk
from wordlist import words

# Constants
BACKGROUND_COLOR = "#B1DDC6"

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
canvas_flashcard.create_image(400, 263, image=image_card_f)
canvas_flashcard.create_text(400, 150, font=("Arial", 40, "italic"), text="French")
canvas_flashcard.create_text(400, 263, font=("Arial", 60, "bold"), text=words[0][0])
canvas_flashcard.grid(column=0, row=0, columnspan=2)

# Buttons
button_y = tk.Button(image=image_button_y, bd=0, highlightthickness=0, relief="flat")
button_y.grid(column=1, row=1)

button_n = tk.Button(image=image_button_n, bd=0, highlightthickness=0, relief="flat")
button_n.grid(column=0, row=1)


window_main.mainloop()
