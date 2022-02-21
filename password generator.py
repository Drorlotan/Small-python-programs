from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letters_pass = [random.choice(letters) for char in range(nr_letters)]
    symbols_pass = [random.choice(symbols) for char in range(nr_symbols)]
    numbers_pass = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = letters_pass + symbols_pass + numbers_pass
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_data():
    new_data = {
        website_entry.get(): {
            "email" : email_entry.get(),
            "password" : password_entry.get()
        }
    }


    if len(email_entry.get()) < 1 or len(password_entry.get()) < 1 or len(website_entry.get()) < 1:
        messagebox.showerror(title="Watch Out", message="please don't leave fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(),
                                       message=f"These are the details entered: \n "
                                               f"email: {email_entry.get()} \n "
                                               f"password: {password_entry.get()} \n is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data:
                    data_json = json.load(data)

            except FileNotFoundError:
                with open("data.json", "w") as data:
                    json.dump(new_data, data, indent=4)
            else:
                data_json.update(new_data)
                with open("data.json", "w") as data:
                    json.dump(data_json, data, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="No data", message="No passwords saved yet")
    else:
        if website_entry.get() in data:
            messagebox.showinfo(title=website_entry.get(), message=f"Email: {data[website_entry.get()]['email']} \n "
                                                             f"Password: {data[website_entry.get()]['password']}")
        else:
            messagebox.showerror(title=website_entry.get(), message="No password for this website.")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)
mail = Label(text="Email/Username:")
mail.grid(row=2, column=0)
password = Label(text="Password")
password.grid(row=3, column=0)

website_entry = Entry(width=39)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=39)
email_entry.insert(END, "dragondror@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

generate = Button(text="Generate Password", command=generate_password)
generate.grid(row=3, column=2)
add = Button(text="Add", width=33, command=add_to_data)
add.grid(row=4, column=1, columnspan=2)
search = Button(text="Search", command=find_password, width=13)
search.grid(row=1, column=2)
window.mainloop()
