# Open the input file and read it into separate lines
with open("input.txt", "r") as f:
    lines = f.readlines()


def course(locations):

    # Establish some variables to hold course info
    depth = 0
    heading = 0

    # Split each line into a direction and a value
    for line in locations:
        location = line.split()

        # Run through the cases for each action type
        if location[0] == "down":
            depth += int(location[1])
        elif location[0] == "up":
            depth -= int(location[1])
        elif location[0] == "forward":
            heading += int(location[1])

    # Perform the desired multiplication to solve the problem
    total = depth * heading
    print(f"The total is {total}.")


course(lines)
