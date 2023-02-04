import random
from tkinter import *

root = Tk()
root.configure(bg='peach puff')
root.geometry('480x480')
root.title('Slot Machine')
root.resizable(False, False)


SYMBOLS = ('SEVEN', 'bell', 'orange')  # , 'lemon', 'twoja stara', 'PIWSKO')
payline = ['', '', '']


def randomize_reels():
    for i in range(3):
        payline.append(random.choice(SYMBOLS))
        del payline[0]


def all_same(payline_list):
    return all(x == payline_list[0] for x in payline_list)


def spin_it():
    randomize_reels()
    reel_one.config(text=f'{payline[-3]}')
    reel_two.config(text=f'{payline[-2]}')
    reel_three.config(text=f'{payline[-1]}')

    if all_same(payline):
        result_label.config(text='Win')
    elif not all_same(payline):
        result_label.config(text='Lost')
    else:
        raise TypeError('001')



reel_one = Label(root, text=f'{payline[-3]}')
reel_two = Label(root, text=f'{payline[-2]}')
reel_three = Label(root, text=f'{payline[-1]}')
reel_one.grid(row=0, column=1)
reel_two.grid(row=0, column=2)
reel_three.grid(row=0, column=3)
result_label = Label(root, text='   ')
result_label.grid(row=3)

spin_it()

lever = Button(root, text='Spin It', command=spin_it)
lever.grid(row=1, columnspan=3)



root.mainloop()
