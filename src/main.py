# Imports
import tkinter
import turtle
import math
import sympy

#Defining everything for the parametric curve.
def fn(t):
    return float(2*sympy.cos(4*t)*sympy.cos(t))*100

def gn(t):
    return float(2*sympy.cos(4*t)*sympy.sin(t))*100

def draw_curve():

    a = float(start_time_entry.get())
    b = float(end_time_entry.get())
    delta_t = 0.025

    t = a

    draw.goto(fn(t),gn(t))
    draw.pendown()

    while t <= b:
        draw.goto(float(fn(t)),float(gn(t)))
        t += delta_t

    draw.penup()

def clear():
    draw.penup()
    draw.goto(0,0)
    draw.clear()

# Setting up layout for window. Mostly irrelevant to the actual parametric curve.
canvas_width = 500
canvas_height = 500

root = tkinter.Tk()
root.title("Tofu Parametric Visualizer")
root.resizable(False,False)

settings_frame = tkinter.Frame(root,width=200,height=canvas_height)
curve_canvas = tkinter.Canvas(root,width=canvas_width,height=canvas_height)

start_button = tkinter.Button(settings_frame,text="Draw curve",command=draw_curve)
clear_button = tkinter.Button(settings_frame,text="Clear canvas",command=clear)
start_time_entry_label = tkinter.Label(settings_frame,text="Start of interval")
start_time_entry = tkinter.Entry(settings_frame)
end_time_entry_label = tkinter.Label(settings_frame,text="End of interval")
end_time_entry = tkinter.Entry(settings_frame)



draw = turtle.RawTurtle(curve_canvas)

draw.penup()
draw.speed(40)

settings_frame.grid(row=0,column=0)
curve_canvas.grid(row=0,column=1)
start_time_entry_label.pack()
start_time_entry.pack()
end_time_entry_label.pack()
end_time_entry.pack()
start_button.pack()
clear_button.pack()

root.mainloop()