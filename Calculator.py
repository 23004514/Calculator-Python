import tkinter as tk
import math

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x500")

expression = ""

# Function to update expression
def press(key):
    global expression
    expression += str(key)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Clear screen
def clear():
    global expression
    expression = ""
    equation.set("")

# Scientific functions
def sin():
    global expression
    result = math.sin(math.radians(float(expression)))
    equation.set(str(result))
    expression = str(result)

def cos():
    global expression
    result = math.cos(math.radians(float(expression)))
    equation.set(str(result))
    expression = str(result)

def tan():
    global expression
    result = math.tan(math.radians(float(expression)))
    equation.set(str(result))
    expression = str(result)

def log():
    global expression
    result = math.log10(float(expression))
    equation.set(str(result))
    expression = str(result)

def sqrt():
    global expression
    result = math.sqrt(float(expression))
    equation.set(str(result))
    expression = str(result)

equation = tk.StringVar()

entry = tk.Entry(root, textvariable=equation, font=('Arial',20), bd=10, insertwidth=2, width=18)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
('7',1,0),('8',1,1),('9',1,2),('/',1,3),
('4',2,0),('5',2,1),('6',2,2),('*',2,3),
('1',3,0),('2',3,1),('3',3,2),('-',3,3),
('0',4,0),('.',4,1),('+',4,2),('=',4,3)
]

for (text,row,col) in buttons:
    if text == "=":
        tk.Button(root,text=text,width=7,height=2,command=equalpress).grid(row=row,column=col)
    else:
        tk.Button(root,text=text,width=7,height=2,command=lambda t=text: press(t)).grid(row=row,column=col)

# Scientific buttons
tk.Button(root,text="sin",width=7,height=2,command=sin).grid(row=5,column=0)
tk.Button(root,text="cos",width=7,height=2,command=cos).grid(row=5,column=1)
tk.Button(root,text="tan",width=7,height=2,command=tan).grid(row=5,column=2)
tk.Button(root,text="log",width=7,height=2,command=log).grid(row=5,column=3)

tk.Button(root,text="√",width=7,height=2,command=sqrt).grid(row=6,column=0)
tk.Button(root,text="Clear",width=7,height=2,command=clear).grid(row=6,column=1,columnspan=2)

root.mainloop()