import numpy as np
summary1 = []
with open("input4.txt") as input:
    lines = input.readlines()
    count_part1 = 0
    count_part2 = len(lines)
    for i in range(len(lines)):
        pairs = lines[i].split(",")
        pair1 = pairs[0].split("-")
        pair2 = pairs[1].split('-')
        if (int(pair1[0]) <= int(pair2[0]) and int(pair1[1]) >= int(pair2[1])) or (int(pair1[0]) >= int(pair2[0]) and int(pair1[1]) <= int(pair2[1])):
            count_part1 += 1
        if int(pair1[1]) < int(pair2[0]) and int(pair1[0]) < int(pair2[0]) or int(pair2[1]) < int(pair1[0]) and int(pair2[0]) < int(pair1[0]):
            count_part2 -= 1
print(count_part1)
print(count_part2)


# if check[i] in bukvi.keys():