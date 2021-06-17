import tkinter as tk
from tkinter.constants import END
from tkinter import messagebox
import csv
import random

# --------------------------- PASSWORD GENERATOR ----------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= random.randint(8, 10) 
    nr_symbols = random.randint(2, 4) 
    nr_numbers = random.randint(2, 4) 

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list) 

    new_password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(END, new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(site) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="you have empty fields")
    else:
        is_ok = messagebox.askokcancel(
            title=site,
            message=f"These are the details entered: \nEmail: {email}"
                    f"\nPassword: {password} \nIs it ok to save?"
            )

        if is_ok:
            with open("data.csv", "a") as data:
                csv_writer = csv.writer(data)
                csv_writer.writerow([site, email, password])
            
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

# Labels and input
website_label = tk.Label(text="Website:")
website_input = tk.Entry(width=35)
email_label = tk.Label(text="Email/Username:")
email_input = tk.Entry(width=35)
password_label = tk.Label(text="Password:")
password_input = tk.Entry()
generate_button = tk.Button(text="Generate Password", font=("Arial", 10), command=generate)
add_button = tk.Button(text="Add", command=save)

website_input.focus()
email_input.insert(END, "myEmail@email.com")

# positioning
canvas.grid(column=1, row=0)
website_label.grid(column=0,row=1, sticky="E")
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
email_label.grid(column=0, row=2, sticky="E")
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
password_label.grid(column=0, row=3, sticky="E")
password_input.grid(column=1, row=3, sticky="EW")
generate_button.grid(column=2, row=3, sticky="EW")
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()