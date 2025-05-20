import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("380x580")
root.resizable(False, False)

# Entry widget for input and result
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Define button click logic
def on_click(symbol):
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

# Create buttons using a loop
for row_num, row_values in enumerate(buttons):
    for col_num, value in enumerate(row_values):
        if value == '=':
            btn = tk.Button(root, text=value, width=5, height=2, font=('Arial', 18), command=calculate)
        else:
            btn = tk.Button(root, text=value, width=5, height=2, font=('Arial', 18), command=lambda v=value: on_click(v))
        btn.grid(row=row_num + 1, column=col_num, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text='C', width=22, height=2, font=('Arial', 18), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

root.mainloop()
