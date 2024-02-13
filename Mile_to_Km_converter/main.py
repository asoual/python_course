from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width= 180, height=100)
window.config(padx=20, pady=20)
#Entries
entry = Entry(width=10)
print(entry.get())
entry.grid(column=1, row=0)

#Labels
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)
result_label = Label(text="0")
result_label.grid(column=1, row=1)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

#Buttons
def calculate():
    miles = entry.get()
    km = float(miles) * 1.609
    result_label.config(text=km)
    
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)



window.mainloop()