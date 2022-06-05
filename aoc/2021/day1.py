def readData(filename):
    data = []
    f = open(filename, "r")
    for line in f:
        data.append(int(line.strip()))

    f.close()
    return data

def solvePart1(data):
    prevDepth = None
    increaseCounter = 0

    for depth in data:
        if prevDepth != None and depth > prevDepth:
            increaseCounter += 1

        prevDepth = depth

    return increaseCounter

def solvePart2(data):
    prevSum = None
    increaseCounter = 0

    for i in range (len(data) - 2):
        windowSum = data[i] + data[i+1] + data[i+2]

        if prevSum != None and windowSum > prevSum:
            increaseCounter += 1

        prevSum = windowSum


    return increaseCounter


if __name__ == "__main__":
    filename = "data.txt"
    data = readData(filename)
    print(f"Data: {data}")

    part1Ans = solvePart1(data)
    print(f"The answer to part 1 is: {part1Ans}")

    part2Ans = solvePart2(data)
    print(f"The answer to part 2 is: {part2Ans}")
