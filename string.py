text = "X-DSPAM-Confidence:    0.8475"
gif=text.find('0')
hif=text.find('5')
jif=text[gif:hif+1]
lif=float(jif)
print(lif)
