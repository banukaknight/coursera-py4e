text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(':')
snumb = text[pos+1:]
fnumb = float(snumb.strip())
print(fnumb)