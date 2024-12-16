from database.connection import get_db_connection

class Author:
    def __init__(self, id=None, name=None):
        if not isinstance(name, str) or len(name) <= 0:
            raise ValueError("Name must be a non-empty string.")

        self._name = name

        if id is None:  # If no id is provided, create a new record
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
            self._id = cursor.lastrowid
            conn.commit()
            conn.close()
        else:
            self._id = id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM articles
            WHERE author_id = ?
        """, (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON a.magazine_id = m.id
            WHERE a.author_id = ?
        """, (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines

    def __str__(self):
        return f"Author(id={self.id}, name='{self.name}')"
