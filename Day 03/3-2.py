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

    oxy_index = 0

    while len(oxy) > 1:

        for item in oxy:

            if item[oxy_index] == find_common(oxy, oxy_index):
                continue
            else:
                oxy.remove(item)
                print(oxy)

        oxy_index += 1

    C02_index = 0

    while len(C02) > 1:

        for item in C02:

            if item[C02_index] == find_common(C02, C02_index):
                C02.remove(item)

        C02_index += 1

    print(C02)

# TODO: rewrite find_common into an oxy version (if there are equal 1s and 0s, 1 wins) and C02 version (if there are equal 1s and 0s, 0 wins). See if that fixes the C02 code, which is currently returning the wrong result.

gasses(lines)