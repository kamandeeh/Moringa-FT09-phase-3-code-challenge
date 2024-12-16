import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        # Create an author instance
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")
        self.assertEqual(author.id, 1)

    def test_article_creation(self):
        # Create supporting instances for the article
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        
        # Create the article instance
        article = Article(1, author, magazine, "Test Title")
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.author.name, "John Doe")
        self.assertEqual(article.magazine.name, "Tech Weekly")

    def test_magazine_creation(self):
        # Create a magazine instance
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")
        self.assertEqual(magazine.id, 1)

if __name__ == "__main__":
    unittest.main()
