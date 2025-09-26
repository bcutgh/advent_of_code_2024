# File: day1.py
# Author: Brad Cutler
# Date: September 24, 2025
# Description: Advent of Code 2024 Day 1

def calculate_distance_apart(location_id_1, location_id_2):
    """
    Calculate the distance 2 locations are apart

    Args:
        location_id_1 (int): The first location id.
        location_id_2 (int): The second location id.

    Returns:
        int: The distance the 2 location ids are apart.
    """
    distance_apart = int(location_id_1) - int(location_id_2)
    if (distance_apart < 0):
        distance_apart *= -1 # Use the absolute value
    return distance_apart

def calculate_total_distance_apart():
    """
    Calculate the answer for part 1 of the challenge - the total distance
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

def calculate_total_similarity_score():
    """
    Calculate the total similarity score
    """
    dict_number_occurence = {}
    total_similarity_score = 0
    list1, list2 = read_input_file("puzzle_input.txt");
    # Count how many times numbers occur in the 2nd list
    for x in list2:
        if x not in dict_number_occurence:
            dict_number_occurence[x] = 1
        else:
            dict_number_occurence[x] += 1
    for x in list1:
        if x in dict_number_occurence:
            occurence_count = x * dict_number_occurence[x]
            total_similarity_score += occurence_count
    print(f"The total similarity score betwen the lists: {total_similarity_score}")

def read_input_file(file_name):
    """
    Read data from a file.

    Args:
        file_name (string): The name of the file to read.

    Returns:
        list1: The 1st list of data.
        list2: The 2nd list of data.
    """
    list1 = []
    list2 = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip() # Remove leading/trailing whitespace/newlines
            data = line.split()
            list1.append(int(data[0]))
            list2.append(int(data[1]))
        return list1, list2

def main():
    """
    Main function to avoid using global variables
    """
    calculate_total_distance_apart() # Calculate the answer for part 1
    calculate_total_similarity_score() # Calculate the answer for part 2

if __name__ == "__main__":
    main()


