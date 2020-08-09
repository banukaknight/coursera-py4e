# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for fline in fh:
    fl = fline.rstrip()
    print (fl.upper())