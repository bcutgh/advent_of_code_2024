# File: day3.py
# Author: Brad Cutler
# Date: September 27, 2025
# Description: Advent of Code 2024 Day 3

import ast # To convert a string to a list
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

def remove_corrupt_and_disabled_instructions(instruction_set):
    """
    Remove the corrupt and disabled mul values from an instruction set.

    Args:
        instruction_set (string): The original set of instructions

    Returns:
        string: The instruction set with corrupt and disabled values removed
    """
    instruction_set = "".join(instruction_set)
    regex = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    instructions = re.findall(regex, instruction_set)
    enabled = True # By default instructions are enabled (implicit 'do')
    enabled_instructions = "["
    for instruction in instructions:
        if instruction[0] == "do()":
            enabled = True
        elif instruction[0] == "don't()":
            enabled = False
        else:
            if enabled:
                if instruction[1] and instruction[2]: # Ensure values are set
                    enabled_instructions += "(" + instruction[1] + "," + instruction[2] + "),"
    enabled_instructions = enabled_instructions[:-1] # Chop off the last comma
    enabled_instructions += "]"
    return enabled_instructions

def main():
    """
    Main function to avoid using global variables
    """
    instruction_set = read_input_file("puzzle_input.txt")
    print(f"The instruction set is: {instruction_set}")

    # For part 1, remove any corrupt instructions
    valid_mul_instructions = remove_corrupt_values(instruction_set)
    result = 0
    for x, y in valid_mul_instructions:
        print(f"X: {x}")
        print(f"Y: {y}")
        result += int(x) * int(y)
    print(f"The part 1 result is {result}")

    # For part 2, remove any corrupt and disabled instructions
    valid_mul_instruction_string = remove_corrupt_and_disabled_instructions(instruction_set)
    instructions = ast.literal_eval(valid_mul_instruction_string) # Convert the string to a list
    print(f"The enabled instruction set is: {instructions}")
    result = 0
    for x, y in instructions:
        print(f"X: {x}")
        print(f"Y: {y}")
        result += int(x) * int(y)
    print(f"The part 2 result is {result}")

if __name__ == "__main__":
    main()


