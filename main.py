from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def find_password():
    if len(website_input.get()) == 0:
        messagebox.showinfo(title="Oops",message="Fill in all required fields")
    else:
        try:
            with open("data.json", "r", encoding='utf-8') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error",message="Data not found")
        else:
            if website_input.get() in data:
                email = data[website_input.get()]["email"]
                password = data[website_input.get()]["password"]
                messagebox.showinfo(title="Result",message=f"Email: {email}\nPassword: {password}")
            elif website_input.get() not in data:
                messagebox.showinfo(title="Error", message="No details for that website exist")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    letters_list = [random.choice(letters) for char in range(nr_letters)]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    symbols_list = [random.choice(symbols) for char in range(nr_letters)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    numbers_list = [random.choice(numbers) for char in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = letters_list + numbers_list + symbols_list

    random.shuffle(password_list)

    password = "".join(password_list)

# password = ""
# for char in password_list:
#   password += char

    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }

    if len(password) == 0 or len(website) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops",message="Fill in all required fields")

    else:
            # is_ok = messagebox.askyesno(title="Title",
            #                             message=f"Website: {website_input.get()} \nEmail: {email_input.get()} "
            #                                     f"\nPassword: {password_input.get()} \nConfirm?")
        try:
            with open("data.json", "r", encoding='utf-8') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
            # file.write(f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n")
            # json.dump(new_data, data_file, indent=4)
            # Reading the old data
            # Updating old data with new data
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
            # Saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
            password_input.delete(0, 'end')
            website_input.delete(0, 'end')





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Pass")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200,highlightthickness=0)
app_image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=app_image)
canvas.grid(row=0,column=1)


website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

website_input = Entry(width=33)
website_input.grid(row=1,column=1)
website_input.focus()

search_button = Button(text="Search", width=14,command=find_password)
search_button.grid(row=1,column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

email_input = Entry(width=51)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"caspermuziri01@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

password_input = Entry(width=33)
password_input.grid(row=3,column=1)

generate_button = Button(text="Generate Password",command=generate_password, width=14)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add", width=43,command=save)
add_button.grid(row=4,column=1,columnspan=2)







window.mainloop()