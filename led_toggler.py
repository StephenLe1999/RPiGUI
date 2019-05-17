from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

Green = LED(14)
Blue = LED(15)
Red = LED(18)

win = Tk()
win.title("Led Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

def GreenToggle():
    if Green.is_lit:
        Green.off()
        GreenButton["text"] = "Turn Green LED on"
    else:
        Green.on()
        GreenButton["text"] = "Turn Green LED off"

def BlueToggle():
    if Blue.is_lit:
        Blue.off()
        BlueButton["text"] = "Turn Yellow LED on"
    else:
        Blue.on()
        BlueButton["text"] = "Turn Yellow LED off"
        
def RedToggle():
    if Red.is_lit:
        Red.off()
        RedButton["text"] = "Turn Red LED on"
    else:
        Red.on()
        RedButton["text"] = "Turn Red LED off"

def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
GreenButton = Button(win, text = 'Turn Green LED On', font = myFont, command = GreenToggle, bg = 'yellow', height = 1, width = 24)
GreenButton.grid(row = 0, column = 1)

BlueButton = Button(win, text = 'Turn Yellow LED On', font = myFont, command = BlueToggle, bg = 'yellow', height = 1, width = 24)
BlueButton.grid(row = 0, column = 2)

RedButton = Button(win, text = 'Turn Red LED On', font = myFont, command = RedToggle, bg = 'yellow', height = 1, width = 24)
RedButton.grid(row = 0, column = 3)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row = 2, column = 2)

win.protocol("WM DELETE WINDOW", close)

win.mainloop()
