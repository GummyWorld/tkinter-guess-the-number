from tkinter import *

import random as rnd

class Application(Frame):

    def __init__(self, master): #creates the frame
        self.master = master
        master.title("Guess the number")

        #creates a label of a random number in the range of 10
        self.quit_button=Button(master, text="QUIT", command=master.quit)
        self.quit_button.pack(padx=5, pady=10)

        #Label of the number chosen
        self.chosen_number=Label(master, text=str(rnd.randrange(10)))
        self.chosen_number.pack(padx=5, pady=10)

        #Button that has the function to change the number chosen
        self.change_number=Button(master, text="CHANGE", command=self.change)
        self.change_number.pack()

        #Checks the answer
        self.check_button=Button(master, text="Check your answer?", command=self.check_number)
        self.check_button.pack()

        #Creates a entry for answer input
        self.entry_name=Label(master, text="Your Guess")
        self.entry_name.pack(padx=5, pady=20, side=LEFT)

        #Tje player's guess
        self.answer_entry=Entry(master)
        self.answer_entry.pack(padx=5, pady=20, side=LEFT)

        #Slider to show value
        self.range_slider=Scale(master, from_=0, to=100, orient=HORIZONTAL)
        self.range_slider.pack(padx=5, pady=20, side=LEFT)

        self.range_explain=Label(master, text="Range")
        self.range_explain.pack(padx=5, pady=20, side=LEFT)

    #Change the number to a new number in the range of 10
    def change(self):
        self.chosen_number.config(text=rnd.randrange(self.range_slider.get()))
        
        self.chosen_number.config(background="black")
        
    #Check if the number is right
    def check_number(self):
        if self.answer_entry.get() == self.chosen_number["text"]:
            correct_window=Toplevel(root)
            correct_text=Label(correct_window, text="Correct!")
            correct_text.pack()

            self.chosen_number.config(background="white")

        elif self.answer_entry.get() != self.chosen_number["text"]:
            wrong_window=Toplevel(root)
            wrong_text=Label(wrong_window, text="Wrong!")
            wrong_text.pack()

            self.chosen_number.config(background="white")
        

root = Tk()
app = Application(root)
root.mainloop()

        ##w = tk.Label(root, bg = "blue", text="Hello Tkinter")
        ##w.config(root, bg = "0000ff")
        ##w.pack()
