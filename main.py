from app.io.input import read_from_console, read_from_file, read_from_file_pandas
from app.io.output import print_to_console, write_to_file

def main():
    """Main function that processes text and outputs it to the console and a file."""
    test1 = read_from_console()
    test2 = read_from_file("data/input.txt")
    test3 = read_from_file_pandas("data/input.txt")

    print_to_console(test1)
    print_to_console(test2)
    print_to_console(test3)

    write_to_file("data/output.txt", test1)
    write_to_file("data/output.txt", test2)
    write_to_file("data/output.txt", test3)


if __name__ == "__main__":
    main()

