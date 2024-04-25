from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repos = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_title.config(text="Timer")
    check.config(text="")
    global repos
    repos = 1

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global repos
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repos % 8 == 0:
        count_down(long_break_sec)
        timer_title.config(text="Break", fg=RED)
    elif repos % 2 == 0:
        count_down(short_break_sec)
        timer_title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_title.config(text="Work", fg=GREEN)
    repos += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'     # Dynamic typing

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if repos % 2 == 0:
            mark = ""
            for _ in range(math.floor(count / 2)):
                mark += 'r'
            check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg="YELLOW")

timer_title = Label(window, text="Timer", font=(FONT_NAME, 30, "bold"), bg="YELLOW", fg="GREEN")
timer_title.grid(column=1, row=0)

start_button = Button(window, text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(window, text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check = Label(font=(FONT_NAME, 8, "bold"),bg="YELLOW", fg="GREEN", anchor=CENTER)
check.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg="YELLOW", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()
