import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import Combobox
from PIL import Image, ImageTk


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
heart_background = Label(image=heart, borderwidth=0, highlightthickness=0)
heart_background.place(x=940, y=10)

title = PhotoImage(file="title.png")
title_background = Label(image=title, borderwidth=0, highlightthickness=0)
title_background.place(x=40, y=10)

detail_entry = Frame(root, width=750, height=400, bg='#a6a6a6', bd=1)
detail_entry.place(x=100, y=200)

Label(detail_entry, text="Do you have hypertension?", font="halvetica 13", bg=framebg, fg='white').place(x=60, y=30)
Label(detail_entry, text="Do you have heart disease?", font="halvetica 13", bg=framebg, fg='white').place(x=60, y=70)
Label(detail_entry, text="Have you ever been married?", font="halvetica 13", bg=framebg, fg='white').place(x=60, y=110)


def selection():
    if hypertenstion.get() == 1:
        hyp = 1
        return hyp
    elif hypertenstion.get() == 2:
        hyp = 0
        return hyp


def selection2():
    if heart_disease.get() == 1:
        dis = 1
        return (dis)
    elif heart_disease.get() == 2:
        dis = 0
        return (dis)


hypertenstion = IntVar()
R1 = Radiobutton(detail_entry, text='Yes', variable=hypertenstion, value=1, command=selection)
R2 = Radiobutton(detail_entry, text='No', variable=hypertenstion, value=2, command=selection)
R1.place(x=330, y=30)
R2.place(x=390, y=30)

heart_disease = IntVar()
R3 = Radiobutton(detail_entry, text='Yes', variable=heart_disease, value=1, command=selection)
R4 = Radiobutton(detail_entry, text='No', variable=heart_disease, value=2, command=selection)
R3.place(x=330, y=70)
R4.place(x=390, y=70)

ever_married = IntVar()
R3 = Radiobutton(detail_entry, text='Yes', variable=ever_married, value=1, command=selection)
R4 = Radiobutton(detail_entry, text='No', variable=ever_married, value=2, command=selection)
R3.place(x=330, y=110)
R4.place(x=390, y=110)


def selection5():
    input = gender_combobox.get()
    if input == "Male":
        return 0
    elif input == "Female":
        return 1
    elif input == "Other":
        return 2


Label(detail_entry, text="Gender", font='arial 13', bg=framebg, fg='white').place(x=60, y=150)
Label(detail_entry, text="Work type", font='arial 13', bg=framebg, fg='white').place(x=60, y=190)
Label(detail_entry, text="Residence type", font='arial 13', bg=framebg, fg='white').place(x=60, y=230)
Label(detail_entry, text="Smoking status", font='arial 13', bg=framebg, fg='white').place(x=60, y=270)

gender_combobox = Combobox(detail_entry, values=['Male', 'Female', 'Other'], font="arial 12", state="r", width=14)
work_combobox = Combobox(detail_entry, values=['Private', 'Self-employed', 'Government job', 'Childre',
                                               'Never worked'], font="arial 12", state="r", width=14)
residence_combobox = Combobox(detail_entry, values=['Urban', 'Rural'], font="arial 12", state="r", width=14)
smoking_combobox = Combobox(detail_entry, values=['smokes', 'never smoked', 'formerly smoke'], font="arial 12",
                            state="r", width=14)

gender_combobox.place(x=330, y=150)
work_combobox.place(x=330, y=190)
residence_combobox.place(x=330, y=230)
smoking_combobox.place(x=330, y=270)

Label(detail_entry, text="Age", font="arial 13", width=7, bg=framebg, fg='white').place(x=60, y=310)
Label(detail_entry, text="Average glucose level", font="arial 13", width=20, bg=framebg, fg='white').place(x=60, y=350)
Label(detail_entry, text="BMI", font="arial 13", width=7, bg=framebg, fg='white').place(x=590, y=30)

age = IntVar()
avg_g = StringVar()
bmi = StringVar()

age_entry = Entry(detail_entry, textvariable=age, width=10, font='arial 13', bg="#ededed", fg="#222222")
avg_g_entry = Entry(detail_entry, textvariable=avg_g, width=10, font='arial 12', bg="#ededed", fg="#222222")
bmi_entry = Entry(detail_entry, textvariable=bmi, width=11, font='arial 12', bg="#ededed", fg="#222222")

age_entry.place(x=330, y=310)
avg_g_entry.place(x=330, y=350)
bmi_entry.place(x=580, y=60)

def bmi():
    def calculate_bmi():
        weight = float(m.get())
        height = float(h.get())
        bmi_result = weight / (height / 100) ** 2
        b_label.config(text=f"BMI: {bmi_result:.2f}")

    Label(detail_entry, text="Weight", font="arial 11", width=7, bg='#94c3dd', fg='white').place(x=580, y=200)
    Label(detail_entry, text="Height", font="arial 11", width=7, bg='#94c3dd', fg='white').place(x=580, y=260)
    m = StringVar()
    h = StringVar()
    m_entry = Entry(detail_entry, textvariable=m, width=7, font='arial 13', bg="#ededed", fg="#222222")
    h_entry = Entry(detail_entry, textvariable=h, width=7, font='arial 12', bg="#ededed", fg="#222222")
    m_entry.place(x=580, y=230)
    h_entry.place(x=580, y=290)

    b_button = Button(detail_entry, text="Calculate BMI", command=calculate_bmi)
    b_button.place(x=580, y=330)
    b_label = Label(detail_entry, text="", font="arial 11", width=12, bg='#545454', fg='white')
    b_label.place(x=580, y=360)


bmi_button_image = Image.open("bmi.png")  # Ścieżka do obrazka przycisku
bmi_button_image = ImageTk.PhotoImage(bmi_button_image)
bmi_button = Button(detail_entry, image=bmi_button_image, command=bmi, borderwidth=0)
bmi_button.image = bmi_button_image
bmi_button.place(x=580, y=90)

root.mainloop()
