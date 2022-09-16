from scripts.preprocess import Preporcess
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join("./scripts")))


class TestPromptGeneration(unittest.TestCase):

    def setUp(self):
        self.prp = Preporcess()

    def test_clean_test_token(self):
        self.assertEqual(
            self.prp.clean_test_token(['\nToken1\nToken2']), 'token1;token2')

    def test_clean_extracted_token(self):
        self.assertEqual(
            self.prp.clean_extracted_token(['\nToken1\nToken2---']), 'token1;token2')


if __name__ == "__main__":
    unittest.main()
