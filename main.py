# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
from tkinter.ttk import Progressbar
from tkinter import Menu
import time
window = Tk()         # Create the application window
window.title("Welcome")
window.geometry('350x200')
# Add a label with the text "Hello"
lbl = Label(window, text="Hello, prepare to be processed. Please, do not resist.", font=("Comic Sans", 50))
# Place the label in the window at 0, 0
lbl.grid(column=0, row=0)
seclbl = Label(window, text="Your contributions are apreciated.", font=("Comic Sans", 20))
seclbl.grid(column=0, row=1)
clicks = 0
time = 0

def clicked():
    global clicks
    clicks = clicks + 1
    trelbl = Label(window, text=clicks)
    trelbl.grid(column=0, row=5)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
#secbtn = Button(window, text="Click Me Too")
#secbtn.grid(column=1, row=0)
txt = Entry(window, width=10)
txt.grid(column=0, row=2)
chk = Checkbutton(window, text="Choose")
chk.grid(column=0, row=3)
bar = Progressbar(window, length=200)
bar['value'] = 5
bar.grid(column=1, row=2)
menu = Menu(window)
window.config(menu=menu)
new_item = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Fresh')
menu.add_cascade(label='Look Here', menu=new_item)
window.config(menu=menu)
window.mainloop()     # Keep the window open
