from tkinter import *
import requests
import secondcode

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
canvas.grid(row=0, column=0)

def get_quote():
    k_quote = requests.get('https://api.kanye.rest')
    k_quote.raise_for_status()
    data = k_quote.json() 
    quote_data= data['quote']
    canvas.delete("kanyequote")
    quote_text = canvas.create_text(150, 207, text=quote_data, width=250, font=("Arial", 30, "bold"), fill="white", tags="kanyequote")
    print(quote_text)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

print(secondcode.get_apple("jatin"))
print(secondcode.apple)

window.mainloop()

print(secondcode.juice)