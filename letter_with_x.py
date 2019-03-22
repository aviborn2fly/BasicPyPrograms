numbers = [2, 2, 2, 2, 5]
for items in numbers:
    i = 0
    symbol = ""
    for count in range(items):
        symbol += "x"
        i += 1
    print(symbol)