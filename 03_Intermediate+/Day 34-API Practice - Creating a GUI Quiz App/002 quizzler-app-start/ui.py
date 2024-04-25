from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background='white')
        self.question = self.canvas.create_text(150, 125, width=280,text="What is your favorite",
                                                fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=50, pady=50)

        correct = PhotoImage(file="images/true.png")
        self.right_btn = Button(image=correct, highlightthickness=0, command=self.true_btn)
        self.right_btn.grid(row=2, column=0, padx=20, pady=20)

        incorrect = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=incorrect, highlightthickness=0, command=self.false_btn)
        self.wrong_btn.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of of the quiz")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")


    def false_btn(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def true_btn(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)


