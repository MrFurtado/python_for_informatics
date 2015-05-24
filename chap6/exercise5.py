#take str = 'X-DSPAM-Confidence:  0.8475' use find and string sclicing to
#extract the portion of the string after the colon character and then use the
#float fucntion to convert the extracted string into a floating point number.
str = 'X-DSPAM-Confidence:  0.8475'

new_string = str.replace(" ", "")
start = new_string.find(":")
data = new_string[start+1:]
print float(data)