from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = None

def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)

def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Упс!, нельзя сохранить файл")

def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return
        file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)

root = Tk()
#З аголовок.
root.title("Заметки")
root.geometry("400x400")


menu_bar = Menu(root)
file_menu = Menu(menu_bar)

file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить как", command=save_as)

# Создание кнопки.
menu_bar.add_cascade(label="Файл", menu=file_menu)

# Создание размеров техтового файла.
text = Text(root,
            width=400,
            height=400,
            background="Grey",
            fg='Blue',
            wrap=WORD,
            insertbackground='brown',
            selectbackground='#2F4F4F')
text.pack(expand=1, fill=BOTH, side=LEFT)

#Скрол текста.
scroll = Scrollbar(text, command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scroll.set)


root.config(menu=menu_bar)
root.mainloop()