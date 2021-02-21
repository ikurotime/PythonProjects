import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text= '00:00')
    timer_label.config(text= 'Timer')
    check_label.config(text= '')
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec= WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Break', fg= PINK)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='Break', fg= RED)

    else:
        count_down(work_sec)
        timer_label.config(text='Work', fg= GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    global timer
    if int(seconds) < 10:
        seconds = f'0{seconds}'
    if minutes < 10:
        minutes = f'0{minutes}'
    canvas.itemconfig(timer_text,text= f'{minutes}:{seconds}')
    if count > 0:
       timer = window.after(1000,count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = (math.floor(reps/2))
        for _ in range(work_sessions):
            marks += '✔'
            check_label['text'] = marks
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
window.minsize(width=500, height=450)
window.maxsize(width=500, height=450)
# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Labels
timer_label = Label(text='Timer', font=(FONT_NAME, 50, "normal"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)
check_label = Label(text='', fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)
# Buttons
button_start = Button(text='Start', command= start_timer, highlightthickness=0)
button_start.grid(column=0, row=2)
button_reset = Button(text='Reset', command= reset_timer, highlightthickness=0)
button_reset.grid(column=2, row=2)


window.mainloop()
