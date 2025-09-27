# File: day3.py
# Author: Brad Cutler
# Date: September 27, 2025
# Description: Advent of Code 2024 Day 3

def read_input_file(file_name):
    """
    Read data from a file.

    Args:
        file_name (string): The name of the file to read.

    Returns:
        string: The instruction set for the shopkeeper's computer
    """
    with open(file_name, "r") as file:
        instruction_set = file.readlines()
        return instruction_set

def main():
    """
    Main function to avoid using global variables
    """
    instruction_set = read_input_file("puzzle_input.txt")
    print(f"The instruction_set is: {instruction_set}")

if __name__ == "__main__":
    main()


