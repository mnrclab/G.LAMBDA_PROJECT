#CARA PERTAMA
def prima(x):
    a = False
    if x > 1:
        if x == 2: a = True
        else:
            for i in range(2, x):
                if x % i == 0: return False; break
                else: a = True
    else: a = False
    return a
print(prima(81))

#CARA KEDUA
x = lambda a : 'Angka Genap' if a % 2 == 0 else 'Angka Ganjil'

angka = int(input('Masukkan angka yang ingin dites: '))
y = lambda a : 'Bilangan Prima' if (a == 2) or (angka % a == 0) else 'Bukan Bilangan Prima'
print(y(angka))
