def linearis():
    also: int = 42
    felso: int = 67
    i = also
    while i < felso and not(i % 10 == 0):
        i += 1
    van: bool = i <= felso
    if van:
        print(f"Van 0-ra végződő szám: {i}")
    else:
        print("Nincs 0-ra végződő")


linearis()
