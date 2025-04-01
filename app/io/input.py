import pandas as pd

def read_from_console():
    """Reads text input from the console."""
    return input("Enter text: ")

def read_from_file(filepath):
    """Reads text from a file using Python's built-in capabilities.

    Args:
        filepath (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def read_from_file_pandas(filepath):
    """Reads text from a file using the pandas library.

    Args:
        filepath (str): The path to the file to be read.

    Returns:
        str: The content of the file as a single string with lines joined by newline characters.
    """
    df = pd.read_csv(filepath, header=None)
    return "\n".join(df[0].astype(str))
