class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        return sum(coef * (x ** i) for i, coef in enumerate(self.coefficients))

    def derivative(self):
        return Polynomial([i * coef for i, coef in enumerate(self.coefficients[1:], 1)])

def newton_method(polynomial, initial_guess, tolerance=1e-6, max_iterations=100):
    x = initial_guess
    guesses = []
    for _ in range(max_iterations):
        fx = polynomial(x)
        guesses.append(fx)
        if abs(fx) < tolerance:
            return guesses
        dfx = polynomial.derivative()(x)
        if dfx == 0:
            raise ValueError("Derivative is zero. Newton's method failed.")
        x = x - fx / dfx
    raise ValueError(f"Newton's method did not converge after {max_iterations} iterations.")

# Example usage:
if __name__ == "__main__":
    # Create a polynomial: 2x^3 - 4x^2 + 3x - 6
    p = Polynomial([6, -3, 4, -2])

    try:
        root = newton_method(p, initial_guess=-1.0)[-1]
        print(f"Found root: {root}")
        print(f"f({root}) = {p(root)}")
    except ValueError as e:
        print(f"Error: {e}")

