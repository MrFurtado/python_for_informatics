# Write another program that prompts for a list of numbers like chap 5
# exercise 1 and at the end prints out both the maximum and minimum of the
# numbers instead of the average
num_array = []
while True:
	prompt1 = raw_input("Enter a number (tpye 'done' to stop): ")
	if prompt1 == 'done':
		break
	num = int(prompt1)
	num_array.append(num)

print 'Minimum is: ', min(num_array)
print 'Maximum is: ', max(num_array)