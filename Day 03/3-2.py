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
        return '0'
    else:
        return '1'

def gasses(data):

    oxy = []
    C02 = []

    index = 0

    for item in data:
        if item[index] == find_common(data, index):
            oxy.append(item)
        else:
            C02.append(item)

    while len(oxy) > 1:
        index = 0

        for item in oxy:

            if item[index] == find_common(oxy, index):
                index += 1
            else:
                oxy.remove(item)
                index += 1

    print(oxy)



gasses(lines)