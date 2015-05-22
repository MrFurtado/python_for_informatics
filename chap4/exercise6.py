#Like chap3 exercise 1


def computepay(hours, rate):
  
  if hours > 40:
    pay = rate * 40 + (rate * 1.5 * (hours - 40))
    print pay
  else:
    pay = rate * hours
    print pay
    

prompt1 = raw_input('Enter hours: ')
hours = float(prompt1)
prompt2 = raw_input('Enter Rate: ')
rate = float(prompt2)
computepay(hours, rate)