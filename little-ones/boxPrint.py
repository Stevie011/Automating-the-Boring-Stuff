#!python3

#box print- exception and error testing

def boxPrint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception("symbol must be single char string")
    if width <= 2:
        raise Exception("width must be > 2")
    if height <= 2:
        raise Exception("height must be > 2")

    print(symbol * width)
    for i in range(height-2):
        print(symbol + (" "* (width-2))+ symbol)
    print(symbol*width)

for sym,w,h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym,w,h)
    except Exception as err:
        print("Exception happened : " + str(err))