import sys
from unittest import TestCase

sys.path.insert(0, r'C:\Users\ruben\OneDrive\01. estudo\01_linguagem_programacao\02_python\estudos_python\tests\blog')

from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        blog = Blog("Test", "Test Author")

        self.assertEqual("Test", blog.title)
        self.assertEqual("Test Author", blog.author)
        self.assertListEqual([], blog.posts)
        self.assertEqual(len([]), len(blog.posts))

    def test_repr(self):
        blog1 = Blog("Test", "Test Author")
        blog2 = Blog("My Day", "Rolph")

        self.assertEqual(blog1.__repr__(), "Test by Test Author (0 posts)")
        self.assertEqual(blog2.__repr__(), "My Day by Rolph (0 posts)")

    def test_multiple_posts(self):
        blog1 = Blog("Test", "Test Author")
        blog1.posts = ["Another test"]

        self.assertEqual(blog1.__repr__(), "Test by Test Author (1 posts)")


if __name__ == "__main__":
    import unittest

    unittest.main()
