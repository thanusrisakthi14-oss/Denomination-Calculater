import tkinter as tk
window=tk.Tk()
window.title("Denomination Calculater")
window.geometry("500x500")

def calculator():
    amount= int(e.get())
    denominations=[500,200,100,50,20,5]
    t.delete("1.0",tk.END)
    for denomination in denominations:
        result = amount//denomination
        if result > 0:
            t.insert(tk.END,f"{denomination} -----> {result}\n")
        amount=amount%denomination
    

l=tk.Label(window,text="Entre the Amount:")
l.pack()
e=tk.Entry(window)
e.pack()
b=tk.Button(window,text="Gernerate",command=calculator)
b.pack()
t=tk.Text(window,width=40,height=40)
t.pack()
window.mainloop()

        
