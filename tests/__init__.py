import unittest
import os
from app.io.input import read_from_file, read_from_file_pandas

class TestFileReading(unittest.TestCase):
    """Test cases for file reading functions."""

    TEST_FILE_PATH = "input.txt"
    EMPTY_FILE_PATH = "empty_file.txt"
    NON_EXISTENT_FILE_PATH = "non_existent_file.txt"

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

    def test_read_from_file_normal(self):
        """Test if read_from_file correctly reads a standard text file."""
        content = read_from_file(self.TEST_FILE_PATH)
        expected_content = "Test line 1\nTest line 2\nTest line 3"
        self.assertEqual(content, expected_content)

    def test_read_from_file_empty(self):
        """Test if read_from_file returns an empty string when reading an empty file."""
        content = read_from_file(self.EMPTY_FILE_PATH)
        self.assertEqual(content, "")

    def test_read_from_file_non_existent(self):
        """Test if read_from_file raises a FileNotFoundError for a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            read_from_file(self.NON_EXISTENT_FILE_PATH)

if __name__ == "__main__":
    unittest.main()
