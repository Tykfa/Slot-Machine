from tkinter import *
from tkinter import messagebox
from game_window import Game
import sqlite3


class MainMenu:
    def __init__(self, username_input):
        self.root = Tk()
        self.stored_username = username_input
        title = str('Logged as' + ' ' + self.stored_username)
        self.root.title(title)
        self.root.geometry('288x384')
        self.root.resizable(False, False)

        self.users = sqlite3.connect('users.db')
        self.c = self.users.cursor()

        self.start_game_button = Button(self.root, text="Start Game", command=self.start_game)
        self.log_out_button = Button(self.root, text="Log Out", command=self.log_out)
        self.start_game_button.pack(pady=5)
        self.log_out_button.pack(pady=5)

        self.deposit_credits_button = Button(self.root, text="Deposit Credits", command=self.deposit_credits)
        self.deposit_credits_button.pack(pady=5)
        self.deposit_entry = Entry(self.root)
        self.deposit_entry.pack()

        self.withdraw_credits_button = Button(self.root, text="Withdraw Credits", command=self.withdraw_credits)
        self.withdraw_credits_button.pack(pady=5)
        self.withdraw_entry = Entry(self.root)
        self.withdraw_entry.pack()

    def start_game(self):
        self.root.destroy()
        Game(self.stored_username).run()

    def deposit_credits(self):
        # Code to deposit credits goes here
        deposit = self.deposit_entry.get()
        self.c.execute("UPDATE users SET credits = credits + ? WHERE username=?", (deposit, self.stored_username))
        self.users.commit()
        print("Depositing credits...")

    def withdraw_credits(self):
        # Code to withdraw credits goes here
        withdrawal = int(self.withdraw_entry.get())
        self.c.execute("SELECT credits FROM users WHERE username=?", (self.stored_username,))
        balance = self.c.fetchone()
        if withdrawal <= balance[0]:
            self.c.execute("UPDATE users SET credits = credits - ? WHERE username=?", (withdrawal, self.stored_username))
            self.users.commit()
            print("Withdrawing credits...")
        else:
            messagebox.showinfo("Withdrawal unsucesful!", "Not enough credits.")

    def log_out(self):
        from login_and_register_window import UserAuth
        self.root.destroy()
        self.users.close()
        UserAuth().run()

    def run(self):
        self.root.mainloop()
        self.users.close()
