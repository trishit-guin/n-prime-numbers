n = int(input('Enter the number of prime numbers needed:'))
j = 2
while n != 0:
	for i in range(2, j):
		if j % i == 0:
			break
	else:
		print(j, end=' ')
		n = n - 1
	j = j + 1
