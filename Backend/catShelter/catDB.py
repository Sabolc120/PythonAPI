import sqlite3

con = sqlite3.connect("catBase.db")
print("Database opened successfully")

con.execute(
    "create table cats (id INTEGER PRIMARY KEY AUTOINCREMENT, catName TEXT NOT NULL, catGender TEXT NOT NULL, catAge INTEGER NOT NULL)")

print("Table created successfully")

con.close()
