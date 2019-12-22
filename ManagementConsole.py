import tkinter as tk
from tkinter import ttk

def Window1():
    def QuitWindow1():
        root1.destroy()

    root1.title("Management Console")
    main = ttk.Frame(root1, padding=(40, 20))
    main.grid()

    greet_button = ttk.Button(main, text="DB Input", command=dbInputWindow, style="PomodoroButton.TButton")
    greet_button.grid(row=0, column=0, sticky="EW", padx=10)

    greet_button = ttk.Button(main, text="Frame2", command=Window2, style="PomodoroButton.TButton")
    greet_button.grid(row=0, column=1, sticky="EW", padx=10)

    greet_button = ttk.Button(main, text="Frame3", command=Window2, style="PomodoroButton.TButton")
    greet_button.grid(row=0, column=2, sticky="EW", padx=10)

    greet_button = ttk.Button(main, text="QUIT", command=QuitWindow1, style="PomodoroButton.TButton")
    greet_button.grid(row=0, column=3, sticky="EW", padx=10)

    root1.mainloop()

def Window2():
    pass

def dbInputWindow():
    def quit():
        root2.destroy()

    #root1.destroy()
    root2=tk.Tk()
    root2.geometry("600x400")
    root2.resizable(False, False)
    root2.title("DataBase Input")
    root2.columnconfigure(0, weight=1)
    main2 = ttk.Frame(root2, padding=(40, 20))
    main2.grid()

    # -- Widgets --
    username_label = ttk.Label(root2, text="User Name:")
    #username_input = ttk.Entry(main2, width=10, textvariable=self.Op_username, font=(None, 15))  # None means "don't change the font".
    password_label = ttk.Label(root2, text="Password: ")
    #password_input = ttk.Entry(main2, width=10, textvariable=self.Op_password, font=(None, 15))  # None means "don't change the font".

    # -- Layout --
    username_label.grid(column=0, row=0, sticky="W", padx=10)
    #username_input.grid(column=1, row=0, sticky="EW")
    #username_input.focus()
    password_label.grid(column=0, row=1, sticky="W", padx=10)
    #password_input.grid(column=1, row=1, sticky="EW")
    
    greet_button = ttk.Button(main2, text="QUIT", command=quit, style="PomodoroButton.TButton")
    greet_button.grid(column=0, row=3, sticky="EW", padx=10)

    root2.mainloop()


root1 = tk.Tk()
root1.resizable(False, False)

Window1()