secret='sumba5postgress'
import psycopg2 as pg2
import tkinter as tk
from tkinter import ttk

# CODE OM DE CONNECTIE MET DE DATABASE TE LEGGEN
conn =pg2.connect(database='password', user='postgres', password=secret)
cur = conn.cursor()

# CODE OM GEBRUKERSINPUT VOOR USERNAME EN PASSWORD TE KRIJGEN
#usrname = input("What is your username: ")
#password = input("What is your password: ")

root = tk.Tk()
root.title("My Password Project")
root.geometry("600x400")

# Here we create an instances of the StringVar() class, which is to track the content of widgets
user_name = tk.StringVar()
password = tk.StringVar()

name_label = ttk.Label(root, text="User Name: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()

name_label = ttk.Label(root, text="Password: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(root, width=15, textvariable=password)
name_entry.pack(side="left")

# Implementeer INVOER button
invoer_button = ttk.Button(root, text="ENTER VALUES IN DATABASE", command=root.destroy)
invoer_button.pack(side="bottom")

root.mainloop()

# CODE OM DATA IN DE TABEL TE PLAATSEN
userN = user_name.get() # haal de tkinter string variable user_name op en converteer naar string userN
passW = password.get() # haal de tkinter sting variable password op en converteer naar string passW

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


# NOG TE IMPLEMENTEREN - KORTE TERMIJN
# 01. BUTTON om te stoppen zonder iets in de database op te slaan
# 02. Nette positionering van de buttons
# 03. Output geslaagde database insert in Tkinter window
# 04. Converteren van code naar nette functies
