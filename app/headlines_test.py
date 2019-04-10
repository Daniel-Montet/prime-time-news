import unittest
from models import headlines
Headline = headlines.Headline


class HeadlineTest(unittest.TestCase):
    """
    Test class to test behaviour of Headlines class
    """

    def setUp(self):
        self.news_headline= Headline()

    def test_instance(self):
        self.assertTrue(isinstance(self.news_headline,Headline))