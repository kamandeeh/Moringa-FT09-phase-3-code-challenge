from database.connection import get_db_connection


class Magazine:
    def __init__(self, id=None, name=None, category=None):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Magazine name must be a non-empty string.")
        if not isinstance(category, str) or len(category.strip()) == 0:
            raise ValueError("Magazine category must be a non-empty string.")

        self._name = name
        self._category = category

        if id is None:  # Create a new record
            conn = get_db_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
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

    @property
    def category(self):
        return self._category

    @staticmethod
    def get_magazine_by_id(magazine_id):
        """Fetch a magazine by its ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM magazines WHERE id = ?", (magazine_id,))
            row = cursor.fetchone()
            if row:
                return Magazine(id=row["id"], name=row["name"], category=row["category"])
            return None
        finally:
            conn.close()

    def update_category(self, new_category):
        """Update the category of the magazine."""
        if not isinstance(new_category, str) or len(new_category.strip()) == 0:
            raise ValueError("New category must be a non-empty string.")
        
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE magazines SET category = ? WHERE id = ?", (new_category, self.id))
            conn.commit()
            self._category = new_category  # Update instance variable
        finally:
            conn.close()

    def delete_magazine(self):
        """Delete the magazine from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM magazines WHERE id = ?", (self.id,))
            conn.commit()
        finally:
            conn.close()

    def __str__(self):
        return f"Magazine(id={self.id}, name='{self.name}', category='{self.category}')"