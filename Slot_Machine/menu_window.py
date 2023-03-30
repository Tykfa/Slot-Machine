from tkinter import *
from game_window import Game


class MainMenu:
    def __init__(self, username_input):
        self.root = Tk()
        self.stored_username = username_input
        title = str('Logged as' + ' ' + self.stored_username)
        self.root.title(title)
        self.root.geometry('288x384')
        self.root.resizable(False, False)
        self.start_game_button = Button(self.root, text="Start Game", command=self.start_game)
        self.deposit_credits_button = Button(self.root, text="Deposit Credits", command=self.deposit_credits)
        self.withdraw_credits_button = Button(self.root, text="Withdraw Credits", command=self.withdraw_credits)
        self.log_out_button = Button(self.root, text="Log Out", command=self.log_out)
        self.start_game_button.pack(pady=5)
        self.deposit_credits_button.pack(pady=5)
        self.withdraw_credits_button.pack(pady=5)
        self.log_out_button.pack(pady=5)

    def start_game(self):
        self.root.destroy()
        Game(self.stored_username).run()

    def deposit_credits(self):
        # Code to deposit credits goes here
        print("Depositing credits...")

    def withdraw_credits(self):
        # Code to withdraw credits goes here
        print("Withdrawing credits...")

    def log_out(self):
        from login_and_register_window import UserAuth
        self.root.destroy()
        UserAuth().run()

    def run(self):
        self.root.mainloop()
