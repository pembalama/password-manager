from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pw_letter = [random.choice(letters) for _ in range(nr_letters)]
    pw_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pw_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = pw_letter + pw_symbols + pw_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    print("ADD button is clicked")
    website_value = website_input.get()
    email_password_value = email_username_input.get()
    password_value = password_input.get()

    if len(website_value) == 0 or len(password_value) == 0:
        messagebox.showinfo(title="warning", message="Please fill out empty fields")
    else:
        is_ok = messagebox.askokcancel(title=website_value, message=f"Here are the details:\nWebsite: {website_value}\n"
                                                              f"Email: {email_password_value}\nPassword: {password_value}")

        if is_ok:
            with open("data.txt", "a") as my_file:
                my_file.write(f"{website_value} | {email_password_value} | {password_value}\n")
                website_input.delete(0, 'end')
                password_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_img)
canvas.grid(column=1, row=0)

#WEBSITE
website = Label(text="Website:")
website.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

#EMAIL/USERNAME
email_or_username = Label(text="Email/Username:")
email_or_username.grid(column=0, row=2)
email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "lama@gmail.com")

#PASSWORD
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

#BUTTONS
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()