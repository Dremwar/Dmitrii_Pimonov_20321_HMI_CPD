import numpy as np
import matplotlib.pyplot as plt
# Параметры задачи
Lx, Ly, Nx, Ny, Re, dt, n_steps = 1.0, 1.0, 50, 50, 100, 0.001, 500
dx, dy = Lx / (Nx - 1), Ly / (Ny - 1)
# Инициализация полей
u, v, p = np.zeros((Nx, Ny)), np.zeros((Nx, Ny)), np.zeros((Nx, Ny))
u[0, :] = 1  # Верхний край (поток)
# Функция для расчета правой части
build_rhs = lambda f: (
    - (u * (np.roll(f, -1, axis=0) - np.roll(f, 1, axis=0)) / (2 * dx))
    - (v * (np.roll(f, -1, axis=1) - np.roll(f, 1, axis=1)) / (2 * dy))
    + (1 / Re) * (
        (np.roll(f, -1, axis=0) - 2 * f + np.roll(f, 1, axis=0)) / dx**2 +
        (np.roll(f, -1, axis=1) - 2 * f + np.roll(f, 1, axis=1)) / dy**2
    )
)
# Итерации
for _ in range(n_steps):
    u[1:-1, 1:-1] += dt * build_rhs(u)[1:-1, 1:-1]
    v[1:-1, 1:-1] += dt * build_rhs(v)[1:-1, 1:-1]
# Визуализация
plt.figure(figsize=(8, 6))
plt.quiver(u.T, v.T, scale=10)
plt.title("Скоростное поле (u, v)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
