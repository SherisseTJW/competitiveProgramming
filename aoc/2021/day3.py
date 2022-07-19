from ReadData import readData


def getNthDigit(binary, n):
	return binary[n]

def filterData(data, i, type):
	nDigits = []

	for binary in data:
		nDigits.append(getNthDigit(binary, i))


def solvePart1(data):
	numDigits = len(data[0])
	gamma = ""
	epsilon = ""

	for i in range(numDigits):
		nDigits = []

		for binary in data:
			nDigits.append(getNthDigit(binary, i))

		gamma += str(max(nDigits, key = nDigits.count))
		epsilon += str(min(nDigits, key = nDigits.count))

	# Convert to decimal
	gamma = int(gamma, 2)
	epsilon = int(epsilon, 2)

	return gamma*epsilon


def solvePart2(data):
	numDigits = len(data[0])
	o2_rating = ""
	co2_rating = ""

	o2_tempData = data
	co2_tempData = data

	for i in range(numDigits):
		nDigits = []

		for binary in o2_tempData:
			nDigits.append(getNthDigit(binary, i))

		o2_criteria = max(nDigits, key = nDigits.count)


		co2_criteria = min(nDigits, key = nDigits.count)


if __name__ == "__main__":
	filename = "data.txt"
	data = readData(filename)
	print(f"Data: {data}")

	part1Ans = solvePart1(data)
	print(f"The answer for part 1 is: {part1Ans}")
