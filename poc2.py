import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import hashlib
import psycopg2 as pg2
secret='sumba5postgress'


class dbInputWindowClass(tk.Tk):
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.user_name = tk.StringVar()
            self.password = tk.StringVar()

            self.title("DataBase Input Window")
            # Places the icon in the window
            self.wm_iconbitmap('C:/Python Projects/My Password Project/dbinput.ico')     
            self.geometry("420x500")
            self.resizable(False, False)
            self.columnconfigure(0, weight=1)

            self.ConsoleFrame=ttk.Frame(self, padding=(60,30))
            self.ConsoleFrame.grid()

            self.ConsoleFrame2=ttk.Frame(self, padding=(10,10))
            self.ConsoleFrame2.grid()

            name_label = ttk.Label(self.ConsoleFrame, text="User Name: ")
            name_entry = ttk.Entry(self.ConsoleFrame, width=15, textvariable=self.user_name)
            name_entry.focus()
            psswd_label = ttk.Label(self.ConsoleFrame, text="Password: ")
            psswd_entry = ttk.Entry(self.ConsoleFrame, width=15, textvariable=self.password)

            name_label.grid(row=0, column=1, sticky="NESW", padx=10)
            name_entry.grid(row=0, column=2, sticky="NESW", padx=10)
            
            #psswd_label.pack(side="left")
            #psswd_entry.pack(side="left", padx=(12,10))


        
        
            Return_button = ttk.Button(self.ConsoleFrame2,text="Return to Console", command=self.returnToConsole)
            Return_button.grid(row=0, column=2, sticky="NESW", padx=10)

            self.mainloop()

        def hash_string(string):
            # Return the SHA-256 Hash of a given string
            return hashlib.sha256(string.encode('utf-8')).hexdigest()

        
        def returnToConsole(self):
            self.destroy()
            MngmtConsole = MainWindow()



class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Management Console")

        # Setup of Window properties & Picture
        self.wm_iconbitmap('C:/Python Projects/My Password Project/settings.ico')     
        self.geometry("420x500")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.ConsoleFrame=ttk.Frame(self, padding=(60,30))
        self.ConsoleFrame.grid()
        self.ConsoleFrame2=ttk.Frame(self, padding=(10,10))
        self.ConsoleFrame2.grid()
        
        image = Image.open('C:/Python Projects/My Password Project/postgress.png')
        photo = ImageTk.PhotoImage(image)
        picture_text = ttk.Label(self.ConsoleFrame2,image=photo, compound="center")
        picture_text.grid(row=0, column=0, padx=10)  


        DbInput_button = ttk.Button(self.ConsoleFrame, text="DB Input", command=self.dbInput)
        DbInput_button.grid(row=0, column=0, sticky="NESW", padx=10)
     
        Access_button = ttk.Button(self.ConsoleFrame, text="Access", command=self.dbInput)
        Access_button.grid(row=0, column=1, sticky="NESW", padx=10)

        Quit_button = ttk.Button(self.ConsoleFrame,text="Quit", command=self.quit)
        Quit_button.grid(row=0, column=2, sticky="NESW", padx=10)

        # Places the Postgress image in the window
        # For demonstration purpose I will use the file pointer method here

        #with open("postgress.png", "r") as f:
            #print(f)

        self.mainloop()

    def quit(self):
        self.destroy()

    def dbInput(self):
        self.destroy()
        dbInputWindow = dbInputWindowClass()

    
MngmtConsole = MainWindow()