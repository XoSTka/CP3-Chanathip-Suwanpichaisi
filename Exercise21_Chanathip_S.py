from tkinter import *
import math

def leftClickButton(event):
    print(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get())/100, 2))
    if float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2) >= 30.0:
        labelResult.configure(text="อ้วนมาก")
    elif 25 <= float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2) < 30.0:
        labelResult.configure(text="อ้วน")
    elif 23 <= float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2) < 25.0:
        labelResult.configure(text="น้ำหนักเกิน")
    elif 18.6 <= float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2) < 23.0:
        labelResult.configure(text="น้ำหนักปกติ")
    elif float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2) < 18.6:
        labelResult.configure(text="ผอมเกินไป")
    else:
        labelResult.configure(text="Error")

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow, text="คำนวณ")
calculateButton.bind("<Button-1>", leftClickButton)
calculateButton.grid(row=2, column=0)
labelResult = Label(MainWindow, text="ผลลัพธ์")
labelResult.grid(row=2, column=1)

MainWindow.mainloop()