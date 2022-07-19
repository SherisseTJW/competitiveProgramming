from ReadData import readData

def getNthDigit(binary, n):
	return binary[n]


def solvePart1(data):
	numDigits = len(data[0])
	gamma = ""
	epsilon = ""

	for i in range(numDigits):
		nDigits = []

		for binary in data:
			nDigits.append(getNthDigit(binary, i))

		gamma += str(max(nDigits))
		epsilon += str(min(nDigits))

		print(nDigits)
		print(gamma)
		print(epsilon)

	# Convert to decimal
	gamma = int(gamma, 2)
	epsilon = int(epsilon, 2)

	return gamma*epsilon


if __name__ == "__main__":
	filename = "testData.txt"
	data = readData(filename)
	print(f"Data: {data}")

	part1Ans = solvePart1(data)
	print(f"The answer for part 1 is: {part1Ans}")
