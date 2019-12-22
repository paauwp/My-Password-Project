import tkinter as tk
from tkinter import ttk

def MngmtConsoleWindow():
    
    def QuitWindow1():
        ConsoleWindow.destroy()

    ConsoleWindow = tk.Tk()
    ConsoleWindow.resizable(False, False)
    ConsoleWindow.title("Management Console")
    
    ConsoleFrame = ttk.Frame(ConsoleWindow, padding=(40, 20))
    ConsoleFrame.grid()

    dbinput_button = ttk.Button(ConsoleFrame, text="DB Input", command=dbInputWindow, style="PomodoroButton.TButton")
    dbinput_button.grid(row=0, column=0, sticky="EW", padx=10)

    action2_button = ttk.Button(ConsoleFrame, text="Frame2", command=Window2, style="PomodoroButton.TButton")
    action2_button.grid(row=0, column=1, sticky="EW", padx=10)

    action3_button = ttk.Button(ConsoleFrame, text="Frame3", command=Window2, style="PomodoroButton.TButton")
    action3_button.grid(row=0, column=2, sticky="EW", padx=10)

    quit_button = ttk.Button(ConsoleFrame, text="Quit", command=QuitWindow1, style="PomodoroButton.TButton")
    quit_button.grid(row=0, column=3, sticky="EW", padx=10)

    ConsoleWindow.mainloop()

def Window2():
    pass

def dbInputWindow():
    
    def quit():
        DbInputWindow.destroy()

    username = tk.StringVar()
    DbInputWindow=tk.Tk()
    DbInputWindow.geometry("600x400")
    DbInputWindow.resizable(False, False)
    DbInputWindow.title("DataBase Input")
    DbInputFrame = ttk.Frame(DbInputWindow, padding=(20, 20))
    DbInputFrame.columnconfigure(0, weight=1)
    DbInputFrame.grid()

    # -- Widgets --
    username_label = ttk.Label(DbInputFrame, text="User Name:")
    username_label.grid(column=1, row=0, sticky="W", padx=10)
    
    username_input = ttk.Entry(DbInputWindow, width=10, textvariable=username)  # None means "don't change the font".
    username_input.grid(column=2, row=0, sticky="W")
    username_input.focus()
    
    #password_label = ttk.Label(DbInputFrame, text="Password: ")
    #password_input = ttk.Entry(main2, width=10, textvariable=self.Op_password, font=(None, 15))  # None means "don't change the font".

    #password_label.grid(column=0, row=1, sticky="W", padx=10)
    #password_input.grid(column=1, row=1, sticky="W")
    
    #greet_button = ttk.Button(DbInputFrame, text="Quit", command=quit, style="PomodoroButton.TButton")
    #greet_button.grid(column=0, row=3, sticky="W", padx=10)

    DbInputWindow.mainloop()


MngmtConsoleWindow()