secret='sumba5postgress'
import hashlib
import psycopg2 as pg2
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Name & Password input")
user_name = tk.StringVar()
password = tk.StringVar()

def hash_string(string):
        # Return the SHA-256 Hash of a given string
        return hashlib.sha256(string.encode('utf-8')).hexdigest()

def quit():
    global root
    print("Destroy Window")
    root.destroy()

def save():
    userN = user_name.get() # haal de tkinter string variable user_name op en converteer naar string userN
    passW = password.get() # haal de tkinter sting variable password op en converteer naar string passW

    # Code om connectie met de database te leggen
    conn =pg2.connect(database='password', user='postgres', password=secret)
    cur = conn.cursor()
    try:
        passWhash = hash_string(passW)
        print ("The hash is: ")
        print (passWhash)

        postgres_insert_query = """ INSERT INTO passwords (username, passwordhash) VALUES (%s,%s)"""
        
        record_to_insert = (userN, passWhash)
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
   
    # WIDGETS
    #Frames
    input_nameframe=ttk.Frame(root, padding = (5,10,20,0))
    input_pswdframe=ttk.Frame(root,padding = (5,10,20,0))
    #Labels
    name_label = ttk.Label(input_nameframe, text="User Name: ")
    name_entry = ttk.Entry(input_nameframe, width=15, textvariable=user_name)
    name_entry.focus()
    psswd_label = ttk.Label(input_pswdframe, text="Password: ")
    psswd_entry = ttk.Entry(input_pswdframe, width=15, textvariable=password)
    # Buttons
    button_frame=ttk.Frame(root, padding=(20,10))
    invoer_button = ttk.Button(button_frame, text="ENTER VALUES IN DATABASE", command=save)  
    quit_button = ttk.Button(button_frame, text="QUIT", command=root.destroy)

    # PACKING
    # Frames
    input_nameframe.pack(fill="both")
    input_pswdframe.pack(fill="both")
    # Labels
    name_label.pack(side="left")
    name_entry.pack(side="left", padx=(5,10))
    psswd_label.pack(side="left")
    psswd_entry.pack(side="left", padx=(12,10))
    #Buttons
    button_frame.pack(fill="both")  
    invoer_button.pack(side="left")
    quit_button.pack(side="left")

    

#MAIN   
venster()
root.mainloop()