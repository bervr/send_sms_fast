import sqlite3

con = sqlite3.connect('wsgi_db.sqlite')
cur = con.cursor()
with open('create_db.sql', 'r') as file:
    text = file.read()
cur.executescript(text)
cur.close()
con.close()
