# A starter program for Python with Tkinter
from tkinter import * # import Tkinter library
import tkinter as tk
import tkinter as Tkinter 
from tkinter.ttk import Progressbar
from tkinter import Menu
import time
from tkinter.ttk import *
from ttkthemes import ThemedTk

window = ThemedTk(theme="aquavito")         # Create the application window

window.title("Welcome")
window.geometry('350x200')
# Add a label with the text "Hello"
lbl = Label(window, text="Hello, prepare to be processed. Please, do not resist.", font=("Comic Sans", 50))
# Place the label in the window at 0, 0
lbl.grid(column=0, row=0)
seclbl = Label(window, text="Your contributions are apreciated.", font=("Comic Sans", 20))
seclbl.grid(column=0, row=1)
clicks = 0
def clicked():
    global clicks
    clicks = clicks + 1
    trelbl = Label(window, text=clicks)
    trelbl.grid(column=0, row=5)
    bar = Progressbar(window, length=200)
    bar['value'] = clicks
    bar.grid(column=1, row=2)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
#secbtn = Button(window, text="Click Me Too")
#secbtn.grid(column=1, row=0)
txt = Entry(window, width=10)
txt.grid(column=0, row=2)
chk = Checkbutton(window, text="Choose")
chk.grid(column=0, row=3)
menu = Menu(window)
window.config(menu=menu)
new_item = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Fresh')
menu.add_cascade(label='Look Here', menu=new_item)
window.config(menu=menu)
counter = -1
running = False
def counter_label(label): 
	def count(): 
		if running: 
			global counter 

			# To manage the intial delay. 
			if counter==-1:			 
				display="Starting..."
			else: 
				display=str(counter) 

			label['text']=display # Or label.config(text=display) 
 
			label.after(1000, count) 
			counter += 1

	# Triggering the start of the counter. 
	count()	 

# start function of the stopwatch 
def Start(label): 
	global running 
	running=True
	counter_label(label) 
	start['state']='disabled'
	stop['state']='normal'
	reset['state']='normal'

# Stop function of the stopwatch 
def Stop(): 
	global running 
	start['state']='normal'
	stop['state']='disabled'
	reset['state']='normal'
	running = False

# Reset function of the stopwatch 
def Reset(label): 
	global counter 
	counter=-1

	# If rest is pressed after pressing stop. 
	if running==False:	 
		reset['state']='disabled'
		label['text']='Welcome!'

	# If reset is pressed while the stopwatch is running. 
	else:			 
		label['text']='Starting...'
label = Tkinter.Label(window, text="Welcome!", fg="black", font="Verdana 30 bold")
label.grid(column=0, row=8)
start = Tkinter.Button(window, text='Start', 
width=15, command=lambda:Start(label)) 
stop = Tkinter.Button(window, text='Stop', 
width=15, state='disabled', command=Stop) 
reset = Tkinter.Button(window, text='Reset', 
width=15, state='disabled', command=lambda:Reset(label)) 
start.grid(column=0, row=9) 
stop.grid(column=0, row=10)
reset.grid(column=0, row=11)

window.mainloop()     # Keep the window open

