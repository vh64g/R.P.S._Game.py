import random
from tkinter import *


def exit_func():
    window.destroy()


def read_level():
    try:
        with open("level.txt", "r") as level_file:
            lev = int(level_file.readline())
            level.set(lev)
    except:
        print("Error found")
        lev = 0
        f = open("level.txt", "w+")
        f.writelines(str(lev))
        f.flush()
        level.set(lev)


def write_level():
    level_file_txt = level.get()
    f = open("level.txt", "w")
    f.writelines(level_file_txt)
    f.flush()


def new_game():
    scissors.configure(state=NORMAL)
    stone.configure(state=NORMAL)
    paper.configure(state=NORMAL)
    accept.configure(state=DISABLED)
    new_game1.configure(state=DISABLED)
    computer_choice2.set("")
    choice.set("")
    result.set("")


def level_up():
    lev = level.get()
    lev = int(lev) + 1
    level.set(lev)
    write_level()


def level_down():
    lev = level.get()
    lev = int(lev) - 1
    level.set(lev)
    write_level()


def run():
    choice1 = choice.get()
    sc_sv = scissors_str_var.get()
    st_sv = stone_str_var.get()
    pa_sv = paper_str_var.get()
    choice2 = random.randint(1, 3)
    if choice2 == 1:
        choice2 = "scissors"
        if choice1 == sc_sv:
            result.set("undetermined")
        elif choice1 == st_sv:
            result.set("You won")
            level_up()
        elif choice1 == pa_sv:
            result.set("You lose")
            level_down()
    elif choice2 == 2:
        choice2 = "stone"
        if choice1 == sc_sv:
            result.set("You lose")
            level_down()
        elif choice1 == st_sv:
            result.set("undetermined")
        elif choice1 == pa_sv:
            result.set("You won")
            level_up()
    elif choice2 == 3:
        choice2 = "paper"
        if choice1 == sc_sv:
            result.set("You won")
            level_up()
        elif choice1 == st_sv:
            result.set("You lose")
            level_down()
        elif choice1 == pa_sv:
            result.set("undetermined")
    computer_choice2.set(choice2)
    scissors.configure(state=DISABLED)
    stone.configure(state=DISABLED)
    paper.configure(state=DISABLED)
    accept.configure(state=DISABLED)
    new_game1.configure(state=NORMAL)


def choose_scissors():
    choice.set("scissors")
    accept.configure(state=NORMAL)


def choose_stone():
    choice.set("stone")
    accept.configure(state=NORMAL)


def choose_paper():
    choice.set("paper")
    accept.configure(state=NORMAL)


window = Tk()
window.title("SSP Game by V.H.")
window.configure(bg="black")

choice = StringVar()
computer_choice2 = StringVar()
result = StringVar()
scissors_str_var = StringVar()
stone_str_var = StringVar()
paper_str_var = StringVar()
level = StringVar()

scissors_str_var.set("scissors")
stone_str_var.set("stone")
paper_str_var.set("paper")
level.set("0")

read_level()

comment_top = Label(window, text="Choose carefully: ", bg="black", fg="red")
scissors = Button(window, text="scissors", bg="black", fg="#7CFC00", command=choose_scissors)
stone = Button(window, text="stone", bg="black", fg="#7CFC00", command=choose_stone)
paper = Button(window, text="paper", bg="black", fg="#7CFC00", command=choose_paper)
your_choice = Label(window, text="Your choice: ", bg="black", fg="red")
your_choice1 = Label(window, textvariable=choice, bg="black", fg="#FF00FF")
accept = Button(window, text="accept choice", bg="black", fg="#00FFFF", command=run, state=DISABLED)
computer_choice = Label(window, text="Computer choose: ", bg="black", fg="red")
computer_choice1 = Label(window, textvariable=computer_choice2, bg="black", fg="#FF00FF")
new_game1 = Button(window, text="New game", bg="black", fg="#FFFF00", state=DISABLED, command=new_game)
result0 = Label(window, text="Result: ", bg="black", fg="red")
result1 = Label(window, textvariable=result, bg="black", fg="#FF00FF")
level_l = Label(window, text="Your Level:",  bg="black", fg="red")
show_l = Label(window, textvariable=level,  bg="black", fg="#FF00FF")
exit_b = Button(window, text="exit", padx=20, bg="black", fg="#FF4500", command=exit_func)

comment_top.grid(row=1, column=1)
scissors.grid(row=1, column=2)
stone.grid(row=1, column=3)
paper.grid(row=1, column=4)
your_choice.grid(row=2, column=1)
your_choice1.grid(row=2, column=2)
accept.grid(row=2, column=5)
computer_choice.grid(row=3, column=1)
computer_choice1.grid(row=3, column=2)
new_game1.grid(row=3, column=5)
result0.grid(row=4, column=1)
result1.grid(row=4, column=2)
level_l.grid(row=5, column=1)
show_l.grid(row=5, column=2)
exit_b.grid(row=5, column=5)

window.mainloop()
# cc vh64g
