# Imports
import tkinter
import turtle
import ttkthemes
from sympy import *
from tkinter import colorchooser

#Defining everything for the parametric curve.
buffer_constant = 5
def draw_curve():

    a = float(parse_expr(start_time_entry.get()))
    b = float(parse_expr(end_time_entry.get()))
    delta_t = 0.025

    t = a
    tvar = Symbol('t')
    f = parse_expr(x_function_entry.get())
    g = parse_expr(y_function_entry.get())

    buffer_multiplier = 1

    if(automatic_scaling_factor.get()==1):
        L = float(minimum(f,tvar,Interval(a,b)))
        R = float(maximum(f,tvar,Interval(a,b)))
        B = float(minimum(g,tvar,Interval(a,b)))
        T = float(maximum(g,tvar,Interval(a,b)))

        delta_L = L
        delta_R = canvas_width-R
        delta_B = B
        delta_T = canvas_height-T

        Q = max(delta_L,delta_R,delta_B,delta_T)

        buffer_multiplier = buffer_constant/Q
        #print(buffer_multiplier)

    def C(t):
        return (float(f.evalf(subs={tvar:t}))/buffer_multiplier,float(g.evalf(subs={tvar:t}))/buffer_multiplier)

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

def choose_canvas_color():
    color_code = colorchooser.askcolor(title ="Choose a color") 
    curve_canvas.configure(bg=color_code[1])

def choose_turtle_color():
    color_code = colorchooser.askcolor(title ="Choose a color") 
    draw.pencolor(color_code[1])

# Setting up layout for window. Mostly irrelevant to the actual parametric curve.
canvas_width = 500
canvas_height = 500

root = ttkthemes.ThemedTk(theme="arc")
root.title("Tofu Parametric Visualizer")
root.resizable(False,False)

settings_frame = tkinter.Frame(root,width=200,height=canvas_height)
curve_canvas = tkinter.Canvas(root,width=canvas_width,height=canvas_height)

start_button = tkinter.Button(settings_frame,text="Draw curve",command=draw_curve)
clear_button = tkinter.Button(settings_frame,text="Clear canvas",command=clear)

canvas_color_button = tkinter.Button(settings_frame,text="Change canvas color",command=choose_canvas_color)
turtle_color_button = tkinter.Button(settings_frame,text="Change curve color",command=choose_turtle_color)
automatic_scaling_factor = tkinter.IntVar()
enable_automatic_scaling_factor_label = tkinter.Label(settings_frame,text="Automatic scaling factor\n(Doesn't work with all functions)")
enable_automatic_scaling_factor = tkinter.Checkbutton(settings_frame,variable=automatic_scaling_factor,onvalue=1,offvalue=0)

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
draw.shape("classic")

settings_frame.grid(row=0,column=0)
curve_canvas.grid(row=0,column=1)

enable_automatic_scaling_factor_label.pack()
enable_automatic_scaling_factor.pack()

canvas_color_button.pack()
turtle_color_button.pack()

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