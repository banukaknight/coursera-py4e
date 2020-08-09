name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mailers = dict()

for line in handle:
    #print(line)
    line = line.strip()
    linewords = line.split()
    if len(line)<4 or linewords[0] != 'From': 
        continue
    else:
        #email = linewords[1]
        if linewords[1] not in mailers:
            mailers[linewords[1]] = 1
        else:
            mailers[linewords[1]] = mailers[linewords[1]] + 1
maxkey = None
maxval = None
for key in mailers:
    if maxval==None or mailers[key] > maxval:
        maxkey = key
        maxval = mailers[key]        
print(maxkey, maxval)

'''
#convert dictlist to normal list
keylist = list(mailers.keys())
vallist = list(mailers.values())
#getmaxvalue's index
print(keylist[vallist.index(max(vallist))], max(vallist) )
'''