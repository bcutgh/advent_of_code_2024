# File: day1.py
# Author: Brad Cutler
# Date: September 24, 2025
# Description: Demonstrate clean, readable, well documented Python code
#              following PEP 8 style guidelines

def calculate_distance_apart(location_id_1, location_id_2):
    distance_apart = int(location_id_1) - int(location_id_2)
    if (distance_apart < 0):
        distance_apart *= -1 # Always use positive numbers
    return distance_apart

def calculate_total_distance_apart():
    """
    Calculte the answer for part 1 of the challenge - the total distance
    between the locations in each list
    """
    total_distance_apart = 0
    list1, list2 = read_input_file("puzzle_input.txt");
    # Sort the location ids so they can be compared
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        total_distance_apart += calculate_distance_apart(list1[i], list2[i])
    print(f"The total distance betwen the lists: {total_distance_apart}")

def read_input_file(file_name):
    """
    Read data from a file.

    Args:
        file_name (string): The name of the file to read.

    Returns:
        list: The list of data.
    """
    list1 = []
    list2 = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip() # Remove leading/trailing whitespace/newlines
            data = line.split()
            list1.append(data[0])
            list2.append(data[1])
        return list1, list2 

def main():
    """
    Main function to avoid using global variables
    """
    calculate_total_distance_apart() # Calculate the answer for part 1

if __name__ == "__main__":
    main()


