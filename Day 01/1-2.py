
# Open the data file and split it into lines
data = open("input.txt")
lines = data.readlines()

# PART TWO


def sonar_average(input_file):
    # Set up a counter
    counter = 0

    # Establish the first sum to start with
    sum1 = (int(input_file[0]) + int(input_file[1]) + int(input_file[2]))

    # Iterate through the file and select each group of three
    for i in range(len(input_file) - 2):
        line1 = int(input_file[i])
        line2 = int(input_file[i + 1])
        line3 = int(input_file[i + 2])

        # Sum each group
        sum2: int = line1 + line2 + line3

        # Compare the new group to the old one and increment the counter as appropriate
        if sum2 > sum1:
            counter += 1

        # Reset sum1 to the new value
        sum1 = sum2

    # Print the output
    print(f"The count is {counter}.")


# Run the function
sonar_average(lines)
