from tkinter import *

THEME_COLOR = "#375362"

class QuizUI():
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=400, height=600, background=THEME_COLOR)

        self.true_img = PhotoImage(file='true.png')
        self.false_img = PhotoImage(file='false.png')

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.create_text(150, 125, text="Question text", font=("Ariel", 30, "bold"))
        self.score_text = Label(text="Score: 0", fg="white")

        self.score_text.grid(row=0, column=1)
        self.canvas.grid(row=1, column=1, columnspan=2)

        self.window.mainloop()