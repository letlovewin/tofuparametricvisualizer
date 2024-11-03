# Imports
import tkinter
import turtle
import math
from sympy import *

#Defining everything for the parametric curve.

def draw_curve():

    a = float(parse_expr(start_time_entry.get()))
    b = float(parse_expr(end_time_entry.get()))
    delta_t = 0.025

    t = a
    tvar = Symbol('t')
    f = parse_expr(x_function_entry.get())
    g = parse_expr(y_function_entry.get())

    def fn(t):
        return float(f.evalf(subs={tvar:t}))

    def gn(t):
        return float(g.evalf(subs={tvar:t}))
    
    def C(t):
        return (fn(t),gn(t))

    draw.goto(C(t))
    draw.pendown()

    while t <= b:
        draw.goto(C(t))
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

x_function_entry_label = tkinter.Label(settings_frame,text="x(t)")
x_function_entry = tkinter.Entry(settings_frame)
x_function_entry.insert(0,"cos(t)")

y_function_entry_label = tkinter.Label(settings_frame,text="y(t)")
y_function_entry = tkinter.Entry(settings_frame)
y_function_entry.insert(0,"sin(t)")

start_time_entry_label = tkinter.Label(settings_frame,text="Start of interval")
start_time_entry = tkinter.Entry(settings_frame)
start_time_entry.insert(0,0)

end_time_entry_label = tkinter.Label(settings_frame,text="End of interval")
end_time_entry = tkinter.Entry(settings_frame)
end_time_entry.insert(0,10)

draw = turtle.RawTurtle(curve_canvas)

draw.penup()
draw.speed(40)

settings_frame.grid(row=0,column=0)
curve_canvas.grid(row=0,column=1)

x_function_entry_label.pack()
x_function_entry.pack(padx=10)

y_function_entry_label.pack()
y_function_entry.pack()

start_time_entry_label.pack()
start_time_entry.pack()

end_time_entry_label.pack()
end_time_entry.pack()

start_button.pack()
clear_button.pack()

root.mainloop()