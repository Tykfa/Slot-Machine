from tkinter import *
from tkinter import messagebox
import sqlite3
from menu_window import MainMenu


class UserAuth:
    def __init__(self):
        self.root = Tk()
        self.root.configure(bg="peach puff")
        self.root.geometry("288x384")
        self.root.title("Log in or Register")
        self.root.resizable(False, False)

        Label(self.root, text="Username").grid(row=0, column=0)
        self.username_entry = Entry(self.root)
        self.username_entry.grid(row=0, column=1)

        Label(self.root, text="Password").grid(row=1, column=0)
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.grid(row=1, column=1)

        self.users = sqlite3.connect("users.db")
        self.c = self.users.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS users (
                     id INTEGER PRIMARY KEY,
                     username TEXT NOT NULL UNIQUE,
                     password TEXT NOT NULL,
                     credits INTEGER)""")
        self.users.commit()
        login_button = Button(self.root, text="Login", command=self.login)
        login_button.grid(row=2, column=0)

        register_button = Button(self.root, text="Register", command=self.register)
        register_button.grid(row=2, column=1)

    def login(self):
        username_input = self.username_entry.get()
        password = self.password_entry.get()

        self.c.execute("SELECT * FROM users WHERE username=? AND password=?", (username_input, password))
        user = self.c.fetchone()
        if user:
            messagebox.showinfo("Login Successful", "Welcome, " + username_input + "!")
            self.root.destroy()
            MainMenu(username_input).run()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

    def register(self):
        username_input = self.username_entry.get()
        password = self.password_entry.get()

        try:
            self.c.execute("INSERT INTO users (username, password, credits) VALUES (?, ?, ?)", (username_input, password, 0))
            self.users.commit()
            messagebox.showinfo("Registration Successful", "Welcome, " + username_input + "!")
            self.root.destroy()
            MainMenu(username_input).run()

        except sqlite3.IntegrityError:
            messagebox.showerror("Registration Error", "Username already taken")

    def run(self):
        self.root.mainloop()
        self.users.close()


if __name__ == "__main__":
    UserAuth().run()
