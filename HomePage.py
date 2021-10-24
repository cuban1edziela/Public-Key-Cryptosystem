import tkinter as tk
from PIL import Image, ImageTk
from db import Database
from ContactBook import *

db = Database('contact_list.db')


class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        master.iconbitmap("icon.ico")
        master.title('NON RSA')

        # size
        master.geometry("600x660")
        self. create_widgets()

    def create_widgets(self):

        # logo
        self.logo = Image.open("logo.png")
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(image=self.logo)
        self.logo_label.image = self.logo
        self.logo_label.grid(column=1, row=0)

        # welcome message
        self.welcome_message = tk.Label(self.master, text="Welcome to the Public Key Cryptosystem Program", pady=50)
        self.welcome_message.grid(column=1, row=2)

        # encipher button
        self.encipher_text = tk.StringVar()
        self.encipher__btn = tk.Button(self.master, textvariable=self.encipher_text, command=lambda: self.encipher_press_btn(), bg="#008037",
                                  fg="white", height=2, width=15)
        self.encipher_text.set("Encipher")
        self.encipher__btn.grid(column=1, row=3, sticky=tk.W)

        # decipher button
        self.decipher_text = tk.StringVar()
        self.decipher__btn = tk.Button(self.master, textvariable=self.decipher_text, command=lambda: self.decipher_press_btn(), bg="#008037",
                                  fg="white", height=2, width=15)
        self.decipher_text.set("Decipher")
        self.decipher__btn.grid(column=2, row=3)


    # enciphering button action after pressing
    def encipher_press_btn(self):
        window = ContactBook(self)
        window.grab_set()


    # deciphering button action after pressing
    def decipher_press_btn(self):
        pass



        # # get message decipher button action after pressing
        # def get_message_decipher():
        #     if text_box_message.get() == '':
        #         messagebox.showerror("Required Fields", "Please include all fields")
        #         return
        #
        #     user_message = tk.Label(root, text=text_box_message.get())
        #     enter__btn__decipher.destroy()
        #     text_box_message.destroy()
        #
        #     user_message_text = user_message.cget("text")
        #     deciphered_message = deciphering.decipher(user_message_text)
        #     enter__btn__decipher.destroy()
        #
        #     output_box = tk.Text(root, height=10, width=80, padx=15, pady=15)
        #     output_box.grid(column=1, row=2)
        #     output_box.insert(1.0, deciphered_message)
        #
        #
        # # get message encipher button action after pressing
        # def get_message_encipher():
        #
        #
        #     n_value = ContactBook.message_contact_n
        #     e_value = ContactBook.message_contact_e
        #
        #     if text_box_message.get() == '' or text_box_e.get() == '' or text_box_n.get() == '':
        #         messagebox.showerror("Required Fields", "Please include all fields")
        #         return
        #     user_message = tk.Label(root, text=text_box_message.get())
        #     n_label = tk.Label(root, text=text_box_n.get())
        #     e_label = tk.Label(root, text=text_box_e.get())
        #
        #     enter__btn__decipher.destroy()
        #     text_box_message.destroy()
        #     text_box_n.destroy()
        #     text_box_e.destroy()
        #
        #     n_value = int(n_label.cget("text"))
        #     e_value = int(e_label.cget("text"))
        #     user_message_text = user_message.cget("text")
        #
        #     enciphered_message = enciphering.encipher(user_message_text, n_value, e_value)
        #     enter__btn__encipher.destroy()
        #
        #     output_box = tk.Text(root, height=10, width=80, padx=15, pady=15)
        #     output_box.grid(column=1, row=2)
        #     output_box.insert(1.0, enciphered_message)


root = tk.Tk()
home_page = HomePage(master=root)
home_page.mainloop()
