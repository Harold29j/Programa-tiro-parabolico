import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtl
from tkinter import Tk, Frame, Button, Label, Entry, ttk, StringVar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

#Definimos los paramentros

grafica, ax = plt.subplots(facecolor='#05FFBF')
plt.title("Grafica de Movimiento Parabolico")

theta= np.pi/3
x0=0.
y0=0.
v0=30.
g=9.8

def x_pos(theta,t,v0,x0):
    x=x0+v0*np.cos(theta)*t
    return x

def y_pos(theta,t,v0,y0):
    y=y0+(v0*np.sin(theta)*t)-((g*t**2)/2)
    return y
time = ((2*v0)*np.sin(theta))/g
t=np.linspace(0,time,50)
x=x_pos(theta,t,v0,0)
y=y_pos(theta,t,v0,0)
N=len(t)

fig, ax=plt.subplots()
ln, = plt.plot(x,y,'ro')
ax.set_xlim(0,100)
ax.xaxis.set_major_locator(mtl.MultipleLocator(10))
ax.set_ylim(0,100)
ax.yaxis.set_major_locator(mtl.MultipleLocator(10))

def actualizar(i):
    ln.set_data(x[i],y[i])
    return ln,
ani = animation.FuncAnimation(fig,actualizar,range(N),interval=1, repeat = False)

def distancia(num):
    num = 0


MiVentana = Tk()
MiVentana.geometry('725x525')
MiVentana.title("Programa")
MiVentana.minsize(width=725 , height=525)
MiVentana.config(bg="white")

frame = Frame(MiVentana, bd=3)
frame.pack(expand=1, fill='both')

canva = FigureCanvasTkAgg(fig, master = frame)
canva.get_tk_widget().pack(padx=5, pady=5, expand=1, fill="both")

entrada = StringVar()

Label(frame, text='Ingrese la distancia: ', width=15, bg='white', fg='black').pack(pady = 5, side='left', expand=1)
Entry(frame, width=35, bg = 'white', fg ='black', textvariable=entrada).pack(pady = 5, side='left', expand=1)
Button(frame, text='Ingresar Dato', width=15, bg='black', fg='white').pack(pady = 5, side='left', expand=1)

MiVentana.mainloop()