"""
Simpson's Rule Approximation Module

This module provides a function to approximate the definite integral 
of a given function using Simpson's rule. It compares the computed 
approximation to the result obtained using SciPy's integration 
method.

Functions:
----------
- approx(f, a=0, b=1, n_node=51, p=10):
    Approximates the integral of the function `f` over the interval 
    [a, b] using Simpson's rule. The number of nodes `n_node` must 
    be an odd number.

Dependencies:
-------------
- numpy
- scipy.integrate

Usage Example:
--------------
>>> import numpy as np
>>> from scipy import integrate
>>> from simpson_module import approx  # Assuming you save this as simpson_module.py
>>> f = lambda x: np.sin(x)
>>> approx(f, 0, np.pi, 51)

Output:
-------
Python calculated:   2.0000000000
We calculated:       2.0000000000
Difference is        0.0000000000
"""

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

    sum_n = 0

    for i in range(n):
        sum_n += values[2*i] + 4*values[2*i+1] + values[2*i+2]
    sum_n *= h/6
    result, _ = integrate.quad(f, a, b)
    print(f"{'Python calculated:':<20}{result:.{p}f}")
    print(f"{'We calculated:':<20}{sum_n:.{p}f}")
    print(f"{'Difference is':<20}{abs(result-sum_n):.{p}f}")


approx(np.sin, 0, 1, 9)

# import numpy as np
# from scipy import integrate
# from typing import Callable, Tuple


# def approx(
#     f: Callable[[np.ndarray], np.ndarray],
#     a: float = 0,
#     b: float = 1,
#     n_node: int = 51,
#     precision: int = 10
# ) -> Tuple[float, float, float]:
#     """
#     Approximates a function's integral using Simpson's rule.
#
#     Args:
#         f (Callable[[np.ndarray], np.ndarray]): The function to integrate.
#         a (float): The lower limit of integration.
#         b (float): The upper limit of integration.
#         n_node (int): The number of nodes (must be odd).
#         precision (int): The precision for displaying results.
#
#     Returns:
#         Tuple[float, float, float]: A tuple containing:
#             - simpson_integral: The integral computed using Simpson's rule.
#             - exact_integral: The integral computed using scipy's quad.
#             - difference: The absolute difference between the two results.
#     """
#     if not callable(f):
#         raise TypeError("f must be a callable function.")
#     if a >= b:
#         raise ValueError("Integration bounds must satisfy a < b.")
#     if n_node <= 1:
#         raise ValueError("Number of nodes must be greater than 1.")
#     if not n_node & 1:
#         raise ValueError("Number of nodes must be odd.")
#
#     # Nodes and function values
#     nodes = np.linspace(a, b, n_node)
#     values = f(nodes)
#     h = (b - a) / (n_node - 1)
#
#     # Simpson's rule (vectorized)
#     simpson_integral = h / 3 * (values[0] + 4 * np.sum(values[1:-1:2]) + 2 *
#     np.sum(values[2:-2:2]) + values[-1])
#
#     # Exact result using scipy
#     exact_integral, _ = integrate.quad(f, a, b)
#
#     # Return results
#     return simpson_integral, exact_integral, abs(exact_integral - simpson_integral)
#
#
# def print_results(
#     simpson_integral: float,
#     exact_integral: float,
#     difference: float,
#     precision: int
# ) -> None:
#     """
#     Prints the results of the integration.
#
#     Args:
#         simpson_integral (float): The integral computed using Simpson's rule.
#         exact_integral (float): The integral computed using scipy's quad.
#         difference (float): The absolute difference between the two results.
#         precision (int): The precision for displaying results.
#
#     Returns:
#         None
#     """
#     print(f"{'Python calculated:':<20}{exact_integral:.{precision}f}")
#     print(f"{'We calculated:':<20}{simpson_integral:.{precision}f}")
#     print(f"{'Difference is:':<20}{difference:.{precision}f}")
#
# # Example usage
# if __name__ == "__main__":
#     simpson_result, exact_result, diff = approx(np.sin, 0, np.pi, n_node=9, precision=10)
#     print_results(simpson_result, exact_result, diff, precision=10)
