from tkinter import *

class Application (Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #Top label
        Label(self, text="Jeopardy", relief="solid", font=("Comic Sans", 30)).grid(row=0, column=0, columnspan=5, sticky=N)

        #Category labels
        Label(self, text="Python", relief="solid", font=("Comic Sans", 30)).grid(row=1, column=0, columnspan=1, sticky=N)
        Label(self, text="Numbers", relief="solid", font=("Comic Sans", 30)).grid(row=1, column=1, columnspan=1, sticky=N)
        Label(self, text="Memes", relief="solid", font=("Comic Sans", 30)).grid(row=1, column=2, columnspan=1, sticky=N)
        Label(self, text="BCA", relief="solid", font=("Comic Sans", 30)).grid(row=1, column=3, columnspan=1, sticky=N)
        Label(self, text="Miscellaneous", relief="solid", font=("Comic Sans", 30)).grid(row=1, column=4, columnspan=1,sticky=N)

        # 100 Point row
        cat1_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red") #command
        cat1_100.grid(row=2, column=0, sticky=N)
        cat2_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red") #command
        cat2_100.grid(row=2, column=1, sticky=N)
        cat3_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red") #command
        cat3_100.grid(row=2, column=2, sticky=N)
        cat4_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red") #command
        cat4_100.grid(row=2, column=3, sticky=N)
        cat5_100 = Button(self, text="100", font=("Comic Sans", 30), relief="solid", bg="red") #command
        cat5_100.grid(row=2, column=4, sticky=N)

        # 200 Point row
        cat1_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange")  # command
        cat1_200.grid(row=3, column=0, sticky=N)
        cat2_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange")  # command
        cat2_200.grid(row=3, column=1, sticky=N)
        cat3_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange")  # command
        cat3_200.grid(row=3, column=2, sticky=N)
        cat4_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange")  # command
        cat4_200.grid(row=3, column=3, sticky=N)
        cat5_200 = Button(self, text="200", font=("Comic Sans", 30), relief="solid", bg="orange")  # command
        cat5_200.grid(row=3, column=4, sticky=N)

        # 300 Point row
        cat1_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow")  # command
        cat1_300.grid(row=4, column=0, sticky=N)
        cat2_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow")  # command
        cat2_300.grid(row=4, column=1, sticky=N)
        cat3_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow")  # command
        cat3_300.grid(row=4, column=2, sticky=N)
        cat4_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow")  # command
        cat4_300.grid(row=4, column=3, sticky=N)
        cat5_300 = Button(self, text="300", font=("Comic Sans", 30), relief="solid", bg="yellow")  # command
        cat5_300.grid(row=4, column=4, sticky=N)

        # 400 Point row
        cat1_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green")  # command
        cat1_400.grid(row=5, column=0, sticky=N)
        cat2_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green")  # command
        cat2_400.grid(row=5, column=1, sticky=N)
        cat3_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green")  # command
        cat3_400.grid(row=5, column=2, sticky=N)
        cat4_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green")  # command
        cat4_400.grid(row=5, column=3, sticky=N)
        cat5_400 = Button(self, text="400", font=("Comic Sans", 30), relief="solid", bg="green")  # command
        cat5_400.grid(row=5, column=4, sticky=N)

        # 500 Point row
        cat1_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="blue")  # command
        cat1_500.grid(row=6, column=0, sticky=N)
        cat2_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="blue")  # command
        cat2_500.grid(row=6, column=1, sticky=N)
        cat3_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="blue")  # command
        cat3_500.grid(row=6, column=2, sticky=N)
        cat4_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="blue")  # command
        cat4_500.grid(row=6, column=3, sticky=N)
        cat5_500 = Button(self, text="500", font=("Comic Sans", 30), relief="solid", bg="blue")  # command
        cat5_500.grid(row=6, column=4, sticky=N)

    def question_bttn(self, question):
        Text(self, text=question[0])
    def answer(self, question):
        Text(self, text=question[1])
        #self.msg_txt = Text(self, width=50, height=10, wrap=WORD)
        #self.msg_txt.grid(row=3, column=0, columnspan=4)


root = Tk()
root.title("Jeopardy")
app = Application(root)
root.mainloop()