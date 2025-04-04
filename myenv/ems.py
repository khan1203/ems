from customtkinter import *
from PIL import Image

window = CTk()

window.geometry('930x580')
window.resizable(False, False)

window.title("Employee Management System")
logo = CTkImage(Image.open('login1.jpg'), size=(930,158))
logoLabel = CTkLabel(window, image=logo, text='')
logoLabel.grid(row=0,column=0, columnspan=2)  # logoLabel.place(x=0, y=0)

#------------------Left Frame---------------------
leftFrame = CTkFrame(window)
leftFrame.grid(row=1, column=0)

idLabel= CTkLabel(leftFrame, text="Id: ", font=('arial', 18, 'bold'))
idLabel.grid(row=0, column=0,padx=20)

idEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
idEntry.grid(row=0, column=1)

nameLabel= CTkLabel(leftFrame, text="Id: ", font=('arial', 10, 'bold'), width=180)
nameLabel.grid(row=0, column=0,padx=20)

PasswordLabel= CTkLabel(leftFrame, text="Id: ", font=('arial', 10, 'bold'), width=180)
PasswordLabel.grid(row=0, column=0,padx=20)

salaryLabel= CTkLabel(leftFrame, text="Id: ", font=('arial', 10, 'bold'), width=180)
salaryLabel.grid(row=0, column=0,padx=20)





rightFrame = CTkFrame(window)
rightFrame.grid(row=1, column=1)



window.mainloop()

