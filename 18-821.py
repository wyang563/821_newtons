from visualizer import *
from mpmath import mp, mpf, fadd, fmul, fsub, fdiv, log

mp.dps = 5000

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        res = mpf(0)
        x_to_the_i = mpf(1)
        for coeff in self.coefficients:
            res = fadd(res, fmul(mpf(coeff), x_to_the_i))
            x_to_the_i = fmul(x_to_the_i, x)
        return res
        # return sum(mpf(coef) * (x ** i) for i, coef in enumerate(self.coefficients))

    def derivative(self):
        return Polynomial([i * coef for i, coef in enumerate(self.coefficients[1:], 1)])

def newton_method(polynomial, initial_guess, tolerance=1e-6, max_iterations=100):
    x = mpf(initial_guess)
    guesses = []
    for _ in range(max_iterations):
        fx = polynomial(x)
        guesses.append((x, fx))
        # if abs(fx) < tolerance:
        #    return guesses
        dfx = polynomial.derivative()(x)
        # if dfx == 0:
        #     raise ValueError("Derivative is zero. Newton's method failed.")
        x = fsub(x, fdiv(fx, dfx))
    return guesses
    # raise ValueError(f"Newton's method did not converge after {max_iterations} iterations.")

def two_points_method(polynomial, x1, x2, tolerance=1e-6, max_iterations=100):
    guesses = []
    x1, x2 = mpf(x1), mpf(x2)
    for _ in range(max_iterations):
        y1 = polynomial(x1)
        y2 = polynomial(x2)
        guesses.append((x1, y1))
        # if abs(y2) < tolerance:
        #     return guesses
        # find x intercept of line through (x1, y1) and (x2, y2)
        x_intercept = fsub(x1, fmul(y1, fdiv(fsub(x2, x1), fsub(y2, y1))))
        x1, x2 = x2, x_intercept
    return guesses

# Example usage:
if __name__ == "__main__":
    # Create a polynomial: 2x^3 - 4x^2 + 3x - 6
    # p = Polynomial([6, -3, 4, -2])
    # p = Polynomial([-1, 0, 2, 0, 4, -5, 1, 12, 0, 15])
    p = Polynomial([-1, 0, 1])

    try:
        # guesses = newton_method(p, initial_guess=2.0, max_iterations=300)
        guesses = two_points_method(p, 2, 10, max_iterations=10)
        print("Guesses: ")
        for x, fx in guesses:
            # print('x: ' + str(float(x)))
            print('fx: ' + str(float(fx)))
            # print(format(fx, '.3f'))
            # print(f"{fx:.20f}")
        print("Log guesses: ")
        data = ([], [])
        """
        for i, (x, fx) in enumerate(guesses):
            log_guess = log(fx)
            print(float(log_guess))
            data[0].append(2**i)
            data[1].append(log_guess)
        plot_scatter(data)
        """
        print(f"Found root: {guesses[-1]}")
        plot_method(p, guesses)
    except ValueError as e:
        print(f"Error: {e}")
