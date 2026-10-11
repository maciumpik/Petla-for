dane = [1, 4, 6, 7, 1, 2, 4, 8, 7, 9, 6, 6, 10]
for index, x in enumerate(dane):
    if x%2 == 0:
        print(f"Liczba {x} jest parzysta i jej pozycja to: {index+ 1}")
