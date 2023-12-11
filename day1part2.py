# --- Part Two ---
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

#open file
day1_input = open("day1.txt", "r")

#read file

calibration_total = 0
calibration_number = 0
words_to_numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}


for line in day1_input.readlines():
    string_index = -1
    test_string = ''
    finished_string = ''
    for char in line:
        string_index += 1
        if char in words_to_numbers.values():
            finished_string += char
        else:
            test_string = line[string_index: string_index + 3]
            if test_string in words_to_numbers.keys():
                finished_string += words_to_numbers.get(test_string)
            else:
                test_string = line[string_index: string_index + 4]
                if test_string in words_to_numbers.keys():
                    finished_string += words_to_numbers.get(test_string)
                else:
                    test_string = line[string_index: string_index + 5]
                    if test_string in words_to_numbers.keys():
                        finished_string += words_to_numbers.get(test_string)
        
    #concatenate first and last numbers and make them int
    calibration_number = int(finished_string[0] + finished_string[-1])
    #add to the total
    calibration_total += calibration_number