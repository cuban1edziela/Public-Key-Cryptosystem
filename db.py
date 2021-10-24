import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name text, surname text, n text, e text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM contacts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, surname, n, e ):
        self.cur.execute("INSERT INTO contacts VALUES (NULL, ?, ?, ?, ?)", (name, surname, n, e))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM contacts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, name, surname, n, e):
        self.cur.execute("UPDATE contacts SET name = ?, surname = ?, n = ?, e = ? WHERE id = ?", (name, surname, n, e, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#
# db = Database("contacts.db")
# db.insert("Conor", "Sheridan", "711247", "84101")
# db.insert("Kuba", "Niedziela", "720553", "415")


