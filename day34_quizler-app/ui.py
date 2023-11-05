from tkinter import  *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.score_board = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_board.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Some Questions",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"),
                                                     width=280
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, bg=THEME_COLOR, highlightthickness=0, command=self.true_btn_clicked)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, command=self.false_btn_clicked)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_board.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz\n"
                                                            f"Your final score was: "
                                                            f"{self.quiz.score}/{self.quiz.question_number}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
    def true_btn_clicked(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_btn_clicked(self):
        is_wrong = self.quiz.check_answer("false")
        self.give_feedback(is_wrong)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
