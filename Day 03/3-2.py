# Open the input file and read it into separate lines, stripping the newline character at the end
with open("test.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]


# A function to find whether 1 or 0 is more common at any given index of a list
def find_common(data, index):

    # Set up variables to hold our counts
    count0 = 0
    count1 = 0

    # For each line of the data
    for line in data:

        # Turn each line into a list for ease of indexing
        line = list(line)

        # Increment the counter appropriate to what you found at that index
        if line[index] == '0':
            count0 += 1
        elif line[index] == '1':
            count1 += 1

    # Return the most common item or 'equal' if the counts are the same
    if count0 > count1:
        return '0'
    elif count1 > count0:
        return '1'
    else:
        return 'equal'


# The function that actually finds the final number
def gasses(data):

    # Lists of potential oxygen and C02 numbers
    oxy = []
    C02 = []

    # Split the list into oxygen and C02 potentials based on the full list
    for item in data
        # Oxygen takes the items with the most common
        if item[0] == find_common(data, 0):
            oxy.append(item)
        # C02 takes the items with the least common
        else:
            C02.append(item)

    # This is where the oxygen calculator starts.
    # A variable to hold what index we're working from
    oxy_index = 0

    # Loop through the oxygen candidates until there's only one left
    while len(oxy) > 1:

        # For each item in the oxygen candidates
        for item in oxy:

            # If the item has the common value at that index or there are equal numbers, keep it, otherwise discard it
            if item[oxy_index] == find_common(oxy, oxy_index):
                continue
            elif find_common(oxy, oxy_index) == 'equal' and item[oxy_index] == 0:
                oxy.remove(item)
                print(oxy)
            else:
                oxy.remove(item)
                print(oxy)

        # After we've processed each item in the list, increment the index
        oxy_index += 1

    # This is where the C02 calculator starts
    # Set up a variable to hold the C02 index
    C02_index = 0

    # Until there is only one C02 candidate
    while len(C02) > 1:

        # Take each item in the candidate list in turn
        for item in C02:

            # If the item has the most common term at any given index, or the index counts are equal and the item has a 1 at that index, remove it from the list
            if item[C02_index] == find_common(C02, C02_index):
                print(C02)
                C02.remove(item)
            elif find_common(C02, C02_index) == 'equal' and item[C02_index] == 1:
                C02.remove(item)
            else:
                continue

        # Increment the index at each pass through the list
        C02_index += 1

    print(C02)

gasses(lines)