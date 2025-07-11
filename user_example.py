"""
Example usage of abdullah_graph_eq package
This shows how users will use your package in their main.py
"""

from abdullah_graph_eq import graph_equation

# Example 1: Simple quadratic equation (what the user asked for)
print("Graphing x^2 + 2*x + 1...")
graph_equation("x**2 + 2*x + 1")

# Example 2: Using different notation (^ instead of **)
print("\nGraphing x^2 + 2*x + 1 (using ^ notation)...")
graph_equation("x^2 + 2*x + 1")

# Example 3: Custom range
print("\nGraphing with custom range...")
graph_equation("x**2 + 2*x + 1", x_range=(-5, 3))

# Example 4: Save to file
print("\nGraphing and saving to file...")
graph_equation("x**2 + 2*x + 1", save_path="quadratic_graph.png", show=False)

# Example 5: Trigonometric function
print("\nGraphing trigonometric function...")
graph_equation("sin(x) + cos(2*x)")

# Example 6: More complex function
print("\nGraphing complex function...")
graph_equation("exp(-x**2/4) * sin(3*x)")
