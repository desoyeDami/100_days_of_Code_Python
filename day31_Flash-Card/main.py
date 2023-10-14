from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
index_choice = {}
to_learn = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')



def next_card():
    global index_choice, flip_timer
    window.after_cancel(flip_timer)
    index_choice = random.choice(to_learn)
    canvas.itemconfig(canvas_img, image=card_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=index_choice["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=index_choice["English"], fill="white")


def is_known():
    to_learn.remove(index_choice)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ------------------------- UI ---------------------------
window = Tk()
window.title("Flashy Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

#Canvas Image & text
canvas = Canvas(width=800, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 265, image=card_front)
language = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


next_card()

#Image Button
right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, fg=BACKGROUND_COLOR, command=is_known)
right_btn.grid(row=1, column=1)
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, fg=BACKGROUND_COLOR, command=next_card)
wrong_btn.grid(row=1, column=0)


window.mainloop()
