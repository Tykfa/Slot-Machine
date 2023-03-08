from tkinter import *
from tkinter import messagebox
import sqlite3
import game_window as gw


root = Tk()
root.configure(bg="peach puff")
root.geometry("288x384")
root.title("Log in or Register")
root.resizable(False, False)

Label(root, text="Username").grid(row=0, column=0)
username_entry = Entry(root)
username_entry.grid(row=0, column=1)

Label(root, text="Password").grid(row=1, column=0)
password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1)

users = sqlite3.connect("users.db")
c = users.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY,
             username TEXT NOT NULL UNIQUE,
             password TEXT NOT NULL,
             credits INTEGER)""")
users.commit()


def login():
    username = username_entry.get()
    password = password_entry.get()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    if user:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        root.destroy()
        game = gw.Game()
        game.run()  # here open main menu that stores loged in user info

    else:
        messagebox.showerror("Login Error", "Invalid username or password")


def register():
    username = username_entry.get()
    password = password_entry.get()

    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        users.commit()
        messagebox.showinfo("Registration Successful", "Welcome, " + username + "!")
        root.destroy()
        game = gw.Game()
        game.run()  # here open main menu that stores loged in user info

    except sqlite3.IntegrityError:
        messagebox.showerror("Registration Error", "Username already taken")


login_button = Button(root, text="Login", command=login)
login_button.grid(row=2, column=0)

register_button = Button(root, text="Register", command=register)
register_button.grid(row=2, column=1)


root.mainloop()
users.close()
