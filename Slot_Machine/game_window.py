from random import choice
from tkinter import *
import game_settings as gs

player_username = "Test_Username"
player_credits = 100

root = Tk()
root.configure(bg="peach puff")
root.geometry("288x384")
root.title("Slot Machine")
root.resizable(False, False)


def randomize_reels():
    for i in range(3):
        gs.payline.append(choice(gs.SYMBOLS))
        del gs.payline[0]


def all_same(payline_list):
    return all(x == payline_list[0] for x in payline_list)


def spin_it():
    global player_credits
    if player_credits >= 5:
        player_credits -= 5
        randomize_reels()
        reel_one.config(text=f"{gs.payline[-3]}")
        reel_two.config(text=f"{gs.payline[-2]}")
        reel_three.config(text=f"{gs.payline[-1]}")

        if all_same(gs.payline):
            player_credits += 15
            result_label.config(text=f" You have won! \n Congratulations", fg="gold")
            player_credits_label.config(text=f"Your credits:\n {player_credits} $")
            return True
        elif not all_same(gs.payline):
            result_label.config(text="You have lost", fg="black")
            player_credits_label.config(text=f"Your credits:\n {player_credits} $")
            return False
        else:
            raise TypeError("001")
    elif player_credits < 5:
        lever.config(text="Insert more credits", relief="groove", bg=gs.MAIN_COLOR)
        lever["state"] = DISABLED
        reel_one.config(text=f"")
        reel_two.config(text=f"")
        reel_three.config(text=f"")
        exit_to_menu_button.config(bg=gs.SECONDARY_COLOR, fg="gold")
        player_label.config(text=f"See you soon, \n {player_username}!")
    else:
        raise TypeError("002")


interface_frame = Frame(root, bg=gs.MAIN_COLOR)
reels_frame = Frame(interface_frame)
info_frame = Frame(interface_frame, bg=gs.MAIN_COLOR)
exit_buttons_frame = Frame(interface_frame, bg=gs.MAIN_COLOR)

price_label = Label(
    interface_frame,
    text="Spin prize: 5$",
    font="Helvetica 20 bold",
    width=gs.MACHINE_WIDTH - 20,
    height=gs.DEFAULT_WIDGET_HEIGHT - 1,
    bg=gs.MAIN_COLOR,
    fg=gs.SECONDARY_COLOR,
)
reel_one = Label(
    reels_frame,
    text=f"{gs.payline[-3]}",
    width=gs.REEL_WIDTH,
    height=gs.DEFAULT_WIDGET_HEIGHT,
    borderwidth=1,
    relief="sunken",
)
reel_two = Label(
    reels_frame,
    text=f"{gs.payline[-2]}",
    width=gs.REEL_WIDTH,
    height=gs.DEFAULT_WIDGET_HEIGHT,
    borderwidth=1,
    relief="sunken",
)
reel_three = Label(
    reels_frame,
    text=f"{gs.payline[-1]}",
    width=gs.REEL_WIDTH,
    height=gs.DEFAULT_WIDGET_HEIGHT,
    borderwidth=1,
    relief="sunken",
)
result_label = Label(
    interface_frame,
    text=" ",
    font="Helvetica 13 bold",
    width=gs.MACHINE_WIDTH - 18,
    height=gs.DEFAULT_WIDGET_HEIGHT - 1,
    bg=gs.MAIN_COLOR,
)
lever = Button(
    interface_frame,
    text="Spin It!",
    command=spin_it,
    font="Helvetica 13 bold",
    width=gs.MACHINE_WIDTH - 18,
    height=gs.DEFAULT_WIDGET_HEIGHT,
    bg=gs.SECONDARY_COLOR,
)
player_label = Label(
    info_frame,
    font="Helvetica 10 bold",
    text=f"Welcome, \n {player_username}!",
    width=gs.MACHINE_WIDTH - 20,
    height=gs.DEFAULT_WIDGET_HEIGHT,
    bg=gs.MAIN_COLOR,
)
player_credits_label = Label(
    info_frame,
    font="Helvetica 10 bold",
    text=f"Your credits:\n {player_credits}$",
    width=gs.MACHINE_WIDTH - 20,
    height=gs.DEFAULT_WIDGET_HEIGHT,
    bg=gs.MAIN_COLOR,
)
exit_game_button = Button(
    exit_buttons_frame,
    font="Helvetica 8 bold",
    command=exit,
    text="Exit game",
    width=gs.MACHINE_WIDTH - 18,
    height=gs.DEFAULT_WIDGET_HEIGHT - 1,
    bg=gs.MAIN_COLOR,
)
exit_to_menu_button = Button(
    exit_buttons_frame,
    font="Helvetica 8 bold",
    command=exit,
    text="Exit to main menu",
    width=gs.MACHINE_WIDTH - 18,
    height=gs.DEFAULT_WIDGET_HEIGHT - 1,
    bg=gs.MAIN_COLOR,
)

reel_one.grid(row=1, column=0)
reel_two.grid(row=1, column=1)
reel_three.grid(row=1, column=2)
player_label.grid(row=0, column=0)
player_credits_label.grid(row=0, column=1)
exit_to_menu_button.grid(row=0)
exit_game_button.grid(row=0, column=1)

interface_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
price_label.grid(row=0, columnspan=1)
reels_frame.grid(row=1, columnspan=4)
lever.grid(row=2, columnspan=3)
result_label.grid(row=3)
info_frame.grid(row=4)
exit_buttons_frame.grid(row=5)
root.mainloop()
