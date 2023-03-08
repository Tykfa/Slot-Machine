from random import choice
from tkinter import *
import game_settings as gs


class Game:
    def __init__(self):
        self.player_username = "Test_Username"
        self.player_credits = 100

        self.root = Tk()
        self.root.configure(bg="peach puff")
        self.root.geometry("288x384")
        self.root.title("Slot Machine")
        self.root.resizable(False, False)

        self.interface_frame = Frame(self.root, bg=gs.MAIN_COLOR)
        self.reels_frame = Frame(self.interface_frame)
        self.info_frame = Frame(self.interface_frame, bg=gs.MAIN_COLOR)
        self.exit_buttons_frame = Frame(self.interface_frame, bg=gs.MAIN_COLOR)

        self.price_label = Label(
            self.interface_frame,
            text="Spin prize: 5$",
            font="Helvetica 20 bold",
            width=gs.MACHINE_WIDTH - 20,
            height=gs.DEFAULT_WIDGET_HEIGHT - 1,
            bg=gs.MAIN_COLOR,
            fg=gs.SECONDARY_COLOR,
        )
        self.reel_one = Label(
            self.reels_frame,
            text=f"{gs.payline[-3]}",
            width=gs.REEL_WIDTH,
            height=gs.DEFAULT_WIDGET_HEIGHT,
            borderwidth=1,
            relief="sunken",
        )
        self.reel_two = Label(
            self.reels_frame,
            text=f"{gs.payline[-2]}",
            width=gs.REEL_WIDTH,
            height=gs.DEFAULT_WIDGET_HEIGHT,
            borderwidth=1,
            relief="sunken",
        )
        self.reel_three = Label(
            self.reels_frame,
            text=f"{gs.payline[-1]}",
            width=gs.REEL_WIDTH,
            height=gs.DEFAULT_WIDGET_HEIGHT,
            borderwidth=1,
            relief="sunken",
        )
        self.result_label = Label(
            self.interface_frame,
            text=" ",
            font="Helvetica 13 bold",
            width=gs.MACHINE_WIDTH - 18,
            height=gs.DEFAULT_WIDGET_HEIGHT - 1,
            bg=gs.MAIN_COLOR,
        )
        self.lever = Button(
            self.interface_frame,
            text="Spin It!",
            command=self.spin_it,
            font="Helvetica 13 bold",
            width=gs.MACHINE_WIDTH - 18,
            height=gs.DEFAULT_WIDGET_HEIGHT,
            bg=gs.SECONDARY_COLOR,
        )
        self.player_label = Label(
            self.info_frame,
            font="Helvetica 10 bold",
            text=f"Welcome, \n {self.player_username}!",
            width=gs.MACHINE_WIDTH - 20,
            height=gs.DEFAULT_WIDGET_HEIGHT,
            bg=gs.MAIN_COLOR,
        )
        self.player_credits_label = Label(
            self.info_frame,
            font="Helvetica 10 bold",
            text=f"Your credits:\n {self.player_credits}$",
            width=gs.MACHINE_WIDTH - 20,
            height=gs.DEFAULT_WIDGET_HEIGHT,
            bg=gs.MAIN_COLOR,
        )
        self.exit_game_button = Button(
            self.exit_buttons_frame,
            font="Helvetica 8 bold",
            command=exit,
            text="Exit game",
            width=gs.MACHINE_WIDTH - 18,
            height=gs.DEFAULT_WIDGET_HEIGHT - 1,
            bg=gs.MAIN_COLOR,
        )
        self.exit_to_menu_button = Button(
            self.exit_buttons_frame,
            font="Helvetica 8 bold",
            command=exit,
            text="Exit to main menu",
            width=gs.MACHINE_WIDTH - 18,
            height=gs.DEFAULT_WIDGET_HEIGHT - 1,
            bg=gs.MAIN_COLOR,
        )

        self.reel_one.grid(row=1, column=0)
        self.reel_two.grid(row=1, column=1)
        self.reel_three.grid(row=1, column=2)
        self.player_label.grid(row=0, column=0)
        self.player_credits_label.grid(row=0, column=1)
        self.exit_to_menu_button.grid(row=0)
        self.exit_game_button.grid(row=0, column=1)

        self.interface_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.price_label.grid(row=0, columnspan=1)
        self.reels_frame.grid(row=1, columnspan=4)
        self.lever.grid(row=2, columnspan=3)
        self.result_label.grid(row=3)
        self.info_frame.grid(row=4)
        self.exit_buttons_frame.grid(row=5)

    def randomize_reels(self):
        for i in range(3):
            gs.payline.append(choice(gs.SYMBOLS))
            del gs.payline[0]

    def all_same(self, payline_list):
        return all(x == payline_list[0] for x in payline_list)

    def spin_it(self):
        if self.player_credits >= 5:
            self.player_credits -= 5
            self.randomize_reels()
            self.reel_one.config(text=f"{gs.payline[-3]}")
            self.reel_two.config(text=f"{gs.payline[-2]}")
            self.reel_three.config(text=f"{gs.payline[-1]}")

            if self.all_same(gs.payline):
                self.player_credits += 15
                self.result_label.config(text=f" You have won! \n Congratulations", fg="gold")
                self.player_credits_label.config(text=f"Your credits:\n {self.player_credits} $")
                return True
            elif not self.all_same(gs.payline):
                self.result_label.config(text="You have lost", fg="black")
                self.player_credits_label.config(text=f"Your credits:\n {self.player_credits} $")
                return False
            else:
                raise TypeError("001")
        elif self.player_credits < 5:
            self.lever.config(text="Insert more credits", relief="groove", bg=gs.MAIN_COLOR)
            self.lever["state"] = DISABLED
            self.reel_one.config(text=f"")
            self.reel_two.config(text=f"")
            self.reel_three.config(text=f"")
            self.exit_to_menu_button.config(bg=gs.SECONDARY_COLOR, fg="gold")
            self.player_label.config(text=f"See you soon, \n {self.player_username}!")
        else:
            raise TypeError("002")

    def run(self):
        self.root.mainloop()
