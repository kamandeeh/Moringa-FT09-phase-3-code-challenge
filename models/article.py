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

        if id is None:  # Create a new record
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
        else:  # Use existing record
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

    @staticmethod
    def get_article_by_id(article_id):
        """Fetch an article by its ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
            row = cursor.fetchone()
            if row:
                author = Author.get_author_by_id(row["author_id"])
                magazine = Magazine.get_magazine_by_id(row["magazine_id"])
                return Article(id=row["id"], author=author, magazine=magazine, title=row["title"])
            return None
        finally:
            conn.close()

    def update_title(self, new_title):
        """Update the title of the article."""
        if not isinstance(new_title, str) or len(new_title) < 5 or len(new_title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE articles SET title = ? WHERE id = ?", (new_title, self.id))
            conn.commit()
            self._title = new_title  # Update instance variable
        finally:
            conn.close()

    def delete_article(self):
        """Delete the article from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM articles WHERE id = ?", (self.id,))
            conn.commit()
        finally:
            conn.close()

    def __str__(self):
        return f"Article(id={self.id}, title='{self.title}', author='{self.author.name}', magazine='{self.magazine.name}')"
