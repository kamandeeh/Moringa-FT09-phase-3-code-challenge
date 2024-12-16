from database.connection import get_db_connection
from models.author import Author
from models.magazine import Magazine

class Article:
    def __init__(self, id=None, author=None, magazine=None, title=None):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")

        self._author = author
        self._magazine = magazine
        self._title = title

        if id is None:  # If no id is provided, create a new record
            conn = get_db_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO articles (title, author_id, magazine_id)
                    VALUES (?, ?, ?)
                """, (title, author.id, magazine.id))
                self._id = cursor.lastrowid
                conn.commit()
            finally:
                conn.close()
        else:
            self._id = id

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    def __str__(self):
        # Corrected __str__ implementation
        return f"Article(title='{self.title}', author='{self.author.name}', magazine='{self.magazine.name}')"
