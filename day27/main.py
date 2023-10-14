from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

equal_to = Label(text="is equal to")
equal_to.grid(row=1, column=0)
equal_to.config(padx=5, pady=5)

input = Entry(width=10)
input.grid(row=0, column=1)


miles = Label(text="miles")
miles.grid(row=0, column=2)
miles.config(padx=5, pady=5)


def calculate():
    kilometer = float(int(input.get()) / 0.6214)
    calculated_km.config(text=round(kilometer))
    input.delete(0, END)
    return kilometer


calculated_km = Label(text=0)
calculated_km.grid(row=1, column=1)
calculated_km.config(padx=5, pady=5)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)
button.config(padx=5, pady=5)

km = Label(text="km")
km.grid(row=1, column=2)
km.config(padx=5, pady=5)

window.mainloop()
