# Open the input file and read it into separate lines
with open("test.txt", "r") as f:
    lines = f.readlines()


def calc_freq(data):
    freq = {}
    for c in set(data):
        freq[c] = data.count(c)
    print(freq)


def power_consumption(data):

    # Set up strings to hold the "most common" bit for each position
    gamma = ''
    epsilon = ''

    # Iterate through each line of the data
    for line in data:

        # A variable to hold where you are in the line
        linepos = 0

        # While your position is less than the number of items in the line + 1
        while linepos < 5:

            # Counters for how often you've seen each bit
            count0 = 0
            count1 = 0

            # Increment the counters based on what bit you're seeing
            if line[linepos] == '0':
                count0 += 1
            elif line[linepos] == '1':
                count1 += 1

            # Append the most common bit to the correct list
            if count0 > count1:
                gamma += '0'
                epsilon += '1'
            elif count0 < count1:
                gamma += '1'
                epsilon += '0'

            # Increment the line position so you move to the next one
            linepos += 1

    # Print statements for testing
    print(f"Gamma is {gamma}.")
    print(f"Epsilon is {epsilon}.")


power_consumption(lines)
