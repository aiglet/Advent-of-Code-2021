# Open the input file and read it into separate lines, stripping the newline character at the end
with open("test.txt", "r") as f:
    lines = [x.strip() for x in f.readlines()]


def find_common(data):

    count0 = 0
    count1 = 0
    index = 0

    for line in data:

        line = list(line)

        while index < len(line[0]):
            if line[index] == '0':
                count0 += 1
                index += 1
            elif line[index] == '1':
                count1 += 1
                index += 1

    if count0 > count1:
        return('0')
    else:
        return('1')


def gasses(data):

    oxy = []
    C02 = []
    index = 0

    for item in data:
        print(f"The current item is {item}.")
        print(f"The current index is {index}.")
        print(f"The common number is {find_common(data)}.")

        if item[index] == find_common(data):
            oxy += item
        else:
            C02 += item

        index += 1

    print(f"The oxy candidates are {oxy}.")
    print(f"The C02 candidates are {C02}.")



gasses(lines)
