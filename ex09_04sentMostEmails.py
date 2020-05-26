# 9.4 Write a program to read through the mbox-short.txt and
# figure out who has sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes
# the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps
# the sender's mail address to a count of the number of
# times they appear in the file. After the dictionary is
# produced, the program reads through the dictionary using
# a maximum loop to find the most prolific committer.

fname = input('Enter file: ')
if len(fname) < 1: fname = 'mbox-short.txt'
try:fh = open(fname)
except:
    print('Cannot open file: ', fname)
    quit()
sendCount = dict()
for lines in fh:
    if lines.startswith('From '):
        slines = lines.split()
        sendCount[slines[1]] = sendCount.get(slines[1], 0) + 1
#print(sendCount)
bigword = None
bignum = None
for k,v in sendCount.items():
    if bignum is None or v > bignum:
        bignum = v
        bigword = k
print(bigword, bignum)
