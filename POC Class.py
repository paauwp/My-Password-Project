import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Management Console")

        self.wm_iconbitmap('C:/Python Scripts/settings.ico')
        
        self.geometry("300x140")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)

        self.ConsoleFrame=ttk.Frame(self, padding=(60,30))
        self.ConsoleFrame.grid()

        DbInput_button = ttk.Button(self, text="DB Input", command=self.dbInputWindow)
        DbInput_button.grid(row=0, column=0, sticky="W", padx=10, pady=10)
     
        Access_button = ttk.Button(self, text="Access", command=self.dbInputWindow)
        Access_button.grid(row=1, column=0, sticky="W", padx=10, pady=10)

        Quit_button = ttk.Button(self,text="Quit", command=self.quit)
        Quit_button.grid(row=2, column=0, sticky="W", padx=10, pady=10)

        self.mainloop()

    def quit(self):
        self.destroy()

    def dbInputWindow(self):
        pass
  

MngmtConsole = MainWindow()