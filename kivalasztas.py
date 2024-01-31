import math


def kivalsztas():
    prim = False
    n: int = 9999
    while not prim:
        n += 1
        i = 2
        while i <= math.sqrt(n) and not n % i == 0:
            i += 1
        prim = i > math.sqrt(n)
    print(n)


kivalsztas()
