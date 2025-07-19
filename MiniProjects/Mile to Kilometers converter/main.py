from tkinter import *

def calculate_conversion():
    miles = miles_text.get()
    kilometers = int(miles) * 1.609
    kilometer_label.config(text=round(kilometers, 3))

kilometer = 0

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

first_coords = Label(text=" ")
first_coords.grid(row=0, column=0)

equals_label = Label(text=f"is equal to")
equals_label.grid(row=1, column=0)

kilometer_label = Label(text="0")
kilometer_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

miles_text = Entry(width=10)
miles_text.grid(row=0, column=1)

m_label = Label(text="Miles")
m_label.grid(column=2, row=0)

button = Button(text="Calculate", command=calculate_conversion)
button.grid(column=1, row=2)


window.mainloop()


