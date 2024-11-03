import tkinter as tk
import math  # Import math module for trigonometric functions

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("540x550")
root.configure(bg="lightgray")

# Entry widget for displaying numbers and results
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=6, pady=30)

# Global variable to store the current expression
expression = ""

# Function to update the expression in the entry widget
def button_click(item):
    global expression
    expression += str(item)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

# Function to evaluate the expression and display the result
def calculate():
    global expression
    try:
        # Evaluate the expression, handle trigonometric functions, logarithm, square, and percentage
        if 'sin' in expression:
            expression = str(math.sin(math.radians(float(expression.replace('sin', '')))))
        elif 'cos' in expression:
            expression = str(math.cos(math.radians(float(expression.replace('cos', '')))))
        elif 'tan' in expression:
            expression = str(math.tan(math.radians(float(expression.replace('tan', '')))))
        elif 'Log' in expression:
            expression = str(math.log10(float(expression.replace('Log', ''))))
        elif 'X²' in expression:
            expression = str(float(expression.replace('X²', '')) ** 2)
        elif '%' in expression:
            expression = str(float(expression.replace('%', '')) / 100)
        else:
            expression = str(eval(expression))

        entry.delete(0, tk.END)
        entry.insert(tk.END, expression)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# Function to clear the entry widget
def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

# Define button colors
button_color = "#F0EBD8"
operator_color = "#748CAB"
clear_color = "#40916c"
equal_color = "#ffcad4"

# Define button fonts
button_font = ("Arial", 18)

# Create number and operator buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("%", 4, 4),
    ("sin", 1, 4), ("cos", 2, 4), ("tan", 3, 4), ("Log", 1, 5),
    ("X²", 2, 5), ("(", 3, 5), (")", 4, 5)
]

for (text, row, col) in buttons:
    color = operator_color if text in "+-*/%" else button_color
    tk.Button(root, text=text, width=5, height=2, font=button_font, bg=color, command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=5, pady=5)

# Clear and equals buttons
tk.Button(root, text="C", width=5, height=2, font=button_font, bg=clear_color, command=clear).grid(row=4, column=3, padx=5, pady=5)
tk.Button(root, text="=", width=12, height=2, font=button_font, bg=equal_color, command=calculate).grid(row=6, column=1, columnspan=3, padx=5, pady=10)

# Run the main loop
root.mainloop()
