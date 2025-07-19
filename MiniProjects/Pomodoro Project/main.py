from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps

    window.after_cancel(timer)
    title_label.config(text="Timer")
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps % 8 == 0:
        title_label.config(text="BREAK", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="WORKING", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            add_checkmark()
# ---------------------------- UI SETUP ------------------------------- #
def add_checkmark():
    work_sessions = math.floor(reps/2)
    mark = ""
    for _ in range(work_sessions):
        mark += "✔"
    check_label.config(text=mark)

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

first_coords = Label(text="")

title_label = Label(text="Timer", fg=PINK, bg=YELLOW, font=("Courier", 45, "bold"))
title_label.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=3)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=4)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=4)

check_label = Label(text="", fg=GREEN, bg=YELLOW)
check_label.grid(column=2, row=5)

window.mainloop()