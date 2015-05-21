# Write a program which prompts the user for a Celsius temperature, convert
# the temperature to Fahrenheit and print out the converted temperature
prompt1 = "Temp in Celsius: "
celsius = raw_input(prompt1)
farh = int(celsius) * 9/5 + 32
print "Fahrenheit is: ", farh