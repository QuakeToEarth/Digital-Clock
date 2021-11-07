from tkinter import *
from tkinter.ttk import *
from time import strftime


def fetchtime():
    t = strftime('%H : %M : %S : %p')
    label.config(text=t)
    label.after(1000, fetchtime)


root = Tk()
root.title('Clock Window')
label = Label(root, font=('algerian-regular', 80),
              background='black', foreground='purple')
label.pack(anchor='center')
fetchtime()
root.mainloop()
