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

    #write test to confirm if object is instanciated correctly


if __name__=if __name__ == "__main__":
    unittest.main()