from customtkinter import *
from PIL import Image

window = CTk()

window.geometry('930x580')
window.resizable(False, False)

window.title("Employee Management System")
logo = CTkImage(Image.open('login1.jpg'), size=(930,158))
logoLabel = CTkLabel(window, image=logo, text='')
logoLabel.grid(row=0,column=0, columnspan=2, pady=40)  # logoLabel.place(x=0, y=0)

#------------------Left Frame---------------------
leftFrame = CTkFrame(window)
leftFrame.grid(row=1, column=0)

idLabel= CTkLabel(leftFrame, text="Id: ", font=('arial', 18, 'bold'))
idLabel.grid(row=0, column=0, padx=10)

idEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
idEntry.grid(row=0, column=1, pady=10)

nameLabel= CTkLabel(leftFrame, text="Name: ", font=('arial', 18, 'bold'))
nameLabel.grid(row=1, column=0, padx=10)

nameEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
nameEntry.grid(row=1, column=1, pady=10)

PasswordLabel= CTkLabel(leftFrame, text="Password: ", font=('arial', 18, 'bold'))
PasswordLabel.grid(row=2, column=0,padx=10)

passEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
passEntry.grid(row=2, column=1, pady=10)

salaryLabel= CTkLabel(leftFrame, text="Salary: ", font=('arial', 18, 'bold'))
salaryLabel.grid(row=3, column=0,padx=10)

salaryEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
salaryEntry.grid(row=3, column=1, pady=10)



#-------------------Right Frame-------------------------
rightFrame = CTkFrame(window)
rightFrame.grid(row=1, column=1)



window.mainloop()

