from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def get_author_by_id(author_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
    author_data = cursor.fetchone()
    conn.close()
    
    if author_data:
        return Author(author_data["id"], author_data["name"])
    return None

def get_magazine_by_id(magazine_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM magazines WHERE id = ?", (magazine_id,))
    magazine_data = cursor.fetchone()
    conn.close()
    
    if magazine_data:
        return Magazine(magazine_data["id"], magazine_data["name"], magazine_data["category"])
    return None

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create an author
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    author_id = cursor.lastrowid  # Use this to fetch the id of the newly created author

    # Create a magazine
    cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (magazine_name, magazine_category))
    magazine_id = cursor.lastrowid  # Use this to fetch the id of the newly created magazine

    # Create an article
    cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                   (article_title, article_content, author_id, magazine_id))

    conn.commit()

    # Query the database for inserted records. 
    # The following fetch functionality should probably be in their respective models

    cursor.execute('SELECT * FROM magazines')
    magazines = cursor.fetchall()

    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()

    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()

    conn.close()

    # Display results
    print("\nMagazines:")
    for magazine in magazines:
        # Fetch the Magazine instance
        magazine_instance = get_magazine_by_id(magazine["id"])
        print(magazine_instance)

    print("\nAuthors:")
    for author in authors:
        # Fetch the Author instance
        author_instance = get_author_by_id(author["id"])
        print(author_instance)

    print("\nArticles:")
    for article in articles:
        # Fetch the Author and Magazine instances
        article_instance = Article(article["id"], author_instance, magazine_instance, article["title"])
        print(article_instance)
    return None

if __name__ == "__main__":
    main()
