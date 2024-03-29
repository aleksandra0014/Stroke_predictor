import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog


background = '#d9d9d9'
framebg = '#5d9ad8'
framefg = framebg

root = tk.Tk()
root.title("Stroke Predictor")
root.geometry("1450x730+60+80")

root.config(bg=background)
image_icon = PhotoImage(file='heart_maly.png')
root.iconphoto(False, image_icon)

heart = PhotoImage(file="heart_maly.png")
heart_background = Label(image=heart,borderwidth=0, highlightthickness=0)
heart_background.place(x=50, y=10)

title = PhotoImage(file="title.png")
title_background = Label(image=title, borderwidth=0, highlightthickness=0)
title_background.place(x=350, y=10)


root.mainloop()