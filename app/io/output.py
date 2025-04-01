def print_to_console(text):
    """Prints text to the console.

    Args:
        text (str): The text to be printed.
    """
    print(text)


def write_to_file(filepath, text):
    """Writes text to a file using Python's built-in capabilities.

    Args:
        filepath (str): The path to the file where text should be written.
        text (str): The text to be written to the file.
    """
    with open(filepath, "a", encoding="utf-8") as file:
        file.write(text + "\n")



