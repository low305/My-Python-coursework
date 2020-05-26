# findind and counting vowls in a sentence
word = input('Enter sentence here:', )
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
word = word.lower()
for letter in word:
    if letter == 'a':
        count_a = count_a + 1
    if letter == 'e':
        count_e = count_e + 1
    if letter == 'i':
        count_i = count_i + 1
    if letter == 'o':
        count_o = count_o + 1
    if letter == 'u':
        count_u = count_u + 1
print('A:', count_a)
print('E:', count_e)
print('I:', count_i)
print('O:', count_o)
print('U:', count_u)