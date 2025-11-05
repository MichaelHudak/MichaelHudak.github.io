from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        # Builds display window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Instantiate Score display
        self.score = 0
        self.score_display = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_display.grid(column=1, row=0)

        # Instantiates Canvas object to display question text
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="", width=275,
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Instantiates display of check mark image
        true_image = PhotoImage(file="images/true.png")
        self.true_but = Button(image=true_image, command=self.true_press)
        self.true_but.grid(column=0, row=2)

        # Instantiates display of X mark image
        false_image = PhotoImage(file="images/false.png")
        self.false_but = Button(image=false_image, command=self.false_press)
        self.false_but.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_display.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The End")
            self.true_but.config(state="disabled")
            self.false_but.config(state="disabled")

    def true_press(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right) #this is a two-line version of the same code in false_press

    def false_press(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

