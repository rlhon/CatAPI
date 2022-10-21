import tkinter as tk
from tkinter import ttk
from tkinter import *
from cat_facts import *
import requests
import json
from PIL import Image, ImageTk

def displayText() :
    f = requestFact()
    T.delete("1.0", tk.END)
    T.insert(tk.END, f)

window = tk.Tk()
window.geometry('400x300')
window.resizable(False,False)

T = Text(window, height = 10, width = 40)

l = Label(window, text = "Fact")

cat = Image.open("cat.jpg")
cat1 = cat.resize((50,50))
catpic = ImageTk.PhotoImage(cat1)
#catpic = cat1.subsample(50,50)

button = ttk.Button(
    window, 
    image = catpic,
    text = "Click for a Cat Fact ",
    compound = tk.LEFT,
    command = displayText
)

l.pack()
T.pack()
button.pack(expand= True)
displayText()

window.mainloop()


