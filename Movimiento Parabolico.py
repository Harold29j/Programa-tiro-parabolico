import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import matplotlib.animation as animation
#Definimos los paramentros

root = tk.Tk()
root.config(width=725, height=525)
theta=np.pi/4
x0=0.
y0=0.
v0=50.
g=9.8

def x_pos(theta,t,v0,x0):
    x=x0+v0*np.cos(theta)*t
    return x

def y_pos(theta,t,v0,y0):
    y=y0+(v0*np.sin(theta)*t)-((g*t**2)/2)
    return y
t=np.linspace(0,8,50)
x=x_pos(theta,t,v0,0)
y=y_pos(theta,t,v0,0)
N=len(t)

fig, ax=plt.subplots()
ln, = plt.plot(x,y,'ro')
ax.set_xlim(0,280)
ax.set_ylim(0,100)

def actualizar(i):
    ln.set_data(x[i],y[i])
    return ln,
ani = animation.FuncAnimation(fig,actualizar,range(N),interval=0.00001)
plt.grid()
plt.show()