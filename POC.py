import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Management Console")

        # Places the icon in the window
        self.wm_iconbitmap('C:/Python Projects/My Password Project/settings.ico')     
        
        self.geometry("420x500")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)

        self.ConsoleFrame=ttk.Frame(self, padding=(60,30))
        self.ConsoleFrame.grid()

        self.ConsoleFrame2=ttk.Frame(self, padding=(10,10))
        self.ConsoleFrame2.grid()

        DbInput_button = ttk.Button(self.ConsoleFrame, text="DB Input", command=self.dbInputWindow)
        DbInput_button.grid(row=0, column=0, sticky="NESW", padx=10)
     
        Access_button = ttk.Button(self.ConsoleFrame, text="Access", command=self.dbInputWindow)
        Access_button.grid(row=0, column=1, sticky="NESW", padx=10)

        Quit_button = ttk.Button(self.ConsoleFrame,text="Quit", command=self.quit)
        Quit_button.grid(row=0, column=2, sticky="NESW", padx=10)

        # Places the Postgress image in the window
        # For demonstration purpose I will use the file pointer method here

        with open("postgress.png", "r") as f:
            print(f)

        image = Image.open('C:/Python Projects/My Password Project/postgress.png')
        
        photo = ImageTk.PhotoImage(image)
        picture_text = ttk.Label(self.ConsoleFrame2,image=photo, compound="center")
        picture_text.grid(row=0, column=0, padx=10)  

        self.mainloop()

    def quit(self):
        self.destroy()

    def dbInputWindow(self):
        pass
  
MngmtConsole = MainWindow()