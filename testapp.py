import tkinter as tk
import ContactBook
from PIL import Image, ImageTk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)


    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(column=0, row=0)

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.text = tk.Label(self, text="This is the start page")
        self.text.grid(column=1, row=1)
        master.geometry("700x350")

        self.button = tk.Button(self, text="Open page one",
                  command=lambda: master.switch_frame(ContactBook.ContactBook))
        self.button.grid(column=1, row=2)




if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
