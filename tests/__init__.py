import unittest
import os
from app.io.input import read_from_file, read_from_file_pandas

class TestFileReading(unittest.TestCase):
    """Test cases for file reading functions."""

    TEST_FILE_PATH = "input.txt"

    @classmethod
    def setUpClass(cls):
        """Creates a test file before running tests."""
        with open(cls.TEST_FILE_PATH, "w", encoding="utf-8") as file:
            file.write("Test line 1\nTest line 2")

    @classmethod
    def tearDownClass(cls):
        """Deletes the test file after tests are completed."""
        if os.path.exists(cls.TEST_FILE_PATH):
            os.remove(cls.TEST_FILE_PATH)


if __name__ == "__main__":
    unittest.main()
