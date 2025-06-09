#  TKinter module 
# GUI- Graphical User Interface 

import tkinter
# tinker module , tk class
window=tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500,height=300)

# While woriking with tkinter you create it then specify how that label is going to look by calling it with pack() 

my_label=tkinter.Label(text="Hi I'm so hungry",font=("Arial", 24))
my_label.pack()

window.mainloop()
# pack willplace it into the screen at the center 



