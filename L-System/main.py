import tkinter as tk
from turtle import *
import turtle
import draw
import os.path
import pfuncs as pf
from tkinter import messagebox
import sys
from tkinter import *

# return True if inputted string is "true" or default to a return of False
def string_to_bool(input):
    input = str(input).lower()
    if(input == "true"):
        return True
    else:
        return False

# check a list of strings and check weather or not there is an empty string or not
def check_if_empty(values):
    for tmp in values:
        if(tmp == ""):
            return False
    return True

# check a list of strings and remove every white space from every string
def replace_spaces(data):
    for i in range(len(data)):
        data[i] = data[i].replace(" ", "")
    return data

# clean inputs for L-System to avoid any major errors
def clean_inputs(values):
    title = str(values[0]).replace(" ", "_")
    variables = replace_spaces(str(values[1]).split(","))
    moveForward = replace_spaces(str(values[2]).split(","))
    turnLeft = replace_spaces(str(values[3]).split(","))
    turnRight = replace_spaces(str(values[4]).split(","))
    start = str(values[5]).split(",")
    rules = replace_spaces(str(values[6]).split(","))
    angle = float(values[7])
    n = int(values[8])
    dis = int(values[9])
    saveImage = string_to_bool(str(values[10]))

    return title, variables, moveForward, turnLeft, turnRight, start, rules, angle, n, dis, saveImage

# main function for using user's input to create defined L-System
def draw_function():
    values = [e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get(), e8.get(), e9.get(), e10.get(), e11.get()]

    if(check_if_empty(values)):
        title, variables, moveForward, turnLeft, turnRight, start, rules, angle, n, dis, saveImage = clean_inputs(values)

        draw.main(title, variables, moveForward, turnLeft, turnRight, start, rules, angle, n, dis, saveImage)
    
    else:
        messagebox.showerror("INVALID INPUT", "The following input is invalid: \n" + str(values))

# saves user's inputed L-System values to a pickle file (.p file)
def save_inputs():
    values = [e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get(), e8.get(), e9.get(), e10.get(), e11.get()]
    if(check_if_empty(values)):
        title, variables, moveForward, turnLeft, turnRight, start, rules, angle, n, dis, saveImage = clean_inputs(values)
        values = [title, variables, moveForward, turnLeft, turnRight, start, rules, angle, n, dis, saveImage]
        pf.pickle_save(str(values[0])+".pickle", values)
        messagebox.showinfo("Successfully Saved", "Saved The Following Config: \n" + str(values))
    else:
        messagebox.showerror("INVALID INPUT", "The following input is invalid: \n" + str(values))

# load and draw a saved pickle file, generated from save_inputs()
def load_save():
    path = str(e12.get())

    if(os.path.isfile(path)):
        tmp = pf.pickle_load(path)
        title, variables, moveForward, turnLeft, turnRight, start, rules, angle, n, dis, saveImage = tmp
        draw.main(title, variables, moveForward, turnLeft, turnRight, start, rules, angle, n, dis, saveImage)
    else:
        message = "The file/path you have inputed does not exist!"
        messagebox.showerror("INVALID INPUT", message)

# generate an info message of all the paths to all the saved pickle file states
def list_saved_pickles(path="."):
    tmp = pf.find_all_pickle_files(path)
    message = "PATHS: \n"
    for p in tmp:
        message = message + "\n" + str(p)

    print("\n" + message + "\n")
    messagebox.showinfo("Saved Pickle Files PATHs", message)

# print all the options for running the main script
def command_options():
    print("""

    [ Options ]
    python3 main.py     : run main script with initial warning message
    python3 main.py -nw : run main script without initial warning message

    """)

def move_to_saves():
    tmp = pf.move_to_saves()

    if(tmp):
        messagebox.showinfo("Moved Any Remaining .pickle File(s)", "Any L-System configs saves, .pickle, files has been moved to saves/")
    else:
        messagebox.showinfo("FAILED To Move Any Remaining .pickle Files(s)", "Sorry for the error, please correct it if possible!")

#######################################################
#################[ Main TK GUI Setup ]#################
#######################################################

root = tk.Tk()
root.title("L-System Generator")

command_options()

# print gui advice/warning message, toggle on/off by changing the boolean below
if "-nw" not in list(sys.argv):
    messagebox.showerror("Advice/Warning", "Please do not close either of the two windows well in use. Either keep both windows open or close ALL of the windows when you are don using the program.")

tk.Label(root, text="title (str)").grid(row=0)
tk.Label(root, text="variables (list)").grid(row=1)
tk.Label(root, text="forward var (list)").grid(row=2)
tk.Label(root, text="left var (list)").grid(row=3)
tk.Label(root, text="right var (list)").grid(row=4)
tk.Label(root, text="starting (str)").grid(row=5)
tk.Label(root, text="rules (list)").grid(row=6)
tk.Label(root, text="angle (int/float)").grid(row=7)
tk.Label(root, text="n (int)").grid(row=8)
tk.Label(root, text="distance (int)").grid(row=9)
tk.Label(root, text="save image? (boolean)").grid(row=10)

e1 = tk.Entry(root)
e1.grid(row=0, column=1)

e2 = tk.Entry(root)
e2.grid(row=1, column=1)

e3 = tk.Entry(root)
e3.grid(row=2, column=1)

e4 = tk.Entry(root)
e4.grid(row=3, column=1)

e5 = tk.Entry(root)
e5.grid(row=4, column=1)

e6 = tk.Entry(root)
e6.grid(row=5, column=1)

e7 = tk.Entry(root)
e7.grid(row=6, column=1)

e8 = tk.Entry(root)
e8.grid(row=7, column=1)

e9 = tk.Entry(root)
e9.grid(row=8, column=1)

e10 = tk.Entry(root)
e10.grid(row=9, column=1)

e11 = tk.Entry(root)
e11.grid(row=10, column=1)

tk.Button(root, text='DRAW', command=draw_function).grid(row=11, column=1, sticky=tk.W, pady=4)

tk.Button(root, text='SAVE', command=save_inputs).grid(row=12, column=1, sticky=tk.W, pady=4)

tk.Label(root, text="load file (str)").grid(row=13)
e12 = tk.Entry(root)
e12.grid(row=13, column=1)

tk.Button(root, text='LOAD', command=load_save).grid(row=14, column=1, sticky=tk.W, pady=4)

tk.Button(root, text='PATHS', command=list_saved_pickles).grid(row=14, column=0, sticky=tk.W, pady=4)

tk.Button(root, text='CLEAN', command=move_to_saves).grid(row=15, column=0, sticky=tk.W, pady=4)

tk.mainloop()
