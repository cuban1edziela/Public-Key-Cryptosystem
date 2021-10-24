import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from db import Database
import deciphering
import enciphering
from ContactBook import *

db = Database('contact_list.db')

root = tk.Tk()
root.title("NonRSA Cryptosystem")
root.iconbitmap("icon.ico")


canvas = tk.Canvas(root, width=800, height=500)
canvas.grid(columnspan=5, rowspan=5)

# logo
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
welcome_message = tk.Label(root, text="Welcome to the Public Key Cryptosystem Program", font=("bold", 14), pady=20)
welcome_message.grid(column=1, row=1)

# textbox
text_box_message = tk.Entry(root, width=80, borderwidth=2)
text_box_e = tk.Entry(root, width=80, borderwidth=2)
text_box_n = tk.Entry(root, width=80, borderwidth=2)

# encipher button
encipher_text = tk.StringVar()
encipher__btn = tk.Button(root, textvariable=encipher_text, command=lambda: encipher_press_btn(), bg="#008037",
                          fg="white", height=2, width=15)
encipher_text.set("Encipher")
encipher__btn.grid(column=0, row=2)

# enter button encipher
enter_text_encipher = tk.StringVar()
enter__btn__encipher = tk.Button(root, textvariable=enter_text_encipher, command=lambda: get_message_encipher(),
                                 bg="#008037", fg="white",
                                 height=2, width=15)
enter_text_encipher.set("ENTER")

# decipher button
decipher_text = tk.StringVar()
decipher__btn = tk.Button(root, textvariable=decipher_text, command=lambda: decipher_press_btn(), bg="#008037",
                          fg="white", height=2, width=15)
decipher_text.set("Decipher")
decipher__btn.grid(column=2, row=2)

# enter button decipher
enter_text_decipher = tk.StringVar()
enter__btn__decipher = tk.Button(root, textvariable=enter_text_decipher, command=lambda: get_message_decipher(),
                                 bg="#008037", fg="white",
                                 height=2, width=15)
enter_text_decipher.set("ENTER")

# contact book btn
contact_book_text = tk.StringVar()
contact_book_btn = tk.Button(root, textvariable=contact_book_text, command=lambda: open_contact_book(),bg="#008037", fg="white",
                                 height=2, width=15 )
contact_book_text.set("Contact book")

# enciphering button action after pressing
def encipher_press_btn():
    encipher__btn.destroy()
    decipher__btn.destroy()
    enter__btn__encipher.grid(column=0, row=2)
    contact_book_btn.grid(column=0, row=3)

    text_box_message.grid(column=1, row=2)
    text_box_message.insert(0, "Enter your message here")
    text_box_n.grid(column=1, row=3)
    text_box_n.insert(0, "Enter 'n' value of the key")
    text_box_e.grid(column=1, row=4)
    text_box_e.insert(0, "Enter 'e' value of the key")

# deciphering button action after pressing
def decipher_press_btn():
    encipher__btn.destroy()
    decipher__btn.destroy()
    enter__btn__decipher.grid(column=2, row=2)
    text_box_message.grid(column=1, row=2)
    text_box_message.insert(0, "Enter your message here")


# get message decipher button action after pressing
def get_message_decipher():
    if text_box_message.get() == '':
        messagebox.showerror("Required Fields", "Please include all fields")
        return

    user_message = tk.Label(root, text=text_box_message.get())
    enter__btn__decipher.destroy()
    text_box_message.destroy()

    user_message_text = user_message.cget("text")
    deciphered_message = deciphering.decipher(user_message_text)
    enter__btn__decipher.destroy()

    output_box = tk.Text(root, height=10, width=80, padx=15, pady=15)
    output_box.grid(column=1, row=2)
    output_box.insert(1.0, deciphered_message)

def open_contact_book():
    contact_book = ContactBook(self)
    contact_book.grab_set()


# get message encipher button action after pressing
def get_message_encipher():

    if text_box_message.get() == '' or text_box_e.get() == '' or text_box_n.get() == '':
        messagebox.showerror("Required Fields", "Please include all fields")
        return

    user_message = tk.Label(root, text=text_box_message.get())
    n_label = tk.Label(root, text=text_box_n.get())
    e_label = tk.Label(root, text=text_box_e.get())

    contact_book_btn.destroy()
    enter__btn__decipher.destroy()
    text_box_message.destroy()
    text_box_n.destroy()
    text_box_e.destroy()

    n_value = int(n_label.cget("text"))
    e_value = int(e_label.cget("text"))
    user_message_text = user_message.cget("text")

    enciphered_message = enciphering.encipher(user_message_text, n_value, e_value)
    enter__btn__encipher.destroy()

    output_box = tk.Text(root, height=10, width=80, padx=15, pady=15)
    output_box.grid(column=1, row=2)
    output_box.insert(1.0, enciphered_message)


root.mainloop()
