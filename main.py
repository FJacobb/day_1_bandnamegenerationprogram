from tkinter import *
from tkinter import messagebox
from time import sleep
import tkinter
def message():
    messagebox.showinfo("Band Name", message=f"your band name could be '{name_city_input.get()} {name_pet_input.get()}'")
def next ():
    global name_city_input, name_pet_input
    loading_page.destroy()
    name_city = Label(home, text="What's name of the city you grew up in?", font=("arel", 9, "bold"), fg="#000000")
    name_city.place(x=20, y=40)
    name_city_input = Entry(home, width=28, fg="#000000", font=("arel", 9, "normal") )
    name_city_input.place(x=20,y=60 )
    name_pet = Label(home, text="What's your pet's  name?", font=('arel', 9, "bold"), fg="#000000")
    name_pet.place(x=20, y=100)
    name_pet_input = Entry(home, width=28, fg="#000000", font=("arel", 9, "normal"))
    name_pet_input.place(x=20, y=130)
    Button(home, text="submit", fg="black", font=("arel", 10, "bold"), command=message).place(x=200, y=170)

home = Tk()
home.title("Band name generator")
home.geometry("425x250")
loading_page = Button(home, text="Welcome to Band Name Generator", font=("arel", 13, "normal"), fg="#000000", command=next)
loading_page.place(x=80,y=100)
home.mainloop()
