from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

def pick_word():
    global timer, current_card
    window.after_cancel(timer)
    current_card = random.choice(data_dict)
    fr_word = current_card["French"]
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=fr_word, fill="black")
    timer = window.after(3000, pick_en_word)

def know_word():
    data_dict.remove(current_card)
    dataf = pandas.DataFrame(data_dict)
    dataf.to_csv("data/words_to_learn.csv", index=False)
    pick_word()

def pick_en_word():
    en_word = current_card["English"]
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(lang_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=en_word, fill="white")

window = Tk()
window.title("Flashy Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, pick_en_word)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
lang_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=pick_word)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=know_word)
right_button.grid(column=1, row=1)

pick_word()



window.mainloop()