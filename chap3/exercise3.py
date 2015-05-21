# Write a program to rpomt for a score between 0.0 and 1.0. If the score is
# out of the range print an error. If the score is between 0.0 and 1.0, print
# a grade using the following table:
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
prompt1 = raw_input("Enter score ")
try:
	score = float(prompt1)
	if score >= 0.9:
		print 'A'
	elif score >= 0.8:
		print 'B'
	elif score >= 0.7:
		print 'C'
	elif score >= 0.6:
		print 'D'
	else:
		print 'F'
except:
	print 'Bad score'
