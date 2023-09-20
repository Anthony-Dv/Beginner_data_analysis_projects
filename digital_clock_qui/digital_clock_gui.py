# This is digital clock that displays current time with milisecond precision


# Import required libraries
from tkinter import Label, Tk
from datetime import datetime

# Set the basic parameters of the gui
app_window = Tk()
app_window.title("My digital clock")
app_window.geometry("600x150")
app_window.resizable(1,1)

# Define parameters of the digital clock
text_font = ("Boulder", 40, "bold")
background = "#308BD6"
foreground = "#EAF41F"
border_width = 54

label = Label(app_window, font = text_font, bg = background, fg = foreground, bd = border_width)
label.grid(row = 0, column = 1)

# Define digital_clock func
def digital_clock():
    live_time = datetime.now().strftime('%Y-%d-%m %H:%M:%S.%f')[:-4]
    label.config(text = live_time)
    label.after(20, digital_clock)

digital_clock()
app_window.mainloop()

