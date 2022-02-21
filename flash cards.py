from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data_csv = pandas.read_csv("data/french_words.csv")

curr_card = {"English" : "English"}
try:
    data_csv = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data_csv = pandas.read_csv("data/french_words.csv")
finally:
    data = data_csv.to_dict(orient="records")


def new_word():
    global curr_card, flip_timer
    window.after_cancel(flip_timer)
    curr_card = random.choice(data)
    canvas.itemconfig(word, text=curr_card["French"], fill="black")
    canvas.itemconfig(french, text="French", fill="black")
    canvas.itemconfig(card_face, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_face, image=card_back_img)
    canvas.itemconfig(french, text="English", fill="white")
    canvas.itemconfig(word, text=curr_card["English"], fill="white")

def remember():
    global curr_card
    data.remove(curr_card)
    new_data_csv = pandas.DataFrame.from_records(data)
    new_data_csv.to_csv("words_to_learn.csv", index=False)




window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_face = canvas.create_image(400, 263, image=card_front_img)
french = canvas.create_text(400, 150, text="french", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

x_img = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_img, highlightthickness=0, command=new_word)
x_button.grid(row=1, column=0)
y_img = PhotoImage(file="images/right.png")
y_button = Button(image=y_img, highlightthickness=0, command=lambda:[new_word(), remember()])
y_button.grid(row=1,column=1)
window.mainloop()