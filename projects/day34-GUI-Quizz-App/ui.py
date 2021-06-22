import tkinter as tk
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 20, pady=20, bg=THEME_COLOR)

        self.canvas = tk.Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125, width=280,
            text="question text",
            font=("Arial", 15, "italic")
        )

        self.score_label = tk.Label(
            text="score: 0", bg=THEME_COLOR, font=("Arial", 12), fg="white"
        )
        true_img = tk.PhotoImage(file="./images/true.png")
        self.true_button = tk.Button(
            image=true_img, highlightthickness=0, bd=0,
            command=self.answer_true 
        )
        false_img = tk.PhotoImage(file="./images/false.png")
        self.false_button = tk.Button(
            image=false_img, highlightthickness=0, bd=0,
            command=self.answer_false
        )

        # ***** Positioning *****
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.score_label.grid(column=1, row=0)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)


        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        self.score_label.config(text=f"score: {self.quiz.score}")
        self.canvas["bg"] = "white"

        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text="You've reached the end of the quiz."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        self.window.after(1000, self.get_next_question)
        self.canvas["bg"] = "green" if is_right else "red"
