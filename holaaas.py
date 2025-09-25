<<<<<<< HEAD
# Bucle do-while (simulado en Python)
i = 0
while True:
  print(i)
  i += 1
  if i >= 5:
    break
  
  
=======
import numpy as np
from scipy.integrate import quad
from typing import Callable, List, Dict, Tuple, Union

import matplotlib.pyplot as plt

def numerical_integration(
    function: Callable[[float], float],
    a: float,
    b: float,
    method: str = 'trapezoidal',
    n: int = 1000
) -> float:
    """
    Calculates definite integral using various numerical methods.
    
    Parameters:
        function: The function to integrate
        a: Lower bound of integration
        b: Upper bound of integration
        method: Integration method ('trapezoidal', 'simpson', 'midpoint', 'scipy')
        n: Number of intervals
    
    Returns:
        Approximation of the definite integral
    """
    # Variable 1: h - step size
    h = (b - a) / n
    
    if method == 'trapezoidal':
        # Variable 2: result - accumulated sum
        result = 0.5 * (function(a) + function(b))
        for i in range(1, n):
            # Variable 3: x - current x value
            x = a + i * h
            result += function(x)
        return h * result
    
    elif method == 'simpson':
        # Simpson's rule requires even number of intervals
        if n % 2 == 1:
            n += 1
            h = (b - a) / n
            
        result = function(a) + function(b)
        # Variable 4: coefficient - multiplier for each term
        for i in range(1, n):
            x = a + i * h
            coefficient = 4 if i % 2 == 1 else 2
            result += coefficient * function(x)
        return h * result / 3
    
    elif method == 'midpoint':
        result = 0
        for i in range(n):
            # Variable 5: mid_x - midpoint of each interval
            mid_x = a + (i + 0.5) * h
            result += function(mid_x)
        return h * result
    
    elif method == 'scipy':
        # Using SciPy's built-in integration function
        # Variable 6: integral_result - output from scipy's quad function
        integral_result, _ = quad(function, a, b)
        return integral_result
    
    else:
        raise ValueError("Method must be 'trapezoidal', 'simpson', 'midpoint', or 'scipy'")


def polynomial_regression(
    x_data: List[float], 
    y_data: List[float], 
    degree: int = 2
) -> Tuple[np.ndarray, Callable[[Union[float, np.ndarray]], np.ndarray]]:
    """
    Performs polynomial regression on the given data.
    
    Parameters:
        x_data: Independent variable values
        y_data: Dependent variable values
        degree: Degree of the polynomial
        
    Returns:
        Tuple containing coefficients and the fitted function
    """
    # Variable 7: coefficients - polynomial coefficients
    coefficients = np.polyfit(x_data, y_data, degree)
    
    # Create a function from the coefficients
    def fitted_function(x):
        # Variable 8: y_pred - predicted values
        y_pred = 0
        for i, coef in enumerate(reversed(coefficients)):
            y_pred += coef * (x ** i)
        return y_pred
    
    return coefficients, fitted_function


def monte_carlo_simulation(
    trials: int = 10000,
    seed: int = None
) -> Dict[str, float]:
    """
    Performs Monte Carlo simulation to estimate π and calculate statistical measures.
    
    Parameters:
        trials: Number of random points to generate
        seed: Random seed for reproducibility
        
    Returns:
        Dictionary with results including π estimate and statistics
    """
    if seed is not None:
        np.random.seed(seed)
    
    # Variable 9: points_inside - counter for points inside circle
    points_inside = 0
    
    # Lists to store all x and y coordinates for statistical analysis
    x_coords = np.random.uniform(-1, 1, trials)
    y_coords = np.random.uniform(-1, 1, trials)
    
    for i in range(trials):
        # Calculate distance from origin
        distance = x_coords[i]**2 + y_coords[i]**2
        
        # Check if point is inside unit circle
        if distance <= 1:
            points_inside += 1
    
    # Variable 10: pi_estimate - estimate of π using Monte Carlo method
    pi_estimate = 4 * points_inside / trials
    
    # Calculate some statistics on the generated points
    stats = {
        "pi_estimate": pi_estimate,
        "error": abs(pi_estimate - np.pi),
        "relative_error": abs(pi_estimate - np.pi) / np.pi * 100,
        "x_mean": np.mean(x_coords),
        "y_mean": np.mean(y_coords),
        "x_std": np.std(x_coords),
        "y_std": np.std(y_coords)
    }
    
    return stats


# Example usage
if __name__ == "__main__":
    # Testing numerical integration
    print("Numerical Integration Example:")
    f = lambda x: np.sin(x) * np.exp(-x/3)
    a, b = 0, 10
    
    for method in ['trapezoidal', 'simpson', 'midpoint', 'scipy']:
        result = numerical_integration(f, a, b, method)
        print(f"  Method: {method}, Result: {result:.10f}")
    
    # Testing polynomial regression
    print("\nPolynomial Regression Example:")
    x = np.linspace(-5, 5, 20)
    # Generate synthetic data with some noise
    y = 3*x**3 - 5*x**2 + 2*x - 4 + np.random.normal(0, 10, 20)
    
    coeffs, func = polynomial_regression(x, y, 3)
    print(f"  True coefficients: [3, -5, 2, -4]")
    print(f"  Fitted coefficients: {coeffs}")
    
    # Testing Monte Carlo simulation
    print("\nMonte Carlo Simulation Example:")
    for trials in [1000, 10000, 100000]:
        stats = monte_carlo_simulation(trials, seed=42)
        print(f"  Trials: {trials}, π estimate: {stats['pi_estimate']:.10f}, "
            f"Error: {stats['error']:.10f}, Relative Error: {stats['relative_error']:.6f}%")
>>>>>>> f9e5126425cb5c3e7e3733fa6f29520bcbc646ec
