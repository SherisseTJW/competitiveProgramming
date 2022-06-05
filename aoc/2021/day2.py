def readData(filename):
    data = []
    f = open(filename, "r")
    for line in f:
        data.append(line.strip())

    f.close()
    return data


def solvePart1(data):
    x = 0
    y = 0

    for command in data:
        direction = command.split(" ")[0]
        magnitude = int(command.split(" ")[1])

        if direction == "forward":
            x += magnitude

        elif direction == "down":
            y += magnitude

        elif direction == "up":
            y -= magnitude


    return x*y


def solvePart2(data):
	x = 0
	y = 0
	a = 0

	for command in data:
		direction = command.split(" ")[0]
		magnitude = int(command.split(" ")[1])

		if direction == "forward":
			x += magnitude
			y += a*magnitude

		elif direction == "down":
			a += magnitude

		elif direction == "up":
			a -= magnitude

	return x*y


if __name__ == "__main__":
    filename = "data.txt"
    data = readData(filename)
    print(f"Data: {data}")

    part1Ans = solvePart1(data)
    print(f"The answer to part 1 is: {part1Ans}")

    part2Ans = solvePart2(data)
    print(f"The answer to part 2 is: {part2Ans}")
