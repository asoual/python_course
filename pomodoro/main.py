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
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    start_button.config(state=NORMAL)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    start_button.config(state=DISABLED)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown_timer(long_break_sec)
        timer_label.config(text="Long Break",fg=RED)
    elif reps % 2 == 0:
        countdown_timer(short_break_sec)
        timer_label.config(text="Short Break",fg=PINK)
    else:
        countdown_timer(work_sec)
        timer_label.config(text="Work",fg=GREEN)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown_timer(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text =f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown_timer, count -1)
    else:
        start_timer()
        check_mark = "" 
        for _ in range(math.floor(reps/2)):
            check_mark += "✓"
        check_label.config(text=f"{check_mark}")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize(300,300)
window.config(padx=150,pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img) 

timer_text = canvas.create_text(102,130,text=("00:00"),fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

timer_label = Label(text="Timer",bg=YELLOW,fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1,row=0)

start_button = Button(text="Start",command=start_timer, font=(FONT_NAME,12,"normal"))
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",command=reset_timer, font=(FONT_NAME,12,"normal"))
reset_button.grid(column=2,row=2)

check_label = Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME, 20, "bold"))
check_label.grid(column=1,row=3)

window.mainloop()