import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import os

# Function to clear the text editor
def new_file():
    txt_editor.delete("1.0", tk.END)

# Function to open a file and load its contents into the text editor
def open_file():
    file_types = (
        ("Text Files", "*.txt"),
        ("All Files", "*.*")
    )
    file_path = fd.askopenfilename(
        title='Open a File',
        initialdir=initial_directory,
        filetypes=file_types
    )

    if not file_path:
        return
    
    new_file()  # Clear existing text
    with open(file_path, "r") as file:
        text = file.read()
        txt_editor.insert(tk.END, text)

# Function to save the text editor content into a file
def save_file():
    file_types = (
        ("Text Files", "*.txt"),
        ("All Files", "*.*")
    )
    file_path = fd.asksaveasfilename(
        title="Save a File",
        initialdir='/Almadrasa/1/3-python projects/My_projects/6-TextEditor',
        filetypes=file_types
    )

    if not file_path:
        return
    
    with open(file_path, "w") as file:
        text = txt_editor.get("1.0", tk.END)
        file.write(text)

    show_save_message()  # Display save success message

# Function to display a temporary message indicating successful save
def show_save_message():
    message = tk.Label(root, text='File saved successfully 👌', bg='lightgreen', fg='black', padx=10, pady=5)
    message.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    root.after(2000, message.destroy)  # Destroy the message after 2000 milliseconds (2 seconds)

# Create the main window
root = tk.Tk()
root.title('Text Editor')
root.geometry('800x600')

# Set initial directory to the user's home directory
initial_directory = os.path.expanduser("~")

# Create menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Frame to hold buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

# Buttons for New, Open, and Save
new_button = ttk.Button(button_frame, text="New", command=new_file)
new_button.grid(row=0, column=0, padx=5)

open_button = ttk.Button(button_frame, text="Open", command=open_file)
open_button.grid(row=0, column=1, padx=5)

save_button = ttk.Button(button_frame, text="Save", command=save_file)
save_button.grid(row=0, column=2, padx=5)

# Text editor widget
txt_editor = tk.Text(root, bd=4, font=("Helvetica", 12), relief="groove", wrap=tk.WORD)
txt_editor.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

# Start the main event loop
root.mainloop()
