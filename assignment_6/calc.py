import tkinter as tk

first_number = None
operation = None

def add_digit(digit):
    input_field["state"] = "normal"
    input_field.insert(tk.END, str(digit)) 
    input_field["state"] = "readonly"
    #print(f"Digit {digit} added to input field.")

def clear():
    global first_number, operation
    input_field["state"] = "normal"
    input_field.delete(0, tk.END)
    input_field["state"] = "readonly"
    operation = None

def calculate():
    global operation
    if operation is None: 
        return
    formula = str(input_field.get())
    
    if formula is None:
        return
    parts = formula.split(operation)
    first_number = float(parts[0])
    second_number= float(parts[1])
    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Error press (C) to clear"
    input_field["state"] = "normal"
    input_field.delete(0, tk.END)
    input_field.insert(0, str(result))
    input_field["state"] = "readonly"
    operation = None

def set_operation(op):
    global  operation
    if operation is not None:
        return
    operation = op
    add_digit('')
    add_digit(op)
    add_digit('')
    


Window = tk.Tk()
Window.title("Simple Calculator")
#Window.geometry("320x320")
input_field = tk.Entry(Window, width=16, font=('Arial', 24), borderwidth=2, relief='ridge')
input_field.grid(row=0, column=0, columnspan=4)

input_field["state"] = "readonly"

for i in range(1,10):
    button = tk.Button(Window, text=str(i), width=4, height=2, font=('Arial', 18),
                       command=lambda d=i: add_digit(d))
    button.grid(row=(i-1)//3 + 1, column=(i-1)%3)

# Button 0
button_0 = tk.Button(Window, text="0", width=4, height=2, font=('Arial', 18),
                     command=lambda: add_digit(0))
button_0.grid(row=4, column=0)

# Clear button
clear_button = tk.Button(Window, text="C", width=4, height=2, font=('Arial', 18),
                         command=clear)
clear_button.grid(row=4, column=1)

# Equals button
equals_button = tk.Button(Window, text="=", width=4, height=2, font=('Arial', 18),
                          command=calculate)
equals_button.grid(row=4, column=2)

# Operators
add_button = tk.Button(Window, text="+", width=4, height=2, font=('Arial', 18),
                       command=lambda: set_operation('+'))
add_button.grid(row=1, column=3)

sub_button = tk.Button(Window, text="-", width=4, height=2, font=('Arial', 18),
                       command=lambda: set_operation('-'))
sub_button.grid(row=2, column=3)

mul_button = tk.Button(Window, text="*", width=4, height=2, font=('Arial', 18),
                       command=lambda: set_operation('*'))
mul_button.grid(row=3, column=3)

div_button = tk.Button(Window, text="/", width=4, height=2, font=('Arial', 18),
                       command=lambda: set_operation('/'))
div_button.grid(row=4, column=3)

Window.mainloop()