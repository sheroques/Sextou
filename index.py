import tkinter as tk 
import random

root = tk.Tk()
root.geometry('300x300')
root.title('sextou')

def hover(event):
    x=random.randint(0,200)
    y=random.randint(0,200)
    nao.place(x=x, y=y)

def mensagem():
    message = tk.Label(root, text='Onde?')
    message.place(x=70, y=120, relx=0, rely=0)
    
pergunta = tk.Label(root, text='Bora beber hoje?')
pergunta.pack(anchor='n', padx=20)

nao = tk.Button(root, text='não')
nao.place(x=140, y=80)
nao.bind('<Enter>',hover)

sim = tk.Button (root, text='sim', command= mensagem)
sim.place(x=25, y=80, relx=0, rely=0) 

root.mainloop()   
    
    