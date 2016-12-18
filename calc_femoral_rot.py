# Python code to calculate elliptical arc length given 
# lenghts of minor and major axes and desired rotation angle in degrees
# Assumes rotation starts from the major axis to the minor axis
# Author: Surre Markandaya
# Collaborator: Dr. Sangeeth Gangadharan

from tkinter import *
from quit_app import QuitApp
from scipy.integrate import quad
import numpy as np
import math
import decimal
from PIL import Image, ImageTk

fields = ['Major Axis Length', 'Minor Axis Length', 
         'Desired Rotation Angle (deg)']

def get_arc_len(entries):
    input_names = ['a', 'b', 'theta', 'ev']
    input_vals  = [float(entry.get()) for entry in entries[0:-1]] + ['']
    input_dict = dict(zip(input_names, input_vals))
    e_val, c_val = calc_arc_lengths(input_dict['a'], input_dict['b'], 
                                    input_dict['theta'])
    entries[-1].set(e_val)


def makegui(root, fields):
    variables = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=25, text=field, justify=LEFT)
        ent = Entry(row, width=5)
        row.pack(side=TOP, fill=X)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        var = StringVar()
        ent.config(textvariable=var)
        variables.append(var)
    res_row_lbl = Frame(root)
    res_lbl = Label(res_row_lbl, text = 'Calculated Arc Lengths')
    res_lbl.config(bg='black', fg='yellow', height=2)
    res_row_lbl.pack(side=TOP, fill=X)
    res_lbl.pack(side=LEFT, expand=YES, fill=X)

    res_row1 = Frame(root)
    elab = Label(res_row1, height = 3, width=25, 
                 text="Elliptical Arc Length", justify=LEFT)
    evlab = Label(res_row1, height = 3, width=5, justify=LEFT,  
                  text="", bg="yellow",fg="black",font=("times",10,"bold"))
    res_row1.pack(side=TOP, fill=X)
    elab.pack(side=LEFT)
    evlab.pack(side=RIGHT,expand=YES,fill=X)
    ev_var = StringVar()
    evlab.config(textvariable=ev_var)
    variables.append(ev_var)

    return variables


def cobeljic(a, b, theta):
    """Computes Cobeljic's approximation to arc length of ellipse"""

    # a is the length of major axis
    # b is the length of minor axis
    # theta is the desired rotation in radians
    # Assumes rotation starts from the major axis to the minor axis

    avg_rad = (a+b)/2.0
    return float(round(decimal.Decimal(avg_rad*np.sin(theta/2.0)),1)) 

def calc_ellipse_arc_length(a, b, theta):
    """Computes arc length of ellipse via elliptic integral"""

    # a is the length of major axis
    # b is the length of minor axis
    # theta is the desired rotation in radians
    # Assumes rotation starts from the major axis to the minor axis

    maj_ax = a
    min_ax = b
    rot_angle = theta

    def integrand(x):
        return np.sqrt(((min_ax/2.0)**2)*(np.sin(x)**2) + ((maj_ax/2.0)**2)*(np.cos(x)**2))

    arc_len, err = quad(integrand, 0, rot_angle)
    return float(round(decimal.Decimal(arc_len),1))
    
def calc_arc_lengths(a, b, rot_angle_in_degrees):
    # a is the length of major axis
    # b is the length of minor axis

    # convert desired rotation angle in degrees to radians
    rot_angle = (rot_angle_in_degrees/180.0)*math.pi

    ca = str(cobeljic(a, b, rot_angle))
    ea = str(calc_ellipse_arc_length(a, b, rot_angle))
    return (ea, ca)

if __name__=='__main__':
    root = Tk()
    root.title("Ellipse Arc Length Calculator")
    labelfont = ('times', 16, 'bold')
    top_lbl = Label(root, text = 'Femoral Osteotomy Ellipse Arc Length Calculator')
    top_lbl.config(bg='black', fg='yellow')
    top_lbl.config(font=labelfont, height=3)
    top_lbl.pack(side=TOP, expand=YES, fill=X)
    photo = ImageTk.PhotoImage(file='./ellipse3.png')
    canv = Canvas(root, width=750, height = 300)
    canv.create_image(0,-60, image=photo, anchor=NW)
    canv.pack(side=TOP)
    ents = makegui(root, fields)
    Button(root, text="Calculate",
                 command = (lambda: get_arc_len(ents))).pack(side=LEFT)
    QuitApp(root).pack(side=RIGHT)
    root.mainloop()
