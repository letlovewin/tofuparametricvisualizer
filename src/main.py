# This script written by Gray (letlovewin on GitHub)

# Imports
import tkinter
import turtle
import ttkthemes
from multiprocessing import Process
from sympy import *
from tkinter import colorchooser
from tkinter import ttk

#Defining everything for the parametric curve.
buffer_constant = 5
turtle_speed = 40

def draw_curve(draw,xt_entry,yt_entry,a_entry,b_entry):

    a = float(parse_expr(a_entry.get()))
    b = float(parse_expr(b_entry.get()))
    delta_t = 0.025

    t = a
    tvar = Symbol('t')
    f = parse_expr(xt_entry.get())
    g = parse_expr(yt_entry.get())

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

def commence_draw():
    p1 = Process(target=draw_curve(c1_draw,c1_x_function_entry,c1_y_function_entry,c1_start_time_entry,c1_end_time_entry))
    p1.start()
    p2 = Process(target=draw_curve(c2_draw,c2_x_function_entry,c2_y_function_entry,c2_start_time_entry,c2_end_time_entry))
    p2.start()

def clear(draw):
    draw.penup()
    draw.goto(0,0)
    draw.clear()

def clearall():
    clear(c1_draw)
    clear(c2_draw)

def choose_canvas_color():
    color_code = colorchooser.askcolor(title ="Choose canvas color") 
    curve_canvas.configure(bg=color_code[1])

def choose_turtle_color(draw):
    color_code = colorchooser.askcolor(title ="Choose curve color") 
    draw.pencolor(color_code[1])

# Setting up layout for window. Mostly irrelevant to the actual parametric curve.
canvas_width = 500
canvas_height = 500

root = ttkthemes.ThemedTk(theme="arc")
root.title("Tofu Parametric Visualizer")
root.resizable(False,False)

settings_frame = ttk.Notebook(root,width=200,height=canvas_height-30)
c1_curve_settings_frame = ttk.Frame(settings_frame,width=200)
c2_curve_settings_frame = ttk.Frame(settings_frame,width=200)
display_settings_frame = ttk.Frame(settings_frame,width=200)
settings_frame.add(c1_curve_settings_frame,text="Curve 1")
settings_frame.add(c2_curve_settings_frame,text="Curve 2")
settings_frame.add(display_settings_frame,text="Display")
curve_canvas = tkinter.Canvas(root,width=canvas_width,height=canvas_height)

start_button = ttk.Button(display_settings_frame,text="Draw curve",command=commence_draw)
clear_button = ttk.Button(display_settings_frame,text="Clear canvas",command=clearall)

canvas_color_button = ttk.Button(display_settings_frame,text="Change canvas color",command=choose_canvas_color)
automatic_scaling_factor = tkinter.IntVar()
enable_automatic_scaling_factor_label = ttk.Label(display_settings_frame,text="Automatic scaling factor\n(Doesn't work with all functions)")
enable_automatic_scaling_factor = ttk.Checkbutton(display_settings_frame,variable=automatic_scaling_factor,onvalue=1,offvalue=0)

# Objects for drawing of curve 1
c1_display_label = ttk.Label(c1_curve_settings_frame,text="Curve 1")

c1_turtle_color_button = ttk.Button(c1_curve_settings_frame,text="Change curve color",command=lambda:choose_turtle_color(c1_draw))

c1_x_function_entry_label = ttk.Label(c1_curve_settings_frame,text="x(t)")
c1_x_function_entry = ttk.Entry(c1_curve_settings_frame)
c1_x_function_entry.insert(0,"cos(t)")

c1_y_function_entry_label = ttk.Label(c1_curve_settings_frame,text="y(t)")
c1_y_function_entry = ttk.Entry(c1_curve_settings_frame)
c1_y_function_entry.insert(0,"sin(t)")

c1_start_time_entry_label = ttk.Label(c1_curve_settings_frame,text="Start of interval")
c1_start_time_entry = ttk.Entry(c1_curve_settings_frame)
c1_start_time_entry.insert(0,0)

c1_end_time_entry_label = ttk.Label(c1_curve_settings_frame,text="End of interval")
c1_end_time_entry = ttk.Entry(c1_curve_settings_frame)
c1_end_time_entry.insert(0,2*pi)

c1_draw = turtle.RawTurtle(curve_canvas)

c1_draw.penup()
c1_draw.speed(turtle_speed)
c1_draw.shape("classic")

# Objects for drawing of curve 2

c2_display_label = ttk.Label(c2_curve_settings_frame,text="Curve 2")

c2_turtle_color_button = ttk.Button(c2_curve_settings_frame,text="Change curve color",command=lambda:choose_turtle_color(c2_draw))

c2_x_function_entry_label = ttk.Label(c2_curve_settings_frame,text="x(t)")
c2_x_function_entry = ttk.Entry(c2_curve_settings_frame)
c2_x_function_entry.insert(0,"cos(t)")

c2_y_function_entry_label = ttk.Label(c2_curve_settings_frame,text="y(t)")
c2_y_function_entry = ttk.Entry(c2_curve_settings_frame)
c2_y_function_entry.insert(0,"sin(t)")

c2_start_time_entry_label = ttk.Label(c2_curve_settings_frame,text="Start of interval")
c2_start_time_entry = ttk.Entry(c2_curve_settings_frame)
c2_start_time_entry.insert(0,0)

c2_end_time_entry_label = ttk.Label(c2_curve_settings_frame,text="End of interval")
c2_end_time_entry = ttk.Entry(c2_curve_settings_frame)
c2_end_time_entry.insert(0,2*pi)

c2_draw = turtle.RawTurtle(curve_canvas)

c2_draw.penup()
c2_draw.speed(turtle_speed)
c2_draw.shape("classic")

# Adding everything to the root window.

settings_frame.grid(row=0,column=0)
curve_canvas.grid(row=0,column=1)

enable_automatic_scaling_factor_label.pack()
enable_automatic_scaling_factor.pack()

c1_display_label.pack()
c1_turtle_color_button.pack()
c1_x_function_entry_label.pack()
c1_x_function_entry.pack(padx=10)

c1_y_function_entry_label.pack()
c1_y_function_entry.pack()

c1_start_time_entry_label.pack()
c1_start_time_entry.pack()

c1_end_time_entry_label.pack()
c1_end_time_entry.pack()

c2_display_label.pack()
c2_turtle_color_button.pack()
c2_x_function_entry_label.pack()
c2_x_function_entry.pack(padx=10)

c2_y_function_entry_label.pack()
c2_y_function_entry.pack()

c2_start_time_entry_label.pack()
c2_start_time_entry.pack()

c2_end_time_entry_label.pack()
c2_end_time_entry.pack()

canvas_color_button.pack(pady=5)
start_button.pack(pady=5)
clear_button.pack(pady=5)

#Start the GUI

root.mainloop()