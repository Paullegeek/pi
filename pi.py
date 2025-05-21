import mpmath

mpmath.mp.dps = 1  # Précision initiale

while True:
    print(mpmath.nstr(mpmath.pi, mpmath.mp.dps))  # Affiche pi avec la précision actuelle
    mpmath.mp.dps += 1  # Augmente la précision d'une décimale
