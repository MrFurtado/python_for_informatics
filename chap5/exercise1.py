total = 0
while True:
	prompt1 = raw_input("Enter a number: ")
	if prompt1 == 'done':
		break
	num = float(prompt1)
	total = total + 1


print total
