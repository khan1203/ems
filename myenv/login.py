from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', "All fields are required.")
    elif usernameEntry.get()=='khan1203' and passwordEntry.get()=='1203':
        messagebox.showinfo('success', "Successfully Logged in")
        root.destroy()
        import ems
    else:
        messagebox.showwarning('Error', "Wrong Credentials")

root = CTk()
root.geometry('930x473')
root.resizable(0,0)

root.title("Login Page")

image = CTkImage(Image.open('login1.jpg'), size=(930, 478))
imageLabel = CTkLabel(root, image=image, text='')
imageLabel.place(x=0, y=0)

headingLabel = CTkLabel(root, text='Employee Management System', font=('Goudy Old Style', 20,'bold'))
headingLabel.place(x=30, y=30)

usernameEntry = CTkEntry(root, placeholder_text='Enter Your Username', width=180)
usernameEntry.place(x=700, y=250)

passwordEntry = CTkEntry(root, placeholder_text='Enter Your Password', width=180, show='*')
passwordEntry.place(x=700, y=300)

loginButton = CTkButton(root, text='Login',cursor='hand2', command=login)
loginButton.place(x=720, y=350)

root.mainloop()