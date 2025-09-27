# File: day2.py
# Author: Brad Cutler
# Date: September 25, 2025
# Description: Advent of Code 2024 Day 2

import math

def adjacent_levels_within_tolerance(report):
    """
    Check if all the levels in a report are within tolerance.

    Args:
        report (string): A string of levels to check.

    Returns:
        bool: True if all levels are within tolerance, otherise False.
    """
    levels = report.split()
    count = 0
    for level in levels:
        level = int(level)
        count += 1
        if count == len(levels):
            break
        next_level = int(levels[count])
        print(f"Checking on {level}: {report}")
        if math.fabs(level - next_level) < 1:
            print(f"Checking level {level} against next_level more than 1 {next_level} NOT acceptable: {report}")
            print(f"NOT Acceptable: {report}")
            return False
        elif math.fabs(level - next_level) > 3:
            print(f"Checking level {level} against next_level more than 3 {next_level} NOT acceptable: {report}")
            print(f"NOT Acceptable: {report}")
            return False
        if math.fabs(next_level - level) < 1:
            print(f"Checking level {level} against next_level more than 1 {next_level} NOT acceptable: {report}")
            print(f"NOT Acceptable: {report}")
            return False
        elif math.fabs(next_level - level) > 3:
            print(f"Checking level {level} against next_level more than 3 {next_level} NOT acceptable: {report}")
            print(f"NOT Acceptable: {report}")
            return False
    print(f"Acceptable: {report}")
    return True

def dampen(report):
    """
    Remove at most one bad record from a report and retest it.

    Args:
        report (string): A string of levels to work with.

    Returns:
        bool: True if dampening was successful.
    """
    separator = ' '
    original_report = str(report)
    original_levels = original_report.split()
    num_levels = len(original_levels)
    for index_to_delete in range(num_levels):
        test_levels = original_levels.copy()
        print(f"Testing a dampening by removing index {index_to_delete} from {original_report} which is {test_levels[index_to_delete]}")
        del test_levels[index_to_delete] # Remove one level from the report
        dampened_report = separator.join(test_levels)
        if levels_decreasing(dampened_report):
            if (adjacent_levels_within_tolerance(dampened_report)):
                print(f"Dampening successful for descreasing {dampened_report}")
                return True
        elif levels_increasing(dampened_report):
            if (adjacent_levels_within_tolerance(dampened_report)):
                print(f"Dampening successful for increasing {dampened_report}")
                return True
        print(f"Dampening was not successful for {original_report}")
    return False

def levels_decreasing(report):
    """
    Check if all the levels in a report are decreasing

    Args:
        report (string): A string of levels to check.

    Returns:
        bool: True if all levels are decreasing.
    """
    levels = report.split()
    previous_value = 1000000 # Set a high/valid start value
    for level in levels:
        if int(level) >= previous_value:
            print(f"NOT decreasing due to {level} in {report}")
            return False
        previous_value = int(level)
    print(f"Decreasing: {report}")
    return True

def levels_increasing(report):
    """
    Check if all the levels in a report are increasing

    Args:
        report (string): A string of levels to check.

    Returns:
        bool: True if all levels are increasing.
    """
    levels = report.split()
    previous_value = 0
    for level in levels:
        if (int(level) <= previous_value):
            print(f"Not increasing due to {level} in {report}")
            return False
        previous_value = int(level)
    print(f"Increasing: {report}")
    return True

def read_input_file(file_name):
    """
    Read data from a file.

    Args:
        file_name (string): The name of the file to read.

    Returns:
        list: The list of reports.
    """
    reports = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip() # Remove leading/trailing whitespace/newlines
            reports.append(line)
        return reports

def main():
    """
    Main function to avoid using global variables
    """
    reports = read_input_file("puzzle_input.txt")
    num_safe_reports = 0
    safe_report_found = False
    for report in reports:
        if levels_decreasing(report):
            if (adjacent_levels_within_tolerance(report)):
                num_safe_reports += 1
                safe_report_found = True
        elif levels_increasing(report):
            if (adjacent_levels_within_tolerance(report)):
                num_safe_reports += 1
                safe_report_found = True
        if not safe_report_found:
            dampened_report_success = dampen(report)
            if dampened_report_success:
                num_safe_reports += 1

    print(f"The number of safe reports is: {num_safe_reports}")

if __name__ == "__main__":
    main()


