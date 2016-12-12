#   Copyright 2015 David Crespo Romero
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from tkinter import *
   
# formula

def results():
    finallevel = Toplevel()
    finallevel.title('Results')
    finallevel.geometry("150x50")
    finallevel.configure(background="black")
    try:
        solution = (float(vin.get())* (float(r2.get())/ (float(r1.get())+ float(r2.get()))))
        r = Label (finallevel, width=20, bg="black", fg="red", text="{0:.2} Volts".format(solution))
        r.pack()
    except:
        r = Label (finallevel, width=20, bg="black", fg="red", text="Division by zero.\n Adjust Values.")
        r.pack()

# New window with info

def about():
    toplevel = Toplevel()
    toplevel.title('About')
    toplevel.focus_set()
    w = Label(toplevel, text = "Copyright 2015 David Crespo Romero")
    w.pack()
    w = Label(toplevel, text = "This program is free software: you can redistribute it and/or modify")
    w.pack()
    w = Label(toplevel, text = "it under the terms of the GNU General Public License as published by")
    w.pack()
    w = Label(toplevel, text = "the Free Software Foundation, either version 3 of the License, or")
    w.pack()
    w = Label(toplevel, text = "(at your option) any later version.")
    w.pack()
    w = Label(toplevel, text = " ")
    w.pack()
    w = Label(toplevel, text = "This program is distributed in the hope that it will be useful,")
    w.pack()
    w = Label(toplevel, text = "but WITHOUT ANY WARRANTY; without even the implied warranty of")
    w.pack()
    w = Label(toplevel, text = "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the")
    w.pack()
    w = Label(toplevel, text = "GNU General Public License for more details.")
    w.pack()
    w = Label(toplevel, text = " ")
    w.pack()
    w = Label(toplevel, text = "You should have received a copy of the GNU General Public License")
    w.pack()
    w = Label(toplevel, text = "along with this program.  If not, see <http://www.gnu.org/licenses/>.")
    w.pack()

# Set the windows and many variables

finestra = Tk()
finestra.wm_title("divisor")
finestra.configure(bg="black")

vin = DoubleVar()
r1 = DoubleVar()
r2 = DoubleVar()

# tell me things about what you know and want to do

etiqueta1 = Label(finestra, bg="black", fg="red", text="Insert Vin")
etiqueta1.pack()
entrada1=Entry(finestra, highlightbackground="black", bg="red", fg="black", textvar=vin).pack()

etiqueta2 = Label(finestra, bg="black", fg="red", text="Insert R1 value")
etiqueta2.pack()
entrada2=Entry(finestra, highlightbackground="black", bg="red", fg="black", textvar=r1).pack()

etiqueta3 = Label(finestra, bg="black", fg="red", text="Insert R2 value")
etiqueta3.pack()
entrada3=Entry(finestra, highlightbackground="black", bg="red", fg="black", textvar=r2).pack()

# Oh!! It's a button!!

boton1=Button(finestra, activebackground="red", bg="black", fg="red", text="Calculate", command=results)
boton1.config(highlightbackground="black")
boton1.pack(side=RIGHT)

# A new button for information

boton2=Button(finestra, activebackground="red", bg="black", fg="red", text="About", command=about)
boton2.config(highlightbackground="black")
boton2.pack(side=RIGHT)

# Loop
mainloop( )
