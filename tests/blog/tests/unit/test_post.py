from unittest import TestCase

import sys

sys.path.insert(0, r'C:\Users\ruben\OneDrive\01. estudo\01_linguagem_programacao\02_python\estudos_python\tests\blog')

from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        post = Post("Test", "Test Content")

        self.assertEqual("Test", post.title)
        self.assertEqual("Test Content", post.content)

    def test_json(self):
        post = Post("test", "test content")
        expected = {"title": "test", "content": "test content"}

        self.assertDictEqual(expected, post.json())


if __name__ == "__main__":
    import unittest

    unittest.main()
