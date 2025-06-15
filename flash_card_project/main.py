from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, background= BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
front_img= PhotoImage(file="images/card_front.png")
canvas.create_image(400, 226, image= front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel",40, "italic"))
canvas.create_text(400,263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(background= BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid (row=0, column=0, columnspan=2)


wrong_img= PhotoImage(file="images/wrong.png")
uknown_button=Button(image=wrong_img, highlightthickness=0)
uknown_button.grid(row=1,column=0)

right_img= PhotoImage(file="images/right.png")
known_button=Button(image=right_img,highlightthickness=0)
known_button.grid(row=1,column=1)

window.mainloop()

