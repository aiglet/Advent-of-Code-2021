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
    elif count1 > count0:
        return '1'
    else:
        return 'equal'

def gasses(data):

    oxy = []
    C02 = []

    index = 0

    for item in data:
        if item[index] == find_common(data, index):
            oxy.append(item)
        else:
            C02.append(item)

    oxy_index = 0

    while len(oxy) > 1:

        for item in oxy:

            if item[oxy_index] == find_common(oxy, oxy_index):
                continue
            elif find_common(oxy, oxy_index) == 'equal' and item[oxy_index] == 0:
                oxy.remove(item)
                print(oxy)
            else:
                oxy.remove(item)
                print(oxy)

        oxy_index += 1

    C02_index = 0

    while len(C02) > 1:

        for item in C02:

            if item[C02_index] == find_common(C02, C02_index):
                print(C02)
                C02.remove(item)
            elif find_common(C02, C02_index) == 'equal' and item[C02_index] == 1:
                C02.remove(item)
            else:
                continue

        C02_index += 1

    print(C02)

gasses(lines)