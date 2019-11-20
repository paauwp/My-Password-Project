secret='sumba5postgress'
import psycopg2 as pg2
import tkinter as tk
from tkinter import ttk

def quit():
    global root
    print("Destroy Window")
    root.destroy()

def save():

    userN = user_name.get() # haal de tkinter string variable user_name op en converteer naar string userN
    passW = password.get() # haal de tkinter sting variable password op en converteer naar string passW

    # CODE OM DE CONNECTIE MET DE DATABASE TE LEGGEN
    conn =pg2.connect(database='password', user='postgres', password=secret)
    cur = conn.cursor()

    try:

        postgres_insert_query = """ INSERT INTO passwords (username, passwordhash) VALUES (%s,%s)"""
   
        record_to_insert = (userN, passW)
        cur.execute(postgres_insert_query, record_to_insert)
   
        conn.commit()
        count = cur.rowcount
        print (count, "Record inserted successfully into passwords table")

    except (Exception, pg2.Error) as error :
        if(conn):
            print("Failed to insert record into passwords table", error)

    finally:
        #closing database connection.
        if(conn):
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")

def venster():
    # CODE OM DATA IN DE TABEL TE PLAATSEN
    # Here we create an instances of the StringVar() class, which is to track the content of widgets

    # Setup the input Frame
    input_nameframe=ttk.Frame(root, padding = (5,10,20,0))
    input_nameframe.pack(fill="both")

    input_pswdframe=ttk.Frame(root,padding = (5,10,20,0))
    input_pswdframe.pack(fill="both")

    name_label = ttk.Label(input_nameframe, text="User Name: ")
    name_label.pack(side="left", padx=(12, 10))
    name_entry = ttk.Entry(input_nameframe, width=15, textvariable=user_name)
    name_entry.pack(side="left")
    name_entry.focus()

    name_label = ttk.Label(input_pswdframe, text="Password: ")
    name_label.pack(side="left", padx=(20, 10))
    name_entry = ttk.Entry(input_pswdframe, width=15, textvariable=password)
    name_entry.pack(side="left")

    # Implementeer INVOER button

    # Setup van de Button Frame
    button_frame=ttk.Frame(root, padding=(20,10))
    button_frame.pack(fill="both")

    # invoer_button = ttk.Button(button_frame, text="ENTER VALUES IN DATABASE", command=root.destroy)
    invoer_button = ttk.Button(button_frame, text="ENTER VALUES IN DATABASE", command=save)
    invoer_button.pack(side="left")

    quit_button = ttk.Button(button_frame, text="QUIT", command=root.destroy)
    quit_button.pack(side="left")
   
   
root = tk.Tk()
root.title("Pieter's Password Project")
#root.geometry("600x150")   
user_name = tk.StringVar()
password = tk.StringVar()
venster()
root.mainloop()
# NOG TE IMPLEMENTEREN - KORTE TERMIJN
# 01. BUTTON om te stoppen zonder iets in de database op te slaan
# 02. Nette positionering van de buttons
# 03. Output geslaagde database insert in Tkinter window
# 04. Converteren van code naar nette functies
# 05. Password Hash implementeren

# NOG TE IMPLEMENTEREN - BACKLOG
# 01. Access scherm met teruglezen en checken password uit de database
# 02. Volledige GUI