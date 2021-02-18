from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

def calc_km():
    result_label['text'] = f'{float(input.get()) * 1.60934}'
# Labels
km_label = Label(text="Km", font=("Arial", 14, "normal"))
km_label.grid(column=2, row=1)
result_label = Label(text="0", font=("Arial", 14, "normal"))
result_label.grid(column=1, row=1)
equal_label = Label(text='Is equal to', font=("Arial", 14, "normal"))
equal_label.grid(column=0, row=1)
miles_label = Label(text="Miles", font=("Arial", 14, "normal"))
miles_label.grid(column=2, row=0)
# Button
button = Button(text='Calculate',command= calc_km)
button.grid(column=1, row=3)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()
