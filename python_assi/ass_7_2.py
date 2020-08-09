# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
icount = 0
ftot = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':')
    snum = line[pos+1:]
    snum = snum.strip()
    ftot= ftot + float(snum)
    icount = icount + 1
favg = ftot/icount   
print("Average spam confidence:",favg)