# -*- coding: utf-8 -*-
from tkinter import *
import time
from math import sin, cos, radians, pi
import os
import math
g=9.8
ax=0
ay=-g
clock=0.001

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def projection():
	ball=canvas.create_oval(ox-30,oy-30,ox+30,oy+30, fill='orange')
	u=float(u_entry.get())
	theta=float(theta_entry.get())
	theta=radians(theta)
	if theta==0.0:
		T=math.inf
	else:
		T=2*u*sin(theta)/g
	H=((u**2)*((sin(theta))**2))/(2*g)
	R=((u**2)*(sin(2*theta)))/g
	t=0

	xscale,yscale=1,1
	if R<=400 and R>200:
		xscale=5
		yscale=5
	elif R<=200 and R>100: 
		xscale,yscale=10,10
	elif R<=100:
		xscale,yscale=15,15
	print(T,R,H)
	while t<=T:
		if (theta)==0.0:
			x,y=u*t*xscale,0
		else:
			x=(u*t*cos(theta))*xscale
			y=((u*t*sin(theta))-((1.0/2)*g*t**2))*yscale
		#print(x,y)
		#canvas.move(ball,xspeed,-yspeed)
		#pos=canvas.coords(ball) 
		tk.update()
		time.sleep(clock)
		canvas.delete(ball)
		path=canvas.create_text(ox+x,oy-y,text=".")
		ball=canvas.create_oval(ox-30+x,oy-30-y,ox+30+x,oy+30-y, fill='orange')
		t+=clock
	canvas.create_line(ox,oy+20,ox+R*xscale,oy+20)
	canvas.create_text(ox+0.5*R*xscale,oy+30,text="Range="+str(round(R,2))+"metres",font="Times 15 bold")
	canvas.create_line(ox+0.5*R*xscale,oy,ox+0.5*R*xscale,oy-H*yscale)
	canvas.create_text(ox+0.5*R*xscale+20,oy-0.5*H*yscale,text="Maximum Height="+str(round(H,2))+"metres",font="Times 15 bold")
	canvas.create_text(ox+0.5*R*xscale,oy-H*yscale-10,text="Time of Flight="+str(round(T,2))+"seconds",font="Times 15 bold")
	canvas.create_text(1000,100,text="Scale: 1 metre="+str(xscale)+"pixels",font="Times 15 bold")

tk=Tk()

canvas_width=tk.winfo_screenwidth()
canvas_height=tk.winfo_screenheight()

canvas=Canvas(tk,width=canvas_width,height=canvas_height)
canvas.pack() 

#origin
ox,oy=100,750
#x and y axes
canvas.create_line(ox,oy-600,ox,oy,fill='red',width=4)
canvas.create_line(ox,oy,ox+1800,oy,fill='red',width=4)
ball=canvas.create_oval(ox-30,oy-30,ox+30,oy+30, fill='orange')	#ball

#inputs
u_label=Label(canvas, text="Initial velocity: u=",font="Times 15 bold")
canvas.create_text(850,oy+100, text="m/s",font="Times 15 bold")
theta_label=Label(canvas, text="Angle of projection: θ=",font="Times 15 bold")
canvas.create_text(850,oy+130, text="degrees",font="Times 15 bold")
canvas.create_window(600, oy+100, window=u_label, height=25, width=200)
canvas.create_window(600, oy+130, window=theta_label, height=25, width=200)
u_entry = Entry(canvas)
theta_entry=Entry(canvas)
canvas.create_window(750, oy+100, window=u_entry, height=25, width=100)
canvas.create_window(750, oy+130, window=theta_entry, height=25, width=100)

#Buttons
run=Button(canvas, text='Run',font="Times 15 bold", command=projection)	
canvas.create_window(720, oy+170, window=run, height=25, width=50)
clear=Button(canvas, text='Clear',font="Times 15 bold", command=restart_program)
canvas.create_window(800, oy+170, window=clear, height=25, width=60)

mainloop()

