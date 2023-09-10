"""
# 2: Graphical Equation Solver

This program asks the user for two expressions, both involving the dependent variable 'y', and graphs them. It also calculates and prints the solution—the pair of x and y values that satisfy both equations.

Usage:
1. Enter the first expression, using 'y' as the dependent variable.
2. Enter the second expression, using 'y' as the dependent variable.

The program will display the graphs of both expressions along with the solution, showing the point where they intersect.
"""

import sympy

# Get user input for two expressions
expr1 = input("Enter the first expression, using 'y' as the dependent variable:\n> ")
expr2 = input("Enter the second expression, using 'y' as the dependent variable:\n> ")

try:
    # Simplify the input expressions
    expr1 = sympy.simplify(expr1)
    expr2 = sympy.simplify(expr2)
    
    # Solve for the intersection point
    ans = sympy.solve((expr1, expr2), dict=True)
    
    # Solve for 'y' in each expression to prepare for plotting
    expr1 = sympy.solve(expr1, sympy.Symbol('y'))[0]
    expr2 = sympy.solve(expr2, sympy.Symbol('y'))[0]
except sympy.SympifyError as e:
    print(e)
else:
    # Plot the expressions and the intersection point
    expr1_plot = sympy.plotting.plot(expr1, legend=True, line_color='b', show=False)
    expr2_plot = sympy.plotting.plot(expr2, legend=True, line_color='g', show=False)

    vertical_line = sympy.Eq(sympy.Symbol('x'), ans[0][sympy.Symbol('x')])
    vertical_line = sympy.plot_implicit(vertical_line, label="X", line_color='r', show=False)

    horizontal_line = sympy.plot(ans[0][sympy.Symbol('y')], label="Y", line_color='r', show=False)
    
    # Combine and display the plots
    expr1_plot.extend(expr2_plot)
    expr1_plot.extend(vertical_line)
    expr1_plot.extend(horizontal_line)

    expr1_plot.show()
