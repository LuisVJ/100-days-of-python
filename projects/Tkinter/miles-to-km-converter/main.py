import tkinter as tk

window = tk.Tk()
window.title("Miles to Km converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

# create input
input = tk.Entry(width=10)
input.grid(column=1, row=0)
# create 4 text labels
label_miles = tk.Label(text="Miles")
label_miles.grid(column=2, row=0)

label_km = tk.Label(text="Km")
label_km.grid(column=2, row=1)

label_equal = tk.Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_result = tk.Label(text="0")
label_result.grid(column=1, row=1)

# calculate button
def calculate():
    km = round(int(input.get()) * 1.61, 2)
    label_result["text"] = km
    pass

button = tk.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()