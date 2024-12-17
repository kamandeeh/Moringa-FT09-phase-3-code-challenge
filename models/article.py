from database.connection import get_db_connection  # Import database connection
from models.author import Author  # Import the Author class
from models.magazine import Magazine  # Import the Magazine class

class Article:
    def init(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

def __repr__(self):
    return f'<Article {self.title}>'

@property
def author(self):
    """Return the author of the article."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM authors WHERE id = ?', (self.author_id,))
    author_data = cursor.fetchone()
    conn.close()
    if author_data:
        return Author(author_data['id'], author_data['name'])
    return None

@property
def magazine(self):
    """Return the magazine of the article."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM magazines WHERE id = ?', (self.magazine_id,))
    magazine_data = cursor.fetchone()
    conn.close()
    if magazine_data:
        return Magazine(magazine_data['id'], magazine_data['name'], magazine_data['category'])
    return None
    


    # @staticmethod
    # def get_article_by_id(article_id):
    #     """Fetch an article by its ID."""
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     try:
    #         cursor.execute("SELECT * FROM articles id = ?", (article_id,))
    #         row = cursor.fetchone()
    #         if row:
    #             author = Author.get_author_by_id(row["author_id"])
    #             magazine = Magazine.get_magazine_by_id(row["magazine_id"])
    #             return Article(id=row["id"], author=author, magazine=magazine, title=row["title"])
    #         return None
    #     finally:
    #         conn.close()

    # def update_title(self, new_title):
    #     """Update the title of the article."""
    #     if not isinstance(new_title, str) or len(new_title) < 5 or len(new_title) > 50:
    #         raise ValueError("Title must be a string between 5 and 50 characters.")

    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     try:
    #         cursor.execute("UPDATE articles SET title = ? WHERE id = ?", (new_title, self.id))
    #         conn.commit()
    #         self._title = new_title  # Update instance variable
    #     finally:
    #         conn.close()

    # def delete_article(self):
    #     """Delete the article from the database."""
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     try:
    #         cursor.execute("DELETE FROM articles WHERE id = ?", (self.id,))
    #         conn.commit()
    #     finally:
    #         conn.close()

    # def __str__(self):
    #     return f"Article(id={self.id}, title='{self.title}', author='{self.author.name}', magazine='{self.magazine.name}')"
    
