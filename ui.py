import tkinter
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}/{self.quiz.question_number}", font=20, fg="white", bg=THEME_COLOR, padx=20, pady=20)
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")

        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question Text",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_click)
        self.true_button.grid(column=0, row=2)
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_click)
        self.false_button.grid(column=1, row=2)

        self.get_next_ques()
        self.window.mainloop()

    def get_next_ques(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            next_ques = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=next_ques)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the Quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_click(self):
        is_right = self.quiz.check_answer("true")
        self.feedback(is_right)

    def false_click(self):
        is_right = self.quiz.check_answer("false")
        self.feedback(is_right)

    def feedback(self, is_right):

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_ques)




