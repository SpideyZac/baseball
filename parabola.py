import numpy as np
import sympy as sp
from sympy.solvers import solve
import matplotlib.pyplot as plt


def find_parabolic_roots(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a parabolic function.")

    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + np.sqrt(discriminant)) / (2 * a)
        root2 = (-b - np.sqrt(discriminant)) / (2 * a)
        return [root1, root2]
    elif discriminant == 0:
        root = -b / (2 * a)
        return [root]
    else:
        real_part = -b / (2 * a)
        imaginary_part = np.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return [root1, root2]


def find_parabola(y_int: float, x1: float, y1: float, x2: float, y2: float):
    a, b = sp.symbols("a b")
    eq1 = sp.Eq(a * x1**2 + b * x1 + y_int, y1)
    eq2 = sp.Eq(a * x2**2 + b * x2 + y_int, y2)
    output = solve([eq1, eq2], dict=True)

    a, b = output[0][a], output[0][b]

    return float(a), float(b), y_int


def print_equation(a, b, c):
    print(f"{a}x^2 + {b}x + {c}")


def str_equation(a, b, c):
    return f"{a}x^2 + {b}x + {c}"


def value_equation(a, b, c, x):
    return a * x**2 + b * x + c


def get_ball_travel_predicts(x1, y1, x2, y2):
    a, b, c = find_parabola(0, x1, y1, x2, y2)

    print_equation(a, b, c)

    roots = find_parabolic_roots(a, b, c)

    distance_traveled = max(roots)

    print(
        f"Equation: {str_equation(a, b, c)}\nDistance Traveled: {round(distance_traveled)} feet"
    )


def plot_graph(a, b, c, distance):
    x = np.linspace(0, distance, 100)
    y = x ** 2 * a + x * b + c

    plt.plot(x, y)
    plt.show()
