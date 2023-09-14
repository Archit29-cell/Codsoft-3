import tkinter as tk
from tkinter import messagebox

import random
import string
import pyperclip


root = tk.Tk()
root.title('Password Generator')
root.geometry('200x150')
root.resizable(0,0)

password_length = tk.Label(root, text="Password Length ",borderwidth=1,relief='solid')
password_length.pack(pady =2)

password_length_entry = tk.Entry(root, borderwidth =2, relief = 'solid')
password_length_entry.pack(pady =2)

generate_button = tk.Button(root, text ='Generate Password',borderwidth=2, relief= 'solid',command=lambda:generate_password())
generate_button.pack(pady=2)

password_entry = tk.Entry(root, borderwidth=2, relief='solid')
password_entry.pack(pady =2)

copy= tk.Button(root, text ='Copy', borderwidth=2, relief = 'solid',bg='black', fg='white',command=lambda:copy_password())
copy.pack(pady =2)
def generate_password():
    length = int(password_length_entry.get())

    if length <8:
        messagebox.showerror('Error','Password length must be atleast 8 characters', parent= root)
        return 
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    special_characters = string.punctuation
    
    # Ensure at least one character from each set
    password = (
        random.choice(uppercase_letters) +
        random.choice(lowercase_letters) +
        random.choice(special_characters) +
        ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length - 3))
    )
    
    # Shuffle the characters to make it random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo('Copied','Your password has been succesfully copied to clipboard',parent= root)

root.mainloop()