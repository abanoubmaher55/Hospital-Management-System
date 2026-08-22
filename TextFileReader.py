
"""
Text File Reader Module
-----------------------
This module provides functionality to read, process, and analyze plain text
files. It allows users to inspect file content and compute structural
metrics such as line, word, and character counts.
"""


class TextFileReader:
    """
    A class that encapsulates operations for reading and analyzing text files.

    Attributes:
        file_path (str): The file path to the text document.
        content (str): The string content loaded from the target file.
    """

    def __init__(self, file_path: str):
        """
        Initializes the TextFileReader instance with a target file path.

        Args:
            file_path (str): The path to the text file to be read.
        """
        self.file_path = file_path
        self.content = ""

    def read_file(self):
        """
        Reads the entire contents of the text file and stores it in the content attribute.

        Returns:
            None
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                self.content = file.read()
        except FileNotFoundError:
            print(f"Error: The file at '{self.file_path}' was not found.")
            self.content = ""
        except IOError as e:
            print(f"Error reading file: {e}")
            self.content = ""

    def count_lines(self) -> int:
        """
        Counts the total number of lines in the loaded text file.

        Returns:
            int: The total number of lines.
        """
        if not self.content:
            return 0
        return len(self.content.splitlines())

    def count_words(self) -> int:
        """
        Counts the total number of words in the loaded text file.

        Returns:
            int: The total number of words separated by whitespace.
        """
        return len(self.content.split())

    def count_characters(self) -> int:
        """
        Counts the total number of characters in the loaded text file.

        Returns:
            int: The total character count including whitespace and newlines.
        """
        return len(self.content)

    def display_content(self):
        """
        Prints the loaded file content to the standard console output.

        Returns:
            None
        """
        if self.content:
            print(self.content)
        else:
            print("Content is empty or file has not been read yet.")


if __name__ == "__main__":
    test_file = "sample.txt"

    #testing
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("Hello World!\nWelcome to Python OOP.\nThis tests the TextFileReader class.")

    reader = TextFileReader(test_file)
    reader.read_file()

    print("File Content:")
    reader.display_content()

    print("\nFile Statistics:")
    print(f"Total Lines:      {reader.count_lines()}")
    print(f"Total Words:      {reader.count_words()}")
    print(f"Total Characters: {reader.count_characters()}")