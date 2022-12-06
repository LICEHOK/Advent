with open("input5.txt") as input:
    lines = input.readlines()
    i = 9
    raw = 0
    column = 0
    count = 10
    blocks = [0]
    for i in range(count):
        blocks[i] = [0]*10
    print(len(lines))
    for i in range(len(lines)-502):
        print(blocks[i])
        for j in range(len(lines[i])):
            if lines[i][j] == '[':
                print(i, j+1)
                blocks[j // 3][i // 1] = lines[i][j+1]
        c = 0
        print(blocks[i])




