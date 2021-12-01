
# Open the data file and split it into lines
data = open("testdata.txt")
lines = data.readlines()

# PART ONE

def sonar_up(lines):
    counter = 0
    line1 = lines[1]
    line2 = 0

    for line in lines:
        line2 = line
        if line2 > line1:
            counter += 1
        line1 = line

    print(f"The count is {counter}.")

sonar_up(lines)