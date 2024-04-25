from tkinter import *
from random import choice, randint, shuffle
import tkinter.messagebox as messagebox
import pandas
FONT = ("Arial", 10)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    user_password = []

    user_password += [choice(letters) for i in range(randint(8, 10))]
    user_password += [choice(symbols) for j in range(randint(2, 4))]
    user_password += [choice(numbers) for k in range(randint(2, 4))]

    shuffle(user_password)
    password = "".join(user_password)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Error', message="Please make sure you don't leave any fields empty")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email} \nPassword: {password} \nIs it okay to save?")
        if is_okay:
            with open("data.txt", 'a') as data:
                data.write(f"{website} | {email} | {password} \n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

# Image
canvas = Canvas(height=200, width=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Label
website = Label(text="Website", font=FONT)
website.grid(row=1, column=0)

email = Label(text="Email/Username", font=FONT)
email.grid(row=2, column=0)

password = Label(text="Password", font=FONT)
password.grid(row=3, column=0)

# Input
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'tebogosekhula@gmail.com')
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

# Button
generate_button = Button(text="Generate Password", font=FONT, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add",width=52 ,font=FONT, command=save)
add_button.grid(row=4, column=0, columnspan=3)


mainloop()
