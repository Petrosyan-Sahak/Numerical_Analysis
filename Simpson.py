import numpy as np
from scipy import integrate


def approx(f, a=0, b=1, n_node=51, p=10):
    """
    Approximates functions integral with Simpsons formula.

    Given the function f, and node count of n_node
    calculates the integral of the function from a to b
    using Simpson's approximation
    """
    if not n_node & 1:
        raise ValueError("Number of nodes cannot be even.")

    n = (n_node - 1) // 2
    h = (b - a)/n
    nodes = np.linspace(a, b, n_node)
    values = f(nodes)

    sum = 0

    for i in range(n):
        sum += values[2*i] + 4*values[2*i+1] + values[2*i+2]
    sum *= h/6
    result, error = integrate.quad(f, a, b)
    print(f"{'Python calculated:':<20}{result:.{p}f}")
    print(f"{'We calculated:':<20}{sum:.{p}f}")
    print(f"{'Difference is':<20}{abs(result-sum):.{p}f}")


approx(np.sin, 0, 1, 9)
