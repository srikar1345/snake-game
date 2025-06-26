from tkinter import *

window=Tk()
window.title("pomodoro")
window.config(padx=100,pady=50)

canvas=Canvas(width=200,height=224)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(103,112,image=tomato)
canvas.create_text(103,138,text="00:00",fill="white",font=())
canvas.pack()











window.mainloop()