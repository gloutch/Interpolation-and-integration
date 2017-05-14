import tkinter
from tkinter import *

from interpolation_test import *
from airflow_test import *
from integration_test import *
from pressure_map_test import *

def callback():
    if askyesno('Avertissement','Etes vous sur de vouloir fermer le programme?'):
        showwarning('Yes','Fermeture du programme')
        fen.destroy()
            
def test_1():  
    file = v.get()
    display_interpolation(file)
 
def test_2(): 
    file = v.get()
    create_airflow_map(file)

def test_3():   
    test_length_curves()
    compare_integrate()
    test_derivative()
    test_integrate()
    test_methode()

def test_4():
    file = v.get()   
    create_pressure_map(file)
    
fen=Tk()
fen.title("Launcher")
can=Canvas(fen, width=500, height=300, bg="white")
can.pack()
can.propagate(0)

FILES = [
    ("boe103", "model/boe103.txt"),
    ("HOR20", "model/HOR20.txt"),
    ("DU84132V", "model/DU84132V.txt"),
]

v = StringVar()
v.set("model/boe103.txt") # initialize

k = 0
for text, mode in FILES:
    k = k + 100
    b = Radiobutton(can, text=text, variable=v, value=mode)
    b.pack(anchor=W)
    b.place(x=k, y=10)
        
B1=Button(can,text="Test interpolation",fg="orange",command=test_1)
B1.pack()
B1.place(x=190, y=50)

B2=Button(can,text="Test airflow",fg="orange",command=test_2)
B2.pack()
B2.place(x=210, y=100)
     
B3=Button(can,text="Test integration",fg="orange",command=test_3)
B3.pack()
B3.place(x=195, y=150)

B4=Button(can,text="Test pressure map",fg="orange",command=test_4)
B4.pack()
B4.place(x=185, y=200)

fen.mainloop()