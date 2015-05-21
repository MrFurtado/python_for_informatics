# Write a program to prompt the user for hours and rate per hour to compute gorsspay.
prompt1 = 'Enter Hours: '
hours = raw_input(prompt1)
prompt2 = 'Enter Rate: '
rate = raw_input(prompt2)
pay = int(hours) * float(rate)
print "Pay: ", pay