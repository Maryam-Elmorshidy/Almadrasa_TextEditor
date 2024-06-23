import tkinter as tk
from tkinter import filedialog as fd
import os 

root = tk.Tk() 

# Set initial directory to the user's home directory
initial_directory = os.path.expanduser("~")

def new_file():
    txt_editor.delete("1.0" , tk.END)

def open_file():
    file_types = (
        ("text file" , '*.txt'),
        ('All files' , '*.*'),
    )
    file_path = fd.askopenfilename(
        title='open a file',
        initialdir= initial_directory,
        filetypes= file_types
    )

    if not file_path :
        return
    
    new_file
    with open(file_path , "r") as file :
        text = file.read()
        txt_editor.insert(tk.END , text)

def save_file():
    file_types = (
        ("text file" , '*.txt'),
        ('All files' , '*.*'),
    )
    file_path =fd.asksaveasfilename(
        title="save a file" , 
        initialdir= '/Almadrasa/1/3-python projects/My_projects/6-TextEditor' ,
        filetypes= file_types
    )

    if not file_path :
        return
    
    with open(file_path , "w") as file :
        text = txt_editor.get("1.0" , tk.END)
        file.write(text)
        ourMessage = 'File saved successfully 👌'
        message =tk. Message(root,width=200, text=ourMessage)
        message.config(bg='lightgreen')
        root.after(2000, message.destroy) 
        message.pack()
        


list_menu = tk.Menu(root)
root.config(menu=list_menu)

dropdown_menu = tk.Menu(root)
list_menu.add_cascade(label="Menu" , menu=dropdown_menu)
dropdown_menu.add_command(label="New" , command= new_file)
dropdown_menu.add_command(label="Open" , command= open_file)
dropdown_menu.add_command(label="Save" , command= save_file)

txt_editor = tk.Text(root , bd= 4 , font=("Helvetica", 12) , relief= "groove" , height= 30 , width= 70)
txt_editor.pack(padx=5 , pady=5)


root.mainloop()


