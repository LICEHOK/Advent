with open("input6.txt") as input:
    lines = input.readlines()
    block = []
    for i in range(14):
        block.append(lines[0][i])
    i = 13

    while True:
        i += 1
        for j in range(14):
            elem = block[j]
            count = 0
            for k in range(14):
                if block[k] == elem and k != j:
                    count = 1
                    break
            if count == 1:
                break
        if count == 1:
            for k in range(13):
                block[k] = block[k+1]
            block[13] = lines[0][i]
        else:
            print(i)
            break

