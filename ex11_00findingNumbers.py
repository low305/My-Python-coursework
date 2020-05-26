#The basic outline of this problem is to read the file, look for integers
# using the re.findall(), looking for a regular expression of '[0-9]+' and
# then converting the extracted strings to integers and summing up the
# integers.
import re
fname = input('Enter file name: ')
if len(fname) < 1: fname = 'regex_sum_499374.txt'
try: fh = open(fname)
except:
    print('Cannot open file:', fname)
    quit()
lst = list()
for lines in fh:
    num = re.findall('[0-9]+' , lines)
    for n in num:
        x = int(n)
        lst.append(x)
print(sum(lst))
