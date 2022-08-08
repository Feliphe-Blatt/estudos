"""
x = 0
while x < 100:
    if x == 99:
        print(x)
        break  # continue
    else:
        print(x, end=',')
        x += 1
"""
x = 1
while x < 100:
    print(x, end=',')
    x += 1
else:
    print(x)
