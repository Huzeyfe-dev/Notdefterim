import tkinter as t
from tkinter import filedialog as fd


türler=(
    ("tüm dosyalar", "*.*"),
    ("python dosyası", "*.py"),
    ("c dosyası", "*.c"),
    ("c başlık dosyası","*.h"))

dosya_adı=""

def kaydet():
    global dosya_adı
    if dosya_adı=="":
        dosya_adı = fd.asksaveasfilename(filetypes=türler)

    with open(dosya_adı, "w") as f:
        yazı = text.get("1.0",t.END)
        f.write(yazı)

def aç():
    global dosya_adı
    dosya_adı = fd.askopenfilename(filetypes = türler)

    with open(dosya_adı, "r") as f:
        yazı = f.read()

    text.delete(1.0, t.END)
    text.insert(t.END, yazı)

def yeni():
    global dosya_adı

    kaydet()

    dosya_adı=""

    text.delete(1.0, t.END)

def siyah():
    global text
    text["bg"]="black"
    text["fg"]="white"

def beyaz():
    global text
    text["bg"]="white"
    text["fg"]="black"

pn = t.Tk();

menu = t.Menu()
dosya_menu = t.Menu(menu, tearoff=0)
dosya_menu.add_command(label="Aç", command=aç)
dosya_menu.add_command(label="Yeni", command=yeni)
renk_menu=t.Menu(menu, tearoff=0)
renk_menu.add_command(label="Siyah", command=siyah)
renk_menu.add_command(label="Beyaz", command=beyaz)
menu.add_command(label="Kaydet", command=kaydet)
menu.add_cascade(label="Dosya", menu=dosya_menu)
menu.add_cascade(label="Renk", menu=renk_menu)


text = t.Text(pn)
text.grid(row=0, column=0)

pn.config(menu=menu)




pn.mainloop()