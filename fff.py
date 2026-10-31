import sqlite3

db = sqlite3.connect("books.db")
cur = db.cursor()

cur.execute("CREATE TABLE books (title TEXT, author TEXT, year INTEGER)")

cur.execute("INSERT INTO books VALUES ('Harry Potter', 'Rowling', 1997)")
cur.execute("INSERT INTO books VALUES ('The Hobbit', 'Tolkien', 1937)")
cur.execute("INSERT INTO books VALUES ('1984', 'Orwell', 1949)")

cur.execute("SELECT * FROM books")
print(cur.fetchall())

cur.execute("SELECT * FROM books WHERE title = 'Harry Potter'")
print(cur.fetchall())

cur.execute("UPDATE books SET year = 2000 WHERE title = 'Harry Potter'")

cur.execute("DELETE FROM books WHERE title = '1984'")

db.commit()
db.close()