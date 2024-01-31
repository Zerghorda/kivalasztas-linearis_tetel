import math


def szam_szamlaloi(szam):
    szamlalok = []
    i = 2
    while i < round(math.sqrt(szam)):
        if szam % i == 0:
            szamlalok.append(i)
        i += 1
    return szamlalok


print(szam_szamlaloi(10007))

