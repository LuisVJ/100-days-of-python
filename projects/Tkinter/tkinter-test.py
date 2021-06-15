import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

my_label = tkinter.Label(text="A label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0) # precise positioning if we use place(x=, y= )

my_label["text"] = "New Text"

# Button

def button_clicked():
    my_label["text"] = input.get()



button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1) # pack() centers the label in the window

# Entry

input = tkinter.Entry()
input.grid(column=3, row=2)

button2 = tkinter.Button(text="button2")
button2.grid(column=2, row=0)





window.mainloop()