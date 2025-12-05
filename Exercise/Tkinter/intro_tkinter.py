import tkinter as tk
import tkinter.font as tfont
from tkinter import ttk
window=tk.Tk()
window.title("My App")
window.minsize(height=300,width=400)

custom_font=tfont.Font(family="Times New Roman",size=15,slant="italic")
label=ttk.Label(text="Hello World!!\nHave a nice day!!",font=custom_font,padding=15)
label.pack()

user_input=ttk.Entry(width=10,show="*")
user_input.pack()
print(user_input.get())

def function_button():
    inputttt=user_input.get()
    label.config(text=f"User Input={inputttt}")
button=ttk.Button(text="Click",command=function_button)
button.pack()

quit_button=ttk.Button(text="Quit",command=window.destroy)
quit_button.pack(pady=10)

sep=ttk.Separator(orient="horizontal")
sep.pack(fill='x',pady=10)

Text=tk.Text(height=5,width=20)
Text.pack()
Text.focus() #for cursor
Text.insert("1.0","Enter your comments")
def print_func():
    var=Text.get("1.0",'end')
    print(var)

text_button=ttk.Button(text="Get Text",command=print_func) 
text_button.pack()   
"""
Text['state']='disabled'

def enable_text():
    Text['state']='normal'
enabled_button=ttk.Button(text="Enable text box",command=enable_text)
enabled_button.pack()
"""
# check box
check_options=tk.StringVar()
def check_options_get():
    print(check_options.get())
check_button=ttk.Checkbutton(text="Agree with terms and conditions",variable=check_options,
                             command=check_options_get,onvalue="Yes",offvalue="No")
check_button.pack()

#radio button
radio_button=tk.StringVar()
def get_radio_value():
    print(radio_button.get())
option1=ttk.Radiobutton(text="Male",variable=radio_button,value="Male",command=get_radio_value)
option2=ttk.Radiobutton(text="Female",variable=radio_button,value="Female",command=get_radio_value)
option1.pack()
option2.pack()

#combo box
selected_country=tk.StringVar()
countries=ttk.Combobox(textvariable=selected_country,values=("Australia","Canada","USA","New Zealand","Paxtan","Srilanka"))
countries["state"]="readonly"
countries.pack()

def display_country(event):
    country_label=ttk.Label(text=selected_country.get())
    country_label.pack()
    #print(f"Selected country is {selected_country.get()}")
countries.bind("<<ComboboxSelected>>",display_country)

#List box
food_items=("Pizza","Burger","Mango","Apple","Salad")
fav_food=tk.StringVar(value=food_items)
food_list=tk.Listbox(listvariable=fav_food,height=5,selectmode="extended")
food_list.pack()

#Spin box
counter=tk.IntVar(value=10)
spin_box=ttk.Spinbox(from_=0, to=20,textvariable=counter)
spin_box.pack()
window.mainloop()

