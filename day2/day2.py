# File: day2.py
# Author: Brad Cutler
# Date: September 25, 2025
# Description: Advent of Code 2024 Day 2



def main():
    """
    Main function to avoid using global variables
    """

 def read_input_file(file_name):
    """
    Read data from a file.

    Args:
        file_name (string): The name of the file to read.

    Returns:
        list: The list of data.
    """
    list = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip() # Remove leading/trailing whitespace/newlines
            data = line.split()
            list.append(int(data[0]))
        return list1

if __name__ == "__main__":
    main()


