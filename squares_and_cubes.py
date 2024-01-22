print (f'{"number"}\t {"square"}\t {"cube"}')
for number in range(6):
    square = number ** 2
    cube = square * number
    print(f'{number:>5}\t {square:>5}\t {cube:>4}')