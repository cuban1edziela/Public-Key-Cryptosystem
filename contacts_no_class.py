from tkinter import *
from db import Database
from tkinter import messagebox

db = Database('contacts.db')


def populate_list():
    contacts_list.delete(0, END)
    for row in db.fetch():
        contacts_list.insert(END, row)


def add_item():
    if name_text.get() == '' or surname_text == '' or n_text.get() =='' or e_text.get()=='':
        messagebox.showerror("Required Fields", "Please include all fields")
        return

    db.insert(name_text.get(), surname_text.get(), n_text.get(), e_text.get())
    contacts_list.delete(0, END)
    contacts_list.insert(END, (name_text.get(), surname_text.get(), n_text.get(), e_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:

        global selected_item
        index = contacts_list.curselection()[0]
        selected_item = contacts_list.get(index)

        name_entry.delete(0, END)
        name_entry.insert(END, selected_item[1])
        surname_entry.delete(0, END)
        surname_entry.insert(END, selected_item[2])
        n_entry.delete(0, END)
        n_entry.insert(END, selected_item[3])
        e_entry.delete(0, END)
        e_entry.insert(END, selected_item[4])

    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], name_text.get(), surname_text.get(), n_text.get(), e_text.get())
    populate_list()

def clear_text():
    name_entry.delete(0, END)
    surname_entry.delete(0, END)
    n_entry.delete(0, END)
    e_entry.delete(0, END)




# create window object
app = Tk()

app.title('Contacts')
app.geometry('700x350')

# name
name_text = StringVar()
name_label = Label(app, text='Name', pady=20)
name_label.grid(row=0, column=0, sticky=W)
name_entry = Entry(app, textvariable=name_text)
name_entry.grid(row=0, column=1)

# surname
surname_text = StringVar()
surname_label = Label(app, text='Surname')
surname_label.grid(row=0, column=2, sticky=W)
surname_entry = Entry(app, textvariable=surname_text)
surname_entry.grid(row=0, column=3)

# n
n_text = StringVar()
n_label = Label(app, text='Number "n" ')
n_label.grid(row=1, column=0, sticky=W)
n_entry = Entry(app, textvariable=n_text)
n_entry.grid(row=1, column=1)

# e
e_text = StringVar()
e_label = Label(app, text='Number "e" ')
e_label.grid(row=1, column=2, sticky=W)
e_entry = Entry(app, textvariable=e_text)
e_entry.grid(row=1, column=3)

# listbox
contacts_list = Listbox(app, height=12, width=70, border=0)
contacts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20,padx=20)

# create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# set scroll to listbox
contacts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=contacts_list.yview())
# bind select
contacts_list.bind('<<ListboxSelect>>', select_item)

# buttons
add_btn = Button(app, text="Add Contact", width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text="Remove Contact", width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text="Update Contact", width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text="Clear Input", width=12, command=clear_text)
clear_btn.grid(row=2, column=3)


# populate date
populate_list()


# start
app.mainloop()




app.close()
