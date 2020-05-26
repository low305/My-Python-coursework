#bigest and smallest number practice from user input
big_num = None
small_num = None
while True:
    num = input('Enter number: ')
    try:
        num = int(num)
        if big_num is None and small_num is None:
            big_num = num
            small_num = num
        elif num > big_num:
            big_num = num
        elif num < small_num:
            small_num = num
    except:
        if num == 'done':
            break
        print('That was not a valid number!!!\nif done type done')
        continue
print('The biggest number was..', big_num)
print('The smallest number was..', small_num)
