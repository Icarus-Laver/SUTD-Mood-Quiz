from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import subprocess

root = Tk()
root.title("Test")

width = 640
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
#bg = PhotoImage(file="C:\\Users\Acer\PycharmProjects\pythonProject\.png")
#my_label = Label(root,image=bg)
#my_label.place(x=0,y=0,relwidth=1,relheight=1)

def Database():
    global conn, cursor
    conn = sqlite3.connect("db_list.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")

USERNAME = StringVar()
PASSWORD = StringVar()
def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    root.configure(background='white')
    LoginFrame.pack(side=TOP, pady=80)
    lbl_username = Label(LoginFrame, text="Username:", font=('Impact', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(LoginFrame, text="Password:", font=('Impact', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=('Arial', 18))
    lbl_result1.grid(row=3, columnspan=2)
    username = Entry(LoginFrame, font=('Impact', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(LoginFrame, font=('Impact', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(LoginFrame, text="Login", font=('Impact', 18), width=35, command=Login)
    btn_login.grid(row=4, columnspan=2, pady=20)
    lbl_register = Label(LoginFrame, text="Register", fg="Blue", font=('arial', 12))
    lbl_register.grid(row=0, sticky=W)
    lbl_register.bind('<Button-1>', ToggleToRegister)

def RegisterForm():
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame(root)
    root.configure(background='white')
    RegisterFrame.pack(side=TOP, pady=80)
    lbl_username = Label(RegisterFrame, text="Username:", font=('Impact', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(RegisterFrame, text="Password:", font=('Impact', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_result2 = Label(RegisterFrame, text="", font=('Arial', 18))
    lbl_result2.grid(row=5, columnspan=2)
    username = Entry(RegisterFrame, font=('Impact', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(RegisterFrame, font=('Impact', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(RegisterFrame, text="Register", font=('Impact', 18), width=35, command=Register)
    btn_login.grid(row=6, columnspan=2, pady=20)
    lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', ToggleToLogin)


def Exit():
    result = tkMessageBox.askquestion('System', 'Exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def ToggleToLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()


def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()


def Register():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result2.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Username is already taken", fg="red")
        else:
            cursor.execute("INSERT INTO `member` (username, password) VALUES(?, ?)",
                           (str(USERNAME.get()), str(PASSWORD.get())))
            conn.commit()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result2.config(text="Successfully Created!", fg="green")

        cursor.close()
        conn.close()


def Login():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            lbl_result1.config(text="You Successfully Login", fg="green")
            try:
                subprocess.run(['python', 'quiz.py'], check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error running quiz.py: {e}')
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")


LoginForm()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

if __name__ == '__main__':
    root.mainloop()