import tkinter as tk
from tkinter import ttk

Window=tk.Tk()
Window.title("My Application")

my_frame=ttk.Frame()
my_frame.pack(side="left",fill="both",expand=True)

label1=tk.Label(my_frame,text="Hello World",bg="red")
label1.pack(side="left",fill='both',expand=True)

label2=tk.Label(text="How are you?",bg="blue")
label2.pack(side="top",fill='both',expand=True)

label3=tk.Label(text="Have a nice day",bg="green")
label3.pack(side="bottom",fill='both',expand=True)

Window.mainloop()