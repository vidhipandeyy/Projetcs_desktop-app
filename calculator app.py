import tkinter as tk

def click(num):
    entry.insert(tk.END, num)

def clear():
    entry.delete(0, tk.END)

def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, result)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x350")

entry = tk.Entry(root, font=("Arial",20), bd=5, relief="ridge", justify="right")
entry.pack(fill="both", padx=10, pady=10)

buttons = [
["7","8","9","/"],
["4","5","6","*"],
["1","2","3","-"],
["0",".","=","+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    
    for btn in row:
        if btn == "=":
            button = tk.Button(frame, text=btn, width=5, height=2, command=calculate)
        else:
            button = tk.Button(frame, text=btn, width=5, height=2, command=lambda b=btn: click(b))
        button.pack(side="left", padx=5, pady=5)

root.mainloop()