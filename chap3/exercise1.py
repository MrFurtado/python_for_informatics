# Rewrite your pay computation from chap 2 exercise 2 to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
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