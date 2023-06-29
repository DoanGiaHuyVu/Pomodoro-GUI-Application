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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    check_mark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = 10
    short_break_sec = 3
    long_break_sec = 5

    if reps % 8 == 0:
        count_down(long_break_sec)
        my_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        my_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        my_label.config(text="Work", fg=GREEN)


# If there is no reps
#     if reps % 2 == 0:
#         count_down(work_sec)
#         reps += 1
#     elif reps % 7 == 0:
#         count_down(long_break_sec)
#         reps += 1
#     else:
#         count_down(short_break_sec)
#         reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# Cannot use for loop here

def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)

        # if reps % 2 == 0:
        #     check_marks = "✔"
        #     check_mark.config(text=f"{check_marks}")
        # else:
        #     check_mark.config(text="")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# foreground (fg)
my_label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
my_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # pixels
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # x, y

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# Start button
start_btn = Button(text="Start", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

# Reset button
reset_btn = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()
