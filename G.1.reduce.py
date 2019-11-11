from functools import reduce
angka = range(101)

z = reduce(lambda x,y: x + y, list(map(lambda x: x * 2, list(filter(lambda x: x % 2 == 0, angka)))))
print(z)
