from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
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
    website = website_input.get().lower()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="warning", message="Please fill out empty fields")
    else:

        try:
            with open("data.json", "r") as my_file:
                #Reading old data
                data = json.load(my_file)
        except FileNotFoundError:
            with open("data.json", "w") as my_file:
                json.dump(new_data, my_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as my_file:
                json.dump(data, my_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    print("find password is clicked")
    website = website_input.get().lower()
    print(website)
    try:
        with open("data.json", "r") as my_file:
            data = json.load(my_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_img)
canvas.grid(column=1, row=0)

#WEBSITE
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

#EMAIL/USERNAME
email_or_username_label = Label(text="Email/Username:")
email_or_username_label.grid(column=0, row=2)
email_username_input = Entry(width=36)
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
add_button = Button(text="Add", width=37, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()