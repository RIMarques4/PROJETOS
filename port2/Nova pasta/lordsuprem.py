import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox


root = tk.Tk()
root.title('aceitas')
root.geometry('600x600')
root.configure(background='ffc8dd')


def move_button_1(e):
    if abs(e.x - Button_1.winfo_x()) <50 and abs(e.y - Button_1.winfo()) <40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_whidrth())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        Button_1.place(x=x, y=y)


def accepted():
    messagebox.showinfo(
        'MEU AMOR, EU TE AMO')
    

def denied():
    button_1.destroy() 


margin = Canvas(root, width=500, bg='#affc8dd', height=100,
                bd=0, highlightthickness=0, relief='ridge')
margin
