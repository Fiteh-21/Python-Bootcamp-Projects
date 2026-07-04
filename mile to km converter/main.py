from tkinter import *

def calc():
    mile = float(user_mile.get())
    km = round(mile * 1.60934, 2)
    label_calc.config(text=km)

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

user_mile = Entry(width=7)
user_mile.grid(column=1, row=0)

label_mile = Label(text="Miles")
label_mile.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_calc = Label(text="0")
label_calc.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

button = Button(text="Calculate", command=calc)
button.grid(column=1, row=2)

window.mainloop()