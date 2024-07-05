from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        #window setup
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        #score setup
        self.score_label = Label(text='Score : 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        #canvas setup
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        #question
        self.question_text = self.canvas.create_text(
            150,
            125,
            width = 280,
            text='A question',
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )
        #images
        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')
        #buttons
        self.true_button = Button(image=true_img, highlightthickness= 0, command= self.get_next_question)
        self.false_button = Button(image=false_img, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)



        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        q_text = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)





















        self.window.mainloop()




