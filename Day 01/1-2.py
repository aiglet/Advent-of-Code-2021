
# Open the data file and split it into lines
data = open("input.txt")
lines = data.readlines()

# PART TWO

def sonar_average(lines):
# Set up a counter
    counter = 0
    sum1 = (int(lines[0]) + int(lines[1]) + int(lines[2]))

    for i in range (len(lines) - 2):
        line1 = int(lines[i])
        line2 = int(lines[i + 1])
        line3 = int(lines[i + 2])

        sum2 = line1 + line2 + line3

        if sum2 > sum1:
            counter += 1

        sum1 = sum2

    print(f"The count is {counter}.")

sonar_average(lines)