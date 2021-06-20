import tkinter as tk
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
FLIP_TIME = 3000

try:
    words_df = pd.read_csv("./data/words_to_learn.csv")
except:
    words_df = pd.read_csv("./data/french_words.csv")

FRONT_LANGUAGE = words_df.columns[0]
BACK_LANGUAGE = words_df.columns[1]

# *********** Card management *******

def new_card():
    new_word = words_df.sample()
    new_word_front = new_word[FRONT_LANGUAGE].values[0]
    new_word_back = new_word[BACK_LANGUAGE].values[0]

    canvas.itemconfig(canvas_card, image=card_front_img)
    canvas.itemconfig(canvas_language, text=FRONT_LANGUAGE, fill="black") 
    canvas.itemconfig(canvas_word, text=new_word_front, fill="black")

    # "Deactivate" Buttons
    right_button["command"] = ""
    wrong_button["command"] = ""

    window.after(FLIP_TIME, flip_card, new_word_back)

def flip_card(word_back):
    canvas.itemconfig(canvas_card, image=card_back_img)
    canvas.itemconfig(canvas_language, text=BACK_LANGUAGE, fill="white")
    canvas.itemconfig(canvas_word, text=word_back, fill="white")

    # "activate" Buttons
    right_button["command"] = remove_word
    wrong_button["command"] = new_card

# ************ Remove learned word *************
def remove_word():
    word_back = canvas.itemcget(canvas_word, "text")
    words_df.drop(
        words_df.loc[words_df[BACK_LANGUAGE] == word_back].index, inplace=True
    )
    words_df.to_csv("./data/words_to_learn.csv", index=False)

    new_card()

# ************ Layout *************

window = tk.Tk()
window.title("Flashy")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

# Images for the interface
card_front_img = tk.PhotoImage(file="./images/card_front.png")
card_back_img = tk.PhotoImage(file="./images/card_back.png")
right_img = tk.PhotoImage(file="./images/right.png")
wrong_img = tk.PhotoImage(file="./images/wrong.png")

# Canvas properties
canvas = tk.Canvas(
    width=800, height=565, bg=BACKGROUND_COLOR, highlightthickness=0
)
canvas_card = canvas.create_image(400, 280, image=card_front_img)
canvas_language = canvas.create_text(
    400, 150, text="", font=(FONT_NAME, 30, "italic")
)
canvas_word = canvas.create_text(
    400, 300, text="", font=(FONT_NAME, 50, "bold")
)

# Control buttons
wrong_button = tk.Button(
    image=wrong_img, highlightthickness=0, bd=0, command=new_card
)
right_button = tk.Button(
    image=right_img, highlightthickness=0, bd=0, command=remove_word
)

# ************ Positioning **********

canvas.grid(column=0, row=0, columnspan=2)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)


# Generate first word
new_card() 

window.mainloop()