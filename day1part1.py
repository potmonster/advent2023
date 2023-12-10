#open file
day1_input = open("C:/Coding/advent/day1.txt", "r")

#read file

calibration_total = 0
calibration_number = 0

for line in day1_input.readlines():
    #filter numbers from line
    line = ''.join(filter(str.isdigit, line))
    #concatenate first and last numbers and make them int
    calibration_number = int(line[0] + line[-1])
    #add to the total
    calibration_total += calibration_number