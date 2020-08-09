#fname = input("Enter file name: ")
fh = open('romeo.txt')
lst = list()
for line in fh:
    linewords = line.rstrip().split()
    for word in linewords:
        if word not in lst:
            lst.append(word)
lst.sort()            
print(lst)