secret='sumba5postgress'
import psycopg2 as pg2


# CODE OM DE CONNECTIE MET DE DATABASE TE LEGGEN
conn =pg2.connect(database='password', user='postgres', password=secret)
cur = conn.cursor()


# CODE OM GEBRUKERSINPUT VOOR USERNAME EN PASSWORD TE KRIJGEN
usrname = input("What is your username: ")
password = input("What is your password: ")


# CODE OM DATA IN DE TABEL TE PLAATSEN
try:
   
   postgres_insert_query = """ INSERT INTO passwords (username, passwordhash) VALUES (%s,%s)"""
   
   record_to_insert = ("pieter.paauw@gmail.com", "2F@6kkhr20")
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