import tkinter as tk
import tkinter.font as font
from tkinter import ttk
import hashlib
import psycopg2 as pg2

secret='sumba5postgress'

class eK_tkTk_root(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Pieter's Password Project")
        O_PassWordInputFrame = eK_PasswordInputFrame(self, padding=(60,30))
        O_PassWordInputFrame.grid()
        #self.Op_frame=ttk.Frame(self, padding=(60,30))
        #self.Op_frame.grid()


class eK_PasswordInputFrame(ttk.Frame):
    def __init__(self, a_container, **kwargs):
        super().__init__(a_container, **kwargs)

        self.Op_username = tk.StringVar()
        self.Op_password = tk.StringVar()
    
        # -- Widgets --
        username_label = ttk.Label(self, text="User Name:")
        username_input = ttk.Entry(self, width=10, textvariable=self.Op_username, font=(None, 15))  # None means "don't change the font".
        password_label = ttk.Label(self, text="Password: ")
        password_input = ttk.Entry(self, width=10, textvariable=self.Op_password, font=(None, 15))  # None means "don't change the font".

        # -- Layout --
        username_label.grid(column=0, row=0, sticky="W")
        username_input.grid(column=1, row=0, sticky="EW")
        username_input.focus()
        password_label.grid(column=0, row=1, sticky="W")
        password_input.grid(column=1, row=1, sticky="EW")

        # -- Button(s) --
        input_button = ttk.Button(self,text="Input in DB", command=self.Save)
        input_button.grid(column=1, row=3, columnspan=2, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)
    
    def Save(self, *args):
        string ="test"
        hash = hashlib.sha256(string.encode('utf-8')).hexdigest()
        print (hash)


O_root = eK_tkTk_root()
font.nametofont("TkDefaultFont").configure(size=15)
O_root.columnconfigure(0, weight=1)

#O_root.bind("<Return>", calculate_feet)
#O_root.bind("<KP_Enter>", calculate_feet)

O_root.mainloop()