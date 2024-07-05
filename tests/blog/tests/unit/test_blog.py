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


if __name__ == "__main__":
    import unittest

    unittest.main()
