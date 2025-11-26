str= 'X-DSPAM-Confidence:0.8475'
a=str.find(':')
b=str[a+1:]
print(float(b)) 