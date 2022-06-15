from tkinter import *
from time import *

def update():
    timeStr = strftime("%I:%M:%S %p")
    timeLabel.config(text=timeStr)

    dayLabel.config(text=strftime("%A"))

    dateLabel.config(text=strftime("%d %b %Y"))

    window.after(100, update) # we can also use timeLabel.after(1000, update) but it only update the time

window = Tk()

timeLabel = Label(window, font=("Arial", 50), fg="red", bg="black")
timeLabel.pack()

dayLabel = Label(window, font=("Lucida Handwriting", 30))
dayLabel.pack()

dateLabel = Label(window, font=("Algerian", 40), fg="#58a8a0")
dateLabel.pack()

update()

window.mainloop()
