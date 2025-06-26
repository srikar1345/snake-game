from tkinter import *
def miles_to_km():
    miles=float(miles_input.get())
    km=miles*1.609
    kilometer_result_label.config(text=f"{km}")

window=Tk()
window.title("Miles to kilometer converter")
miles_input=Entry()
miles_input.grid(column=1,row=0)
miles_lable=Label(text="Miles")
miles_lable.grid(column=2,row=0)
is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

kilometer_result_label=Label(text="0")
kilometer_result_label.grid(column=1,row=1)
kilometer_label=Label(text="km")
kilometer_label.grid(column=2,row=1)
calculator_button=Button(text="Calculate",command=miles_to_km)

calculator_button.grid(column=1,row=2)




window.mainloop()



