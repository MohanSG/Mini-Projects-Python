from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=400, height=600, background=THEME_COLOR, padx=20, pady=20)

        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Question text", font=("Ariel", 20, "bold"), width=290)
        self.score_text = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 9, "normal"))

        self.true_button = Button(image=true_img, command=self.pressed_true)
        self.false_button = Button(image=false_img, command=self.pressed_false)

        self.score_text.grid(row=0, column=1, padx=20, pady=20)
        self.score_text.grid(row=0, column=2, padx=20, pady=20)
        self.canvas.grid(row=1, column=1, columnspan=2, padx=20, pady=20)
        self.true_button.grid(row=2, column=1, padx=20, pady=20)
        self.false_button.grid(row=2, column=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        next_question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=next_question)

    def pressed_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def pressed_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.window.after(1000, self.flash_screen, "green")
        else:
            self.window.after(1000, self.flash_screen, "red")

    def flash_screen(self, color):
        self.canvas["background"] = color