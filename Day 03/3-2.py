# Open the input file and read it into separate lines, stripping the newline character at the end
with open("input.txt", "r") as f:
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
    for item in data:
        # Oxygen takes the items with the most common
        if item[0] == find_common(data, 0):
            oxy.append(item)
        # C02 takes the items with the least common
        else:
            C02.append(item)

    # This is where the oxygen calculator starts.
    # A variable to hold what index we're working from
    oxy_index = 1

    # Loop through the oxygen candidates until there's only one left
    while len(oxy) > 1:

        # Find the item that's common at the current index
        common = find_common(oxy, oxy_index)
        # For each item in the oxygen candidates
        for item in oxy:

            # If the item has the common value at that index or there are equal numbers and the item has a 1 at that index, keep it, otherwise discard it
            if item[oxy_index] == common:
                continue
            elif common == 'equal' and item[oxy_index] == 0:
                oxy.remove(item)
            else:
                oxy.remove(item)

        # After we've processed each item in the list, increment the index
        oxy_index += 1

    # This is where the C02 calculator starts
    # Set up a variable to hold the C02 index
    C02_index = 1

    # Until there is only one C02 candidate
    while len(C02) > 1:

        # Find the item that's common at the index
        common = find_common(C02, C02_index)
        # Take each item in the candidate list in turn
        for item in C02:

            # If the item has the most common term at any given index, or the index counts are equal and the item has a 1 at that index, remove it from the list
            if item[C02_index] == common:
                C02.remove(item)
            elif common == 'equal' and item[C02_index] == 1:
                C02.remove(item)
            else:
                continue

        # Increment the index at each pass through the list
        C02_index += 1

    # Convert things back out of a list into a string
    oxy = oxy[0]
    C02 = C02[0]

    # Convert the binary numbers to decimal
    oxy_dec = int(oxy, 2)
    C02_dec = int(C02, 2)

    # Perform the life support calculation
    life_support = oxy_dec * C02_dec

    # Print the result
    print(f"The life support value is {life_support}.")


gasses(lines)