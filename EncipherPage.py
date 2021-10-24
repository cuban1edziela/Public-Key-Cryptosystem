import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from db import Database
import deciphering
import enciphering as ec


db = Database('contact_list.db')


class EncipherPage(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('600x600')
        self.title('Encipher Page')


        # textbox
        self.text_box_message = tk.Entry(self.master, width=80, borderwidth=2)
        self.text_box_e = tk.Entry(self.master, width=80, borderwidth=2)
        self.text_box_n = tk.Entry(self.master, width=80, borderwidth=2)
        self.text_box_message.grid(column=1, row=1)
        self.text_box_n.grid(column=1, row=2)
        self.text_box_e.grid(column=1, row=3)

        # enter button

        self.enter__btn = tk.Button(self.master, text="Enter", width=12, command=self.get_message())
        self.enter__btn.grid(column=2, row=1)

    def get_message(self):

        # if self.text_box_message.get() == '' or self.text_box_e.get() == '' or self.text_box_n.get() == '':
        #     messagebox.showerror("Required Fields", "Please include all fields")
        #     return

        self.user_message = tk.Label(self.master, text=self.text_box_message.get())
        self.n_label = tk.Label(self.master, text=self.text_box_n.get())
        self.e_label = tk.Label(self.master, text=self.text_box_e.get())

        self.enter__btn.destroy()
        self.text_box_message.destroy()
        self.text_box_n.destroy()
        self.text_box_e.destroy()

        self.n_value = int(self.n_label.cget("text"))
        self.e_value = int(self.e_label.cget("text"))
        self.user_message_text = self.user_message.cget("text")

        self.enciphered_message = ec.encipher(self.user_message_text, self.n_value, self.e_value)

        self.output_box = tk.Text(self.master, height=10, width=80, padx=15, pady=15)
        self.output_box.grid(column=1, row=2)
        self.output_box.insert(1.0, self.enciphered_message)


