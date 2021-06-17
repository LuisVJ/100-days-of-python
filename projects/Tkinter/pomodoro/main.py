import tkinter as tk

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
def reset():
    global reps
    reps = 0
    start_button["state"] = "active"
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    mark_label.config(text="")

# ---------------------------- TIMER MECHANISM ----------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        timer_sec = LONG_BREAK_MIN * 60
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        timer_sec = SHORT_BREAK_MIN * 60
        timer_label.config(text="Break", fg=PINK)
    else:
        timer_sec = WORK_MIN * 60
        timer_label.config(text="Work", fg=GREEN)

    start_button["state"] = "disabled"
    count_down(timer_sec)

# ---------------------------- COUNTDOWN MECHANISM--------------------------- # 
def count_down(count):
    count_min, count_sec = divmod(count, 60)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02d}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = (reps // 2) * "✔"
        mark_label.config(text= marks)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW,)

# Canvas config
canvas = tk.Canvas(width=200, height=234, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 140, text="00:00", fill="white",
    font=(FONT_NAME, 28, "bold")
    )
canvas.grid(column=1, row=1)

# Labels and buttons:
reset_button = tk.Button(
    text="Reset", command=reset, bg=PINK, activebackground=RED
    )

start_button = tk.Button(
    text="Start", command=start_timer, bg=PINK, activebackground=RED
    )

timer_label = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35), bg=YELLOW)

mark_label = tk.Label(fg=GREEN, font=(FONT_NAME, 25), bg=YELLOW)

# positioning
reset_button.grid(column=2, row=2)
start_button.grid(column=0, row=2)
timer_label.grid(column=1, row=0)
mark_label.grid(column=1, row=3)






window.mainloop()