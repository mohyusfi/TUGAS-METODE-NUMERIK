import numpy as np


# contoh persamaan: x - cos(x) = 0

def f(x):
    return x - np.cos(x)

def regula_falsi(f, a, b, tol=1e-5, max_iter=100):
    # Memastikan tebakan awal mengurung akar (berbeda tanda)
    if f(a) * f(b) >= 0:
        print("Tebakan awal tidak mengurung akar.")
        return None

    c = a
    for _ in range(max_iter):
        # Mencari titik potong garis lurus antara (a, f(a)) dan (b, f(b))
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if abs(f(c)) < tol:
            break
        elif f(a) * f(c) < 0:
            b = c  # Akar ada di bagian kiri
        else:
            a = c  # Akar ada di bagian kanan

    return c

# Menjalankan Regula Falsi pada interval [-1, 1]
akar_regula_falsi = regula_falsi(f, -1, 1)
print(f"Akar (Regula Falsi): {akar_regula_falsi}")
