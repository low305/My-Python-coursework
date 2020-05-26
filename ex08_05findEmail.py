# 8.5 Open the file mbox-short.txt and read it line by line. When you find a
# line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word 
#in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.

#Hint: make sure not to include the lines that start with 'From:'.

fname = input("Enter file name: ")
try: fh = open(fname)
except:
    print('Cannot open file:>>> ', fname)
    quit()
count = 0
for line in fh:
    if line.startswith('From '):
        count = count + 1
        sline = line.split()
        print(sline[1])
print("There were", count, "lines in the file with From as the first word")