from tkinter import *
import json
from tkinter import messagebox

with open('data.json') as f:
    data = json.load(f)

question = data['question']
options = data['options']
points = data['points']
results = data['results']

gui = Tk()
gui.geometry("800x500")
gui.resizable(False, False)
gui.title("Mood detector")


class Questionaire:
    def __init__(self):
        self.q_no = 0
        self.display_title()
        self.display_question()
        self.opt_selected = IntVar()
        self.buttons()
        self.data_size = len(question)
        self.display_options()
        self.answer_ls = list()
        self.mood = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}

    def display_result(self):
        q_no = Label(gui,
                     text='\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t',
                     width=100, font=('Calibri', 15, 'bold'), anchor='w', wraplength=700)
        q_no.place(x=10, y=100)
        self.destroy_options()
        self.get_highest()
        print(self.mood)
        print(max(self.mood, key=self.mood.get))
        q_no = Label(gui, text=f'You are {results[max(self.mood, key=self.mood.get)]}', width=150,
                     font=('Calibri', 20, 'bold'), anchor='w', wraplength=780)
        q_no.place(x=10, y=70)
        end_button = Button(gui, text="Quit", command=gui.destroy,
                            width=10, bg="#ce2029", fg="white", font=("ariel", 16, "bold"))
        end_button.place(x=330,
                         # x=350
                         # y=380)
                         y=440)
        img_ls = ['img/image0.png', 'img/image1.png', 'img/image2.png', 'img/image3.png', 'img/image4.png',
                  'img/image5.png', 'img/image6.png', 'img/image7.png', 'img/image8.png', 'img/image9.png',
                  'img/image10.png', 'img/image11.png']
        image = PhotoImage(file=img_ls[max(self.mood, key=self.mood.get)])
        width, height = 180, 180
        image = image.subsample(int(image.width() / width), int(image.height() / height))
        label = Label(gui, image=image)
        label.image = image
        label.place(relx=0.5,
                    rely=0.55,
                    anchor='center')

    def get_highest(self):
        for i in range(len(self.answer_ls)):
            if i < len(points) and (self.answer_ls[i][1] - 1) < len(points[i]):
                for k in range(len(points[i][self.answer_ls[i][1] - 1])):
                    self.mood[points[i][self.answer_ls[i][1] - 1][k]] += 1
        return max(self.mood, key=self.mood.get)

    def next_btn(self):
        if self.opt_selected.get() == 0:
            messagebox.showwarning("DUMBASS", "You have to select an option before proceeding.")
        else:
            self.q_no += 1
            if self.q_no >= len(question):
                self.answer_ls.append((self.q_no, self.opt_selected.get()))
                print(self.answer_ls)
                self.display_result()
            else:
                self.answer_ls.append((self.q_no, self.opt_selected.get()))
                self.display_question()
                self.destroy_options()
                self.display_options()

                d2 = [item[1] for item in self.answer_ls]
                if self.q_no == 1 and d2[0] == 4:
                    self.mood[3] += 30
                    self.display_result()
                    return

    def destroy_options(self):
        for opt in self.opts:
            opt.destroy()
        self.opts = []

    def display_options(self):
        self.opts = []  # List to hold radio buttons
        y_pos = 150
        self.opt_selected.set(0)

        for i, option in enumerate(options[self.q_no]):
            radio_btn = Radiobutton(gui, text=option, variable=self.opt_selected, value=i + 1, font=("Calibri", 14))
            self.opts.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40

    def display_question(self):
        q_no = Label(gui, text='\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t',
                     width=100, font=('Calibri', 15, 'bold'), anchor='w', wraplength=700)
        q_no.place(x=10, y=100)
        q_no = Label(gui, text=question[self.q_no], width=100, font=('Calibri', 15, 'bold'), anchor='w', wraplength=700)
        q_no.place(x=10, y=70)

    def display_title(self):
        title = Label(gui, text="Mood detector", width=50, bg="#45b3e0", fg="white", font=("ariel", 20, "bold"))
        title.place(x=-30,
                    # x=0,
                    y=2)

    def buttons(self):
        next_button = Button(gui, text="Next", command=self.next_btn,
                             width=10, bg="#87ceeb", fg="white", font=("ariel", 16, "bold"))
        next_button.place(x=330,
                          # y=380)
                          y=440)


Mood_detector = Questionaire()

gui.mainloop()