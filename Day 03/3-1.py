# Open the input file and read it into separate lines, stripping the newline character at the end
with open("test.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]


# PART ONE
def power_consumption(data):

    # Set up strings to hold the "most common" bit for each position
    gamma = ''
    epsilon = ''

    # A variable to hold where you are in the line
    linepos = 0

    # While your position is less than the number of items in the line
    while linepos < len(lines[0]):

        # Counters for how often you've seen each bit
        count0 = 0
        count1 = 0

        # Iterate through each line of the data
        for line in data:

            # Increment the counters based on what bit you're seeing
            if line[linepos] == '0':
                count0 += 1
            elif line[linepos] == '1':
                count1 += 1

        # Append the most common bit to the correct list
        if count0 > count1:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

        # Increment the line position so you move to the next one
        linepos += 1

    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)

    power = gamma_dec * epsilon_dec

    print(f"The power consumption is {power}.")


power_consumption(lines)
