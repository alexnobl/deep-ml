import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    
    def find_der(coef, x):
        tot = 0
        index = 0
        for p in range(len(coef) - 1 , 0, -1):
            tot += p * coef[index] * (x ** (p-1))
            index += 1
        return tot

    def func_out(coef, x):
        tot = 0
        index = 0
        for p in range(len(coef), 0, -1):
            tot += coef[index] * x ** (p - 1)
            index += 1
        return tot
    
    return ((find_der(g_coeffs, x) * func_out(h_coeffs, x)) - (find_der(h_coeffs, x) * func_out(g_coeffs, x))) / (func_out(h_coeffs, x) ** 2)
