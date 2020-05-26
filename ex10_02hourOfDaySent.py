# 10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for
# each of the messages. You can pull the hour out from the
# 'From ' line by finding the time and then splitting the
# string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print
# out the counts, sorted by hour as shown below.

hoursent = dict()
fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
try: fh = open(fname)
except:
    print('Cannot open file:', fname)
    quit()
for lines in fh:
    if len(lines) < 1 or not lines.startswith('From '):continue
    sline = lines.split()
    time = sline[5].split(':')
    hr = time[0]
    hoursent[hr] = hoursent.get(hr,0) + 1
temp = list()
for tups in hoursent.items():
    temp.append(tups)
temp = sorted(temp)
for k,v in temp:
    print(k,v)