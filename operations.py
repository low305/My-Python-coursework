
    import os,sys
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')#clears the screen

    from time import sleep
def print_slow(txt):#prints slow duh
    for x in txt:
        print(x, end='', flush=True)
        sleep(0.03)#speed of print


def big_space():#almost centers from top
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()


def bat_symbol():
    print('                             ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')#for some reson the .center() left 1 line gaps in bat signal
    print('                             ░░░░░░░▄▄▄░░░█▄▄▄█░░░▄▄▄░░░░░░░░')
    print('                             ░░░░░▄███░░░░█████░░░░███▄░░░░░░')
    print('                             ░░░▄█████▄░░▄█████▄░░▄█████▄░░░░')
    print('                             ░░███████████████████████████░░░')
    print('                             ░░███████████████████████████░░░')
    print('                             ░░▀█████████████████████████▀░░░')
    print('                             ░░░░▀███████▀█████▀███████▀░░░░░')
    print('                             ░░░░░░▀███▀░░░███░░░▀███▀░░░░░░░')
    print('                             ░░░░░░░░░▀░░░░░▀░░░░░▀░░░░░░░░░░')
    print('                             ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')


def wave_hand1():
    print('                                               _.-._         ')#hand waving
    print('                                              | | | |_       ')
    print('                                              | | | | |      ')
    print('                                              | | | | |      ')
    print("                                            _ |  '-._ |      ")
    print("                                            \`\`-.'-._;      ")
    print("                                             \    '   |      ")
    print('                                              \  .`  /       ')
    print('                                               |    |        ')
    sleep(0.5)
    clear_screen()
    print("                                               ____          ")
    print("                                            .'` __/_______   ")
    print("                                       ---'  -'`    ______)  ")
    print("                                                    _______) ")
    print("                                                   _______)  ")
    print("                                       -----..___________)   ")
    sleep(0.5)
    clear_screen()
    print('                                               _.-._         ')
    print('                                              | | | |_       ')
    print('                                              | | | | |      ')
    print('                                              | | | | |      ')
    print("                                            _ |  '-._ |      ")
    print("                                            \`\`-.'-._;      ")
    print("                                             \    '   |      ")
    print('                                              \  .`  /       ')
    print('                                               |    |        ')
    sleep(0.5)
    clear_screen()
    print("                                               ____          ")
    print("                                            .'` __/_______   ")
    print("                                       ---'  -'`    ______)  ")
    print("                                                    _______) ")
    print("                                                   _______)  ")
    print("                                       -----..___________)   ")
    sleep(0.5)
