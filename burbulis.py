#mērķis ir uztaisīt programmu, kurā zemūdene spridzina burbuļus
#tiek skaitīti punkti

from tkinter import *
from random import *
from math import *

logs = Tk()
garums = 750
platums = 750
logs.title("Burbuļu spridzinātājs")
a = Canvas(logs, width=platums, height=garums, bg='#DBC4F0')
a.pack()
#kugaID =a.create_polygon(0, 0, 80, 80, outline='#776D8A', width=5)
kugaID2 =a.create_oval(0, 0, 80, 80, outline='#776D8A', width=5)



mainloop()
