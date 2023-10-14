import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, f"{password}")
    pyperclip.copy(f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().capitalize()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(website) != 0 and len(username) != 0 and len(password) != 0:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Writing to newly created json file
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving Updated Data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please do not field(s) empty.")


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search():
    website = website_input.get().capitalize()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=f"{website}", message=f"No details for {website} exist.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# input
website_input = Entry(width=25)
website_input.grid(row=1, column=1)
username_input = Entry(width=44)
username_input.insert(0, "desoyedami@gmail.com")
username_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=25)
password_input.grid(row=3, column=1)

# Button
search_btn = Button(text="Search", width=15, command=search)
search_btn.grid(row=1, column=2)
generate_btn = Button(text="Generate Password", width=15, command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=41, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
