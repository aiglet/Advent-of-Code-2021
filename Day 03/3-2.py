# Open the input file and read it into separate lines, stripping the newline character at the end
with open("test.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]


def find_common(data, index):

    count0 = 0
    count1 = 0

    for line in data:

        line = list(line)

        if line[index] == '0':
            count0 += 1
        elif line[index] == '1':
            count1 += 1

    if count0 > count1:
        print(f"There are more 0s than 1s, the 0 count is {count0}, the 1 count is {count1}.")
    else:
        print(f"There are more 1s than 0s, the 0 count is {count0}, the 1 count is {count1}.")




find_common(lines, 0)