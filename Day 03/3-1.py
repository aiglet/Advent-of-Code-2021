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

    return [gamma, epsilon]

    # Commented this line out because we're now silently returning the binary values instead so I can use them in part 2
#    print(f"The power consumption is {power}.")


power_consumption(lines)

# PART TWO
def life_support(input_data, p_c_data):
    oxy_candidates =[]
    C02_candidates =[]
    linepos = 0
    oxypos = 0
    C02pos = 0
    gamma = list(p_c_data[0])
    epsilon = list(p_c_data[1])

    # Iterate through each line of the data and set up your initial candidates
    for line in input_data:
        if line[linepos] == gamma[linepos]:
            oxy_candidates.append(line)
        else:
            C02_candidates.append(line)

    # So what we need to do now is continue the comparison -- compare the second place of each element in oxy_candidates to the second place of each element in gamma, etc. and then the same with C02_candidates and epsilon.

    for item in range(0, len(oxy_candidates)):
        if oxy_candidates[item] == gamma[item]:
            continue
        else:
            oxy_candidates.remove(oxy_candidates[item])
            print(oxy_candidates)



life_support(lines, power_consumption(lines))
