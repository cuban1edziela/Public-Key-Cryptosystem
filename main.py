from Functions import *
from Variables import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

# root = tk.Tk()

# canvas = tk.Canvas(root, width=600, height=300)
# canvas.grid(columnspan=3, rowspan=3)

# #logo
# logo = Image.open("logo.png")
# logo = ImageTk.PhotoImage(logo)
# logo_label = tk.Label(image=logo)
# logo_label.image = logo
# logo_label.grid(column=1, row=0)

# #instructions
# instructions = tk.Label(root, text = "Welcome to the Public Key Cryptosystem Program")
# instructions.grid(columnspan=3, column=0, row=1)

# #encipherbutton
# encipher_text = tk.StringVar()
# encipher__btn = tk.Button(root, textvariable=encipher_text, command=lambda:encipher_press_btn(), bg="#008037", fg="white", height=2, width=15)
# encipher_text.set("Encipher")
# encipher__btn.grid(column=0, row=2)

# #decipherbutton
# decipher_text = tk.StringVar()
# decipher__btn = tk.Button(root, textvariable=decipher_text, command=lambda:decipher_press_btn(), bg="#008037", fg="white", height=2, width=15)
# decipher_text.set("Decipher")
# decipher__btn.grid(column=1, row=2)

# #enciphering button action after pressing
# def encipher_press_btn():
#     encipher_text.set("loading")
#     import enciphering

# def decipher_press_btn():
#     decipher_text.set("loading")
#     import deciphering
    
#text box
# text_box = tk.Text(root, height=2, width=30, padx=15, pady=15)
# #text_box.insert(1.0)
# text_box.grid(column=1, row=3)

print("\n Welcome to thePublic Key Cryptosystem Program by Kuba Niedziela")
print("\n If you want to encipher a message press 0 and ENTER, to decipher, press 1 and ENTER")
check_user = int(input())

while(check_user != 0 and check_user != 1):
    print("Invalid numerical value. Enter 0 to encipher or 1 to decipher")
    check_user = int(input())

if(check_user == 0):
    import enciphering

if(check_user == 1):
    import deciphering

print("\n Thank you for using Public Key Cryptosystem Program")

# canvas = tk.Canvas(root, width=600, height=250)
# canvas.grid(columnspan=3)

# root.mainloop()