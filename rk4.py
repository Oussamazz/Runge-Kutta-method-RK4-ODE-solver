import numpy as np
import matplotlib.pyplot as plt

def decay_ode(t, y, k):
    return -k * y

def runge_kutta_ode_solver(func, y0, t0, tn, h, k):
    num_steps = int((tn - t0) / h) + 1
    t_values = np.linspace(t0, tn, num_steps)
    y_values = np.zeros(num_steps)
    y_values[0] = y0

    for i in range(1, num_steps):
        k1 = h * func(t_values[i-1], y_values[i-1], k)
        k2 = h * func(t_values[i-1] + h/2, y_values[i-1] + k1/2, k)
        k3 = h * func(t_values[i-1] + h/2, y_values[i-1] + k2/2, k)
        k4 = h * func(t_values[i-1] + h, y_values[i-1] + k3, k)

        y_values[i] = y_values[i-1] + (k1 + 2*k2 + 2*k3 + k4) / 6

    return t_values, y_values

# Initial conditions
y0 = 1
t0 = 0
tn = 5
h = 0.1
k = 0.5  # Decay rate

# Solve ODE using RK4
t_values, y_values = runge_kutta_ode_solver(decay_ode, y0, t0, tn, h, k)

# Plot the numerical solution
plt.plot(t_values, y_values, label=f'k = {k}')
plt.xlabel('Time (t)')
plt.ylabel('Dependent Variable (y)')
plt.legend()
plt.title('Numerical Solution of Exponential Decay ODE')
plt.show()

