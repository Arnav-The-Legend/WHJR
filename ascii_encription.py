from cgitb import text
from tkinter import *

def convertToASCII():
    label["text"] = ""
    input = enterWord.get()

    for letter in input:
        label["text"] += "Name Of ASCII: " + str(ord(letter)) 

root = Tk()
root.title("ASCII Encryption")

root.geometry("400x400")
root.configure(background = "white")

enterWord = Entry(root)
enterWord.place(anchor=CENTER, relx=0.5, rely=0.4)

label = Label(root, text="", bg= "snow", fg="black")
btn =Button(root, text="Show Me In ASCII!", command=convertToASCII, bg="yellow", fg="black")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()