
# Open the data file and split it into lines
data = open("input.txt")
lines = data.readlines()

# PART ONE

def sonar_up(lines):
# Set up a counter and some variables to hold the lines as we iterate through.
    counter = 0
    line1 = (lines[1])
    line2 = 0

# Compare each line to the prior line
    for line in lines:
        line2 = (line)
        # Note the conversion to INT here - otherwise it tries to do a STR comparison and doesn't work
        if int(line2) > int(line1):
            # Increment the counter every time the second thing is bigger than the first thing
            counter += 1
        # Reset for the next comparison
        line1 = line

    # Print the final results
    print(f"The count is {counter}.")

sonar_up(lines)