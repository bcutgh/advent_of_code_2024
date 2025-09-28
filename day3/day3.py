# File: day3.py
# Author: Brad Cutler
# Date: September 27, 2025
# Description: Advent of Code 2024 Day 3

import re # We'll need the regular expression library

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
        instruction_set = str(instruction_set)
        instruction_set.strip() # Remove leading/trailing whitespace/newlines
        return instruction_set

def remove_corrupt_values(instruction_set):
    """
    Remove the corrupt mul values from an instruction set.

    Args:
        instruction_set (string): The original set of instructions

    Returns:
        string: The instruction set with corrupt values removed
    """
    regex_ignore_corrupt_values = r"mul\((\d{1,3}),(\d{1,3})\)"
    valid_mul_instructions = re.findall(regex_ignore_corrupt_values, instruction_set)
    print(f"\nThe valid mul instructions are: {valid_mul_instructions}")
    return valid_mul_instructions

def main():
    """
    Main function to avoid using global variables
    """
    instruction_set = read_input_file("puzzle_input.txt")
    print(f"The instruction_set is: {instruction_set}")

    valid_mul_instructions = remove_corrupt_values(instruction_set)

    result = 0
    for x, y in valid_mul_instructions:
        print(f"X: {x}")
        print(f"Y: {y}")
        result += int(x) * int(y)
    print(f"The result is {result}")

if __name__ == "__main__":
    main()


