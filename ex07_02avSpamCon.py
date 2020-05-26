# 7.2 Write a program that prompts for a file name, then opens that file and
# reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the
# lines and compute the average of those values and produce an output as shown
# below. Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
count = 0
total = 0
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Cannot open file: ' + fname)
    quit()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    sline = line.rstrip()
    colpos = sline.find(':')
    num = sline[colpos+1:]
    num = float(num)
    total = total + num
    count = count + 1
    



print("Average spam confidence:", total / count )


