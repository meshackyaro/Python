for year in range(1, 31):
    amount = 1000 * (1 + 0.07) ** year
    print(f'{year:>2}{amount:>10.2f}')