import time
from tkinter import *
canvas = Tk()
canvas.title("Digital Clock")
label = Label(canvas, font=("ds-digital", 120, 'bold'), bg="black", fg="darkgreen", bd=10)
label.pack(anchor='center')
label.grid(row=0, column=1)


def digitalclock():
    text_input = time.strftime("%H:%M:%S")
    label.config(text=text_input)
    label.after(200, digitalclock)


digitalclock()
canvas.mainloop()
