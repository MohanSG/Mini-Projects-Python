import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT=("Ariel", 45, "italic")
WORD_FONT=("Ariel", 40, "bold")


def get_words():
    try:
        with open("data/words_to_learn.csv", "r", encoding="utf-8") as file:
            data=pandas.read_csv(file)
            data_dict = data.to_dict(orient="records")
            print("Using words to learn")
            return data_dict
    except FileNotFoundError:
        with open("data/chinese_words.csv", "r", encoding="utf-8") as file:
            data = pandas.read_csv(file)
            data_dict = data.to_dict(orient="records")
            print("Using chinese words")
            return data_dict


def get_new_card():
    global random_word
    random_word = random.choice(list(words_dict))
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(language_text, text="Chinese")
    canvas.itemconfig(word_text, text=random_word["Chinese"])
    count_down()


def show_answer():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=random_word["English"])


def word_learned():
    global timer_id
    window.after_cancel(timer_id)
    update_learned_words(random_word)
    get_new_card()

def word_dont_know():
    global timer_id
    window.after_cancel(timer_id)
    get_new_card()

def update_learned_words(word):
        for i in range(len(words_dict)):
            if words_dict[i]["Chinese"] == word["Chinese"]:
                words_dict.remove(words_dict[i])
                print(words_dict)
                break

        with open("data/words_to_learn.csv", "w", encoding="utf-8") as file:
            df = pandas.DataFrame(words_to_learn)
            df.to_csv(file, index=False, lineterminator='\n')

def count_down():
    global timer_id
    timer_id = window.after(3000, show_answer)

random_word = ''
words_dict = get_words()
words_to_learn = words_dict
timer_id = ''

window = Tk()
window.title("Chinese Flashcard Review")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.minsize(width=900, height=700)

wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height= 526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=front_img)
language_text = canvas.create_text(400, 150, text="Chinese", fill="black", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="Ni hao", fill="black", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=wrong_img, command=get_new_card, borderwidth=0, highlightthickness=0)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_img, command=word_learned, borderwidth=0, highlightthickness=0)
right_button.grid(column=1, row=1)

get_new_card()

window.mainloop()