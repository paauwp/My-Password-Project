import tkinter as tk
from tkinter import ttk

def Window1():
    def QuitWindow1():
        root1.destroy()

    root1.title("Management Console")
    main = ttk.Frame(root1, padding=(40, 20))
    main.grid()

    greet_button = ttk.Button(main, text="DB Input", command=Window2, style="PomodoroButton.TButton")
    greet_button.grid(row=0, column=0, sticky="EW", padx=10)

    greet_button = ttk.Button(main, text="Frame2", command=Window2, style="PomodoroButton.TButton")
    greet_button.grid(row=0, column=1, sticky="EW", padx=10)

    greet_button = ttk.Button(main, text="Frame3", command=Window2, style="PomodoroButton.TButton")
    greet_button.grid(row=0, column=2, sticky="EW", padx=10)

    greet_button = ttk.Button(main, text="quit", command=QuitWindow1, style="PomodoroButton.TButton")
    greet_button.grid(row=0, column=3, sticky="EW", padx=10)

    root1.mainloop()

def Window2():
    def quit():
        root2.destroy()

    root1.destroy()
    root2=tk.Tk()
    root2.geometry("600x400")
    root2.resizable(False, False)
    root2.title("DataBase Input")
    main2 = ttk.Frame(root2, padding=(40, 20))
    main2.grid()

    greet_button = ttk.Button(main2, text="Quit", command=quit, style="PomodoroButton.TButton")
    greet_button.grid(row=0, column=2, sticky="EW", padx=10)

    root2.mainloop()


root1 = tk.Tk()
root1.resizable(False, False)

Window1()