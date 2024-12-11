from datetime import *
from math import *
from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
'''dy = datetime(2019,m1,d1)
    dy = dy.strftime("%x")
    with open("tft.txt", "w") as dt:
        for redak in dt:
            podaci += redak.splitlines()
    with open("archive.txt", "w") as dta:
        for i in range (len (podaci)):
            dta.write(END, podaci [i])'''
#=========.ulazna provjera.============
podaci = []
x = datetime.now()
d = int(x.strftime("%d"))
m = int(x.strftime("%m"))
with open ('datum.txt', 'r') as dt:
    d1 = int(dt.readline())
    m1 = int(dt.readline())
if d1-d != 0 or m1-m != 0:
    dy = datetime(2020,m1,d1)
    dy = dy.strftime("%x")
    with open("tft.txt", "r") as dt:
        for redak in dt:
            podaci += redak.splitlines()
    with open("archive.txt", "a") as dta:
        dta.write("\n")
        for i in range (len (podaci)):
            dta.write(podaci [i]+"\n")
        dta.write(dy+"\n")
    with open("datum.txt", "w") as datum:
        datum.write(str(d)+"\n")
        datum.write(str(m))
    with open('tft.txt', 'w') as bla:
        pass
    
#=========.komande.=============
def dodaj():
    temp = E3.get()
    if E3.get() == '':
        showwarning('\t'+'Oprez!', 'Niste unijeli sve vrijednosti')
    else:
        podaci.append(temp)
        L6.insert(END, temp)
        with open ('tft.txt', 'w')as dodat:  #otvaranje datoteke za pisanje
            dodat.write ('\n'.join(L6.get(0, END)))
        E3.delete(0, END)
        prosjek()
def arhiva():
    L6.delete(0, END)
    arhiva = []
    with open("archive.txt", "r") as arc:
        for redak in arc:
            arhiva += redak.splitlines()
        arhiva.reverse() #silazno prikazuje arhivu
        for i in range(len(arhiva)):
            L6.insert(i+1, arhiva [i])
def danas():
    L6.delete(0,END)
    danas = []
    with open("tft.txt", "r") as tft:
        for redak in tft:
            danas += redak.splitlines()
        for i in range (len (danas)):
            L6.insert(i + 1, danas [i])
def prosjek():
    broj = "1234567890"
    t = ""
    num =[]
    for b in range(len(L6.get(0, END))):
        for r in range(0, len(L6.get(b)), 1):
            if (L6.get(b))[r] in broj:
                t = t + (L6.get(b))[r]
        t = int(t)
        num.append(t)
        t = ""
    pros = round((sum(num) / len(num)),2)
    if pros == 0:
        L8 = Label(vp, text = "0.00"+"\t\t\t",bg = "sandybrown")
        L8.place(x=12, y=355)
    else:
        L8 = Label(vp, text = str(pros)+"\t\t",bg = "sandybrown")
        L8.place(x=12, y=355)
#=========.izgled.=============
baseY = 90
vp = Tk()
vp.config(bg = "sandybrown")
vp.geometry("315x500")
vp.title("TFT score")
vp.iconbitmap("tft.ico")
img = ImageTk.PhotoImage(Image.open("tft.jpg"))
slika_poz = Label(vp, image =  img)  #izbacuje error pa je comano
slika_poz.place(x=-2,y=-2)
L1 = Label(vp, text = 'Broj od 1 do 8:', bg = "navajowhite")
L1.place(x = 12, y =15+baseY)
E3 = Entry()
E3.place(x =112, y=15+baseY)
G1 = Button (vp, text = 'Dodaj',bg ="olivedrab", command = dodaj).place(x = 252, y=12+baseY)
G2 = Button (vp, text = 'Arhiva',bg ="olivedrab", command = arhiva).place(x = 202, y=330+baseY)
G3 = Button (vp, text = 'Danas',bg ="olivedrab", command = danas).place(x = 252, y=330+baseY)
F1 = Frame(vp, width = 285, height = 276).place(x = 15, y=45+baseY)
L6 = Listbox(vp, width = 35, height = 16)

klizac = Scrollbar (F1, orient=VERTICAL)
klizac.config(command=L6.yview, width = 16)
L6.config(font = 'System',selectmode = EXTENDED, yscrollcommand=klizac.set)
klizac.place(x = 282, y= 48+baseY)
L6.place(x = 15, y=45+baseY)
L7 = Label(vp, text = "Prosječan placemant:")
L7.config(bg = "navajowhite")
L7.place(x = 12, y=330+baseY)
LP = Label(vp, text = "© Zoltan Balko Macsai, 2024",bg = "sandybrown", fg = "white").place(x = 159,y=390+baseY)
podaci = []
broj = "1234567890"
with open ('tft.txt', 'r') as dat:        #otvori dat za citanje
    for redak in dat:
        podaci += redak.splitlines()
    for i in range (len (podaci)):
        L6.insert(i + 1, podaci [i])
broj = "1234567890"
t = ""
num =[]
for b in range(len(L6.get(0, END))):
    for r in range(0, len(L6.get(b)), 1):
        if (L6.get(b))[r] in broj:
            t = t + (L6.get(b))[r]
    t = int(t)
    num.append(t)
    t = ""
    pros = round((sum(num) / len(num)),2)
    if pros == 0:
        L8 = Label(vp, text = "0.00"+"\t\t\t",bg = "sandybrown")
        L8.place(x=12, y=355+baseY)
    else:
        L8 = Label(vp, text = str(pros)+"\t\t",bg = "sandybrown")
        L8.place(x=12, y=355+baseY)
vp.mainloop()
