# Write a program which repeatedly reads number until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the
# numbers. If the user enters anything other than a number, detect their
# mistake using try and except and print an error message and skop to the next
# number.
total = 0
while True:
	prompt1 = raw_input("Enter a number: ")
	if prompt1 == 'done':
		break
	num = float(prompt1)
	total = total + 1


print total
