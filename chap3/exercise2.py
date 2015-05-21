# Rewrite the program from chap3 exercise 2 using try and except so that the
# program handles non-numeric input gracefully by printing a message and exiting the program. 
try:
	prompt1 = raw_input("Enter Hours: ")
	hours = float(prompt1)

	prompt2 = raw_input("Enter Rate: ")
	rate = float(prompt2)


	if hours > 40:
		pay = rate * 40 + (rate * 1.5 * (hours - 40))
		print pay
	else:
		pay = rate * hours
		print pay
except: 
	print "Please enter a number"