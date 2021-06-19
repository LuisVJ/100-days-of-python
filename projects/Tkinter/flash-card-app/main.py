import tkinter as tk
import csv

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"



# ************ Layout **********

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = tk.PhotoImage(file="./images/card_front.png")
card_back_img = tk.PhotoImage(file="./images/card_back.png")
right_img = tk.PhotoImage(file="./images/right.png")
wrong_img = tk.PhotoImage(file="./images/wrong.png")

canvas = tk.Canvas(width=800, height=565, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 280, image=card_front_img)
canvas.create_text(400, 135, text="French", font=(FONT_NAME, 30, "italic"))
canvas.create_text(400, 270, text="French", font=(FONT_NAME, 50, "bold"))

wrong_button = tk.Button(image=wrong_img, highlightthickness=0)
right_button = tk.Button(image=right_img, highlightthickness=0)

# ************ Positioning **********

canvas.grid(column=0, row=0, columnspan=2)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)





window.mainloop()