from tkinter import *
from tkinter import messagebox
import PasswordGenerator
import pyperclip

#SAVING TO A FILE
def save_to_file():

    website = website_entry.get()
    email_user = email_user_entry.get()
    password = password_entry.get()

    if len(website) != 0 or len(password) != 0:
        is_okay = messagebox.askyesno('Confirmation', 'Are you sure?')

        if is_okay:
            with open("data.txt", "a") as file:
                file.writelines(f"{website} | {email_user} | {password}\n")
            pyperclip.copy(password)
            website_entry.delete(0, END)
            password_entry.delete(0, END)

            messagebox.showinfo('Success', 'Password has been saved successfully')
    else:
        messagebox.showinfo('Invalid entry', "Your email or password field is empty. Please input an email"
                                             " or password")
def gen_password():
    generated_password = PasswordGenerator.generate_password()
    password_entry.insert(END, generated_password)


#USER INTERFACE
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_user_label = Label(text="Email/Username: ")
email_user_label.grid(column=0, row=2)

email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "example@email.com")
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, ipadx=0)

generate_button = Button(text="Generate", height=1, command=gen_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save_to_file)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()