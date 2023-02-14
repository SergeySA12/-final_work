from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, askopenfile

file_name = None

def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)

root = Tk()
root.title("Заметки")
root.geometry("400x400")

menu_bar = Menu(root)
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Файл", menu=file_menu)

text = Text(root, width=400, height=400)
text.pack()

root.config(menu=menu_bar)
root.mainloop()