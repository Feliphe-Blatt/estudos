with open('tabuada.txt', 'w') as tabuada:
    for i in range(1, 11):
        for j in range(1, 11):
            tabuada.write(f'{i} x {j} = {i * j}\n')
