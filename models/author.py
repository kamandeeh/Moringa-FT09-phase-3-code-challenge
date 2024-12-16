from database.connection import get_db_connection


class Author:
    def __init__(self, id=None, name=None):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Author name must be a non-empty string.")
        
        self._name = name

        if id is None:  # Create a new record
            conn = get_db_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
                self._id = cursor.lastrowid
                conn.commit()
            finally:
                conn.close()
        else:  # Use existing record
            self._id = id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @staticmethod
    def get_author_by_id(author_id):
        """Fetch an author by their ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
            row = cursor.fetchone()
            if row:
                return Author(id=row["id"], name=row["name"])
            return None
        finally:
            conn.close()

    def update_name(self, new_name):
        """Update the name of an author."""
        if not isinstance(new_name, str) or len(new_name.strip()) == 0:
            raise ValueError("New name must be a non-empty string.")
        
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (new_name, self.id))
            conn.commit()
            self._name = new_name  # Update instance variable
        finally:
            conn.close()

    def delete_author(self):
        """Delete the author from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM authors WHERE id = ?", (self.id,))
            conn.commit()
        finally:
            conn.close()

    def __str__(self):
        return f"Author(id={self.id}, name='{self.name}')"
