import tkinter as tk

# create the main window 
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#2e2e2e") #dark background

# add display widget
display = tk.Entry(root,width=30,borderwidth=5,font=("Arial",14),bg="#444",fg="#fff",justify='right',insertbackground='white')
display.grid(row=0, column=0,columnspan=4,padx=10,pady=10,ipady=10)

# create buttons and bind functions
def button_click(value):
    current = display.get()
    display.delete(0,tk.END)
    display.insert(0, current + str(value))

# Clear button
def button_clear():
    display.delete(0,tk.END)

# Equal button
def button_equal():
    try:
        result=eval(display.get())
        display.delete(0,tk.END)
        display.insert(0,str(result))
    except:
        display.delete(0,tk.END)
        display.insert(0,"Error")

#keyboard support
def handle_keypress(event):
    key = event.char
    if key in "0123456789+-*/.":
        button_click(key)
    elif key == "\r":
        button_equal()
    elif key.lower() == "c":
        button_clear()

# Bind keys
root.bind_all("<Key>",handle_keypress)

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('+',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('-',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('*',3,3),
    ('C',4,0),('0',4,1),('=',4,2),('/',4,3),
]
for (text, row, col) in buttons:
    action = button_click
    if text == "=":
        action = button_equal
    elif text == "C":
        action = button_clear
    btn = tk.Button(root, text=text, font=("Segoe UI",18), bg="#3a3a3a",fg="white", activebackground="#5a5a5a", activeforeground="white", command=(lambda val=text:action(val) if text not in ("=","C")else action()))
    btn.grid(row=row,column=col, padx=6,pady=6, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i,weight=1)
for i in range(5):
    root.grid_rowconfigure(i,weight=1)

    
root.mainloop()