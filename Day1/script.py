# Look at input file and separate by line into list
lines = [line.strip() for line in open('./input.txt')]
linesum = []

numwords = {
	'one': 1,
	'two': 2,
	'three': 3,
	'four': 4,
	'five': 5,
	'six': 6,
	'seven': 7,
	'eight': 8,
	'nine': 9
}

for line in lines:
	newline = ''
	for word in numwords:
		if word in line:
			newline = line.replace(word, str(numwords[word]))
		print(newline)

# print(lines)

# Function to run through each line and store first integer

# for line in lines:
# 	num1 = ''
# 	num2 = ''
# 	# print(line)
# 	for character in line:
# 		if character.isdigit():
# 			num1 = character
# 			# print(num1)
# 			break

# 	for character in line[::-1]:
# 		if character.isdigit():
# 			num2 = character
# 			# print (num2)
# 			break

# 	linenum = int(num1 + num2)
# 	linesum.append(linenum)

# print(sum(linesum))








# Function to run through each line and store last integer

# Function to concatenate first and last integer to create a 2-digit number

# Store output of concatenation into another list

# Sum of all the 2-digit numbers