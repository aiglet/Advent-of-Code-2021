# Open the input file and read it into separate lines
with open("test.txt", "r") as f:
    lines = f.readlines()

def calc_freq(data):
    freq = {}
    for c in set(data):
        freq[c] = data.count(c)
    print(freq)

def power_consumption(data):
    count0 = 0
    count1 = 0

    gamma = ''
    epsilon = ''

    for line in data:
        linepos = 0

        while linepos < 5:

            if line[linepos] == 0:
                count0 += 1
                print(f"{line[linepos]} is 0.")
                print(count0)
            elif line[linepos] == 1:
                count1 += 1
                print(f"{line[linepos]} is 1.")
                print(count1)

            if count0 > count1:
                gamma += '0'
                epsilon += '1'
            elif count0 < count1:
                gamma += '1'
                epsilon += '0'

            print(f"Gamma is {gamma}.")
            print(f"Epsilon is {epsilon}.")

            linepos += 1







power_consumption(lines)