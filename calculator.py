import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("COS202 - Mathematical Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        self.expression = ""
        self.display = tk.Entry(self.root, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=10, ipady=20)
        
        buttons = ['C', 'OFF', '%', '/', '7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+', '0', '.', '^', '=']
        
        row, col = 1, 0
        for button in buttons:
            if button == "=":
                btn = tk.Button(self.root, text=button, font=("Arial", 18, "bold"), bg="#4CAF50", fg="white", height=2, width=8, command=self.calculate)
            elif button == "C":
                btn = tk.Button(self.root, text=button, font=("Arial", 18), bg="#f44336", fg="white", height=2, width=8, command=self.clear)
            elif button == "OFF":
                btn = tk.Button(self.root, text=button, font=("Arial", 18), bg="#9E9E9E", fg="white", height=2, width=8, command=self.root.quit)
            else:
                btn = tk.Button(self.root, text=button, font=("Arial", 18), height=2, width=8, command=lambda b=button: self.append(b))
            
            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def append(self, value):
        self.expression += str(value)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            expr = self.expression.replace('^', '**')
            result = eval(expr)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(round(result, 8)))
            self.expression = str(result)
        except:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear()

if __name__ == "__main__":
    calc = Calculator()
    calc.root.mainloop()