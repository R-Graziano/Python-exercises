def isPrime(num):
#
# coloca tu código aquí
#
    if num > 1:
        i = 2
        while i < num:
            if num % i == 0:
                return False
            i += 1
        else:
            return True
    else:
        return False

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()