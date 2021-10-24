import tkinter as tk
from tkinter import messagebox
from db import Database
import testapp
# defining database
db = Database('contacts.db')


# gui contact book class

class ContactBook(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title('Contact Book')
        # size
        master.geometry("700x350")
        self._frame = 1
        # create widgets
        self.create_widgets()
        # init selected item var
        self.selected_item = 0
        # populate initial list
        self.populate_list()


    def create_widgets(self):
        # name
        self.name_text = tk.StringVar()
        self.name_label = tk.Label(self.master, text='Name', pady=20)
        self.name_label.grid(row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(self.master, textvariable=self.name_text)
        self.name_entry.grid(row=0, column=1)

        # surname
        self.surname_text = tk.StringVar()
        self.surname_label = tk.Label(self.master, text='Surname')
        self.surname_label.grid(row=0, column=2, sticky=tk.W)
        self.surname_entry = tk.Entry(self.master, textvariable=self.surname_text)
        self.surname_entry.grid(row=0, column=3)

        # n
        self.n_text = tk.StringVar()
        self.n_label = tk.Label(self.master, text='Number "n" ')
        self.n_label.grid(row=1, column=0, sticky=tk.W)
        self.n_entry = tk.Entry(self.master, textvariable=self.n_text)
        self.n_entry.grid(row=1, column=1)

        # e
        self.e_text = tk.StringVar()
        self.e_label = tk.Label(self.master, text='Number "e" ')
        self.e_label.grid(row=1, column=2, sticky=tk.W)
        self.e_entry = tk.Entry(self.master, textvariable=self.e_text)
        self.e_entry.grid(row=1, column=3)

        # listbox
        self.contacts_list = tk.Listbox(self.master, height=12, width=70, border=0)
        self.contacts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

        # create scrollbar
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=3, column=3)
        # set scroll to listbox
        self.contacts_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.contacts_list.yview())

        # bind select
        self.contacts_list.bind('<<ListboxSelect>>', self.select_item)

        # buttons
        self.add_btn = tk.Button(self.master, text="Add Contact", width=12, command=self.add_item)
        self.add_btn.grid(row=2, column=0, pady=20)

        self.remove_btn = tk.Button(self.master, text="Remove Contact", width=12, command=self.remove_item)
        self.remove_btn.grid(row=2, column=1)

        self.update_btn = tk.Button(self.master, text="Update Contact", width=12, command=self.update_item)
        self.update_btn.grid(row=2, column=2)

        self.clear_btn = tk.Button(self.master, text="Clear Input", width=12, command=self.clear_text)
        self.clear_btn.grid(row=2, column=3)

        self.send_message_btn = tk.Button(self.master, text="Send Message", command=self.send_message, width=12)
        self.send_message_btn.grid(row=3, column=4)

    def populate_list(self):
        # Delete items before update
        self.contacts_list.delete(0, tk.END)
        for row in db.fetch():
            self.contacts_list.insert(tk.END, row)

    def add_item(self):
        # user validation
        if self.name_text.get() == '' or self.surname_text == '' or self.n_text.get() == '' or self.e_text.get() == '':
            messagebox.showerror("Required Fields", "Please include all fields")
            return

        # inserting into db
        db.insert(self.name_text.get(), self.surname_text.get(), self.n_text.get(), self.e_text.get())

        # clear list
        self.contacts_list.delete(0, tk.END)
        # inserting into list
        self.contacts_list.insert(tk.END, (self.name_text.get(), self.surname_text.get(), self.n_text.get(), self.e_text.get()))
        self.clear_text()
        self.populate_list()

    def select_item(self, event):
        try:
            # get index
            index = self.contacts_list.curselection()[0]
            # get selected item
            self.selected_item = self.contacts_list.get(index)

            # add text to entries
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, self.selected_item[1])
            self.surname_entry.delete(0, tk.END)
            self.surname_entry.insert(tk.END, self.selected_item[2])
            self.n_entry.delete(0, tk.END)
            self.n_entry.insert(tk.END, self.selected_item[3])
            self.e_entry.delete(0, tk.END)
            self.e_entry.insert(tk.END, self.selected_item[4])

        except IndexError:
            pass

    def remove_item(self):
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()

    def update_item(self):
        db.update(self.selected_item[0], self.name_text.get(), self.surname_text.get(), self.n_text.get(), self.e_text.get())
        self.populate_list()

    def clear_text(self):
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        self.n_entry.delete(0, tk.END)
        self.e_entry.delete(0, tk.END)

    def send_message(self):
        self.n_value = self.selected_item[3]
        self.e_value = self.selected_item[4]
        self.master.switch_frame(testapp.StartPage)





# root = tk.Tk()
# contact_book = ContactBook(master=root)
# contact_book.mainloop()
