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
    def get_derrivative(coefs: list, x: float):
        der, func = 0, 0
        powers = [_ for _ in range(len(coefs) - 1, 0, -1)]
        der_powers = [_ - 1 for _ in powers]
        
        powers += [0]
        der_powers += [0]
        
        for i in range(len(coefs)):
            der += coefs[i] * powers[i] * x ** der_powers[i]
            func += coefs[i] * x ** powers[i]
        
        return der, func
    
    g_der, g = get_derrivative(g_coeffs, x)
    h_der, h = get_derrivative(h_coeffs, x)
    
    return ((g_der * h) - (g * h_der)) / (h ** 2)