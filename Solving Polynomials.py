import sympy


# Solve the expression x2 −3x + 2 = 0
x = sympy.symbols('x')
sol = sympy.solve(x**2 - 3 * x + 2, x)
print(sol)