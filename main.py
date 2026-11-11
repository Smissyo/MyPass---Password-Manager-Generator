from tkinter import *
from tkinter import messagebox
import random
import pyperclip


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

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    print(f"Your password is: {password}")
    pass_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=web_entry.get()
    email=email_entry.get()
    password=pass_entry.get()
    if len(website)==0 or len(password)==0:
        messagebox.showerror("Error","Please enter all required fields")
    else:
        is_ok=messagebox.askokcancel(title=website, message=f"Details entered:\nEmail:{email}\nPassword:{password}\nIs it okay to save?")
        if is_ok:
            with open("data.txt",'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvas=Canvas(window, width=200, height=200)
img=PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0,column=1)

web_label=Label(text="Website:", font=("Aerial", 12))
web_label.grid(row=1,column=0)

email_label=Label(text="Email/Username:", font=("Aerial", 12))
email_label.grid(row=2,column=0)

pass_label=Label(text="Password:", font=("Aerial", 12))
pass_label.grid(row=3,column=0)

web_entry=Entry(width=40)
web_entry.grid(row=1,column=1, columnspan=2)
web_entry.focus()

email_entry=Entry(width=40)
email_entry.grid(row=2,column=1, columnspan=2)
email_entry.insert(0,"smita@gmail.com")

pass_entry=Entry(width=21)
pass_entry.grid(row=3,column=1)

gen_button=Button(text="Generate Password", command=generate_password)
gen_button.grid(row=3,column=2)

add_button=Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()