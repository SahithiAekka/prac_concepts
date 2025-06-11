from tkinter import *
 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Lables 
website_lable=Label(text="Website:")
website_lable.grid(row=1, column=0)
email_lable=Label(text="Email/Username:")
email_lable.grid(row=2, column=0)
password_lable=Label(text="Password:")
password_lable.grid(row=3, column=0)

# Entreis 
website_entry=Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2 )

email_entry=Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry=Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
genertae_password_button=Button(text="Generate Password")
genertae_password_button.grid(row=3, column=2)

add_button = Button(text="Add",  width= 36)
add_button.grid(row=4, column=1,columnspan=2)




window.mainloop()
