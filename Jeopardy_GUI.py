from tkinter import *


class Application (Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Header
        Label(self, text="Jeopardy", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=0, column=0, columnspan=5, sticky=N+S+E+W)

        # Category labels
        Label(self, text="Python", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=1, column=0, columnspan=1, sticky=N+S+E+W)
        Label(self, text="Numbers", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=1, column=1, columnspan=1, sticky=N+S+E+W)
        Label(self, text="Memes", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=1, column=2, columnspan=1, sticky=N+S+E+W)
        Label(self, text="BCA", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=1, column=3, columnspan=1, sticky=N+S+E+W)
        Label(self, text="Miscellaneous", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=1, column=4, columnspan=1, sticky=N+S+E+W)

        # 100 Point row
        self.cat1_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red") #command
        self.cat1_100.grid(row=2, column=0, sticky=N+S+E+W)
        self.cat2_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red") #command
        self.cat2_100.grid(row=2, column=1, sticky=N+S+E+W)
        self.cat3_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red") #command
        self.cat3_100.grid(row=2, column=2, sticky=N+S+E+W)
        self.cat4_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red") #command
        self.cat4_100.grid(row=2, column=3, sticky=N+S+E+W)
        self.cat5_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red") #command
        self.cat5_100.grid(row=2, column=4, sticky=N+S+E+W)

        # 200 Point row
        self.cat1_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange")  # command
        self.cat1_200.grid(row=3, column=0, sticky=N+S+E+W)
        self.cat2_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange")  # command
        self.cat2_200.grid(row=3, column=1, sticky=N+S+E+W)
        self.cat3_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange")  # command
        self.cat3_200.grid(row=3, column=2, sticky=N+S+E+W)
        self.cat4_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange")  # command
        self.cat4_200.grid(row=3, column=3, sticky=N+S+E+W)
        self.cat5_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange")  # command
        self.cat5_200.grid(row=3, column=4, sticky=N+S+E+W)

        # 300 Point row
        self.cat1_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow")  # command
        self.cat1_300.grid(row=4, column=0, sticky=N+S+E+W)
        self.cat2_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow")  # command
        self.cat2_300.grid(row=4, column=1, sticky=N+S+E+W)
        self.cat3_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow")  # command
        self.cat3_300.grid(row=4, column=2, sticky=N+S+E+W)
        self.cat4_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow")  # command
        self.cat4_300.grid(row=4, column=3, sticky=N+S+E+W)
        self.cat5_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow")  # command
        self.cat5_300.grid(row=4, column=4, sticky=N+S+E+W)

        # 400 Point row
        self.cat1_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green")  # command
        self.cat1_400.grid(row=5, column=0, sticky=N+S+E+W)
        self.cat2_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green")  # command
        self.cat2_400.grid(row=5, column=1, sticky=N+S+E+W)
        self.cat3_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green")  # command
        self.cat3_400.grid(row=5, column=2, sticky=N+S+E+W)
        self.cat4_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green")  # command
        self.cat4_400.grid(row=5, column=3, sticky=N+S+E+W)
        self.cat5_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green")  # command
        self.cat5_400.grid(row=5, column=4, sticky=N+S+E+W)

        # 500 Point row
        self.cat1_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="purple")  # command
        self.cat1_500.grid(row=6, column=0, sticky=N+S+E+W)
        self.cat2_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="purple")  # command
        self.cat2_500.grid(row=6, column=1, sticky=N+S+E+W)
        self.cat3_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="purple")  # command
        self.cat3_500.grid(row=6, column=2, sticky=N+S+E+W)
        self.cat4_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="purple")  # command
        self.cat4_500.grid(row=6, column=3, sticky=N+S+E+W)
        self.cat5_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="purple")  # command
        self.cat5_500.grid(row=6, column=4, sticky=N+S+E+W)

        # Question box
        Label(self, text="Question:", font=("Comic Sans", 15)).grid(row=7, column=2, columnspan=2, sticky=N+S+E+W)
        self.question = Text(self, height=5, wrap=WORD)
        self.question.grid(row=8, column=0, columnspan=5)

        # Answer box
        Label(self, text="Answer:", font=("Comic Sans", 15)).grid(row=9, column=2, columnspan=2, sticky=N + S + E + W)
        self.answer = Text(self, height=2, wrap=WORD)
        self.answer.grid(row=10, column=0, columnspan=5)
        self.enter = Button(self, text="Enter", font=("Comic Sans", 15), relief="solid", bg="blue")  # command
        self.enter.grid(row=11, column=2, columnspan=2, sticky=N + S + E + W)
        self.correct = Text(self, height=2, wrap=WORD)
        self.correct.grid(row=12, column=0, columnspan=5)

        # Footer
        Label(self, text=" ", relief="solid", font=("Comic Sans", 30), bg="blue").grid(row=13, column=0, columnspan=5, sticky=N + S + E + W)

    def question_bttn(self, question):
        Text(self, text=question[0])
    def answer(self, question):
        Text(self, text=question[1])
        # self.msg_txt = Text(self, width=50, height=10, wrap=WORD)
        # self.msg_txt.grid(row=3, column=0, columnspan=4


root = Tk()
root.title("Jeopardy")
app = Application(root)
root.mainloop()