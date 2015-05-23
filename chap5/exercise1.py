# Write a program which repeatedly reads number until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the
# numbers. If the user enters anything other than a number, detect their
# mistake using try and except and print an error message and skop to the next
# number.
count = 0
total = 0
while True:
    prompt1 = raw_input("Enter a number: ")
    if prompt1 == 'done':
        break
    try: 
        num = float(prompt1)
    except:
        print "Invalid input"
        continue
    count = count + 1
    total = total + num
    print num, total, count
    
print 'Average: ', total / count
