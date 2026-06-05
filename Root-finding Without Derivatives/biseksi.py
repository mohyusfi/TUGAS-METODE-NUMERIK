import numpy as np


# contoh persamaan: x - cos(x) = 0

def f(x):
    return x - np.cos(x)

def bisection(f, a, b, tol=1e-5):
    # Memastikan tebakan awal mengurung akar (berbeda tanda)
    if f(a) * f(b) >= 0:
        print("Tebakan awal tidak mengurung akar.")
        return None
    
    c = a
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0  # Mencari titik tengah
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c  # Akar ada di bagian kiri
        else:
            a = c  # Akar ada di bagian kanan
    return c

# Menjalankan Bisection pada interval [-1, 1]
akar_bisection = bisection(f, -1, 1)
print(f"Akar (Bisection): {akar_bisection}")
















