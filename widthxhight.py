#outputs the m2 and ft2 area of input in meters 
while True:
    lenth = input('Enter lenth in meters: ')
    width = input('Enter width in meters: ')
    try:
        lenth = float(lenth)
        width = float(width)
        break
    except:
        print('One of the entires was invalid! Please try again.')
        continue
print(('Area in  m2:'),lenth * width,('m2'))
print(('Area in ft2:'),(lenth * width) * 10.764,('ft2'))