import numpy as np

# matrix_size = n x n
def build_magic_squares(matrix_size):
	magic_square = np.zeros((matrix_size, matrix_size), dtype=int)

	n = 1
	i = 0
	j = matrix_size // 2

	while n <= matrix_size * matrix_size:
		magic_square[i, j] = n

		n += 1
		ii = (i - 1) % matrix_size
		jj = (j + 1) % matrix_size

		if magic_square[ii, jj]:
			i += 1
		else:
			i, j = ii, jj

	return magic_square
	print("\n")



# Square formatting here:
def format_magic_square(magic_square):
	nice_list = [["%3s" % str(str(j) + " ") for j in i] for i in magic_square]
	for line in nice_list:
		print(" ".join(map(str, line)))

# Verification/test matrix
def magic_square_test(matrix):
	iSize = len(matrix[0])
	sum_list = []

	#Horizontal Part:
	sum_list.extend([sum(lines) for lines in matrix])

	#Vertical Part:
	for col in range(iSize):
		sum_list.append(sum(row[col] for row in matrix))

	#Diagonals Part
	result1 = 0
	for i in range(0, iSize):
		result1 += matrix[i][i]
	sum_list.append(result1)

	result2 = 0
	for i in range(iSize - 1, -1, -1):
		result2 += matrix[i][i]
	sum_list.append(result2)

	if len(set(sum_list)) > 1:
		return "incorrect"
	return "correct"


def main(matrix_size):
	print("\n")
	magic_square = build_magic_squares(matrix_size)
	print("\n")
	format_magic_square(magic_square)
	print("\n")
	print(magic_square_test(magic_square))


if __name__ == "__main__":
	while True:
		try:
			num = int(input("Please enter a positive odd integer:  "))
		except ValueError:
			print("Sorry, enter valid number")
			continue
		if (num < 0) or (num % 2) == 0:
			print("Sorry, your response must be positive odd number.")
			continue
		else:
			break

if (num % 2) == 1:
	main(num)
