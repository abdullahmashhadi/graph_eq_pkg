"""
Example usage of the abdullah_graph_eq package.
"""

from abdullah_graph_eq import graph_equation

def main():
    """Demonstrate various equation plotting capabilities."""
    
    print("Abdullah Graph Equation - Example Usage")
    print("=" * 40)
    
    # Example 1: Simple quadratic
    print("\n1. Plotting quadratic equation: x**2 - 4*x + 3")
    graph_equation("x**2 - 4*x + 3", x_range=(-2, 6), show=False, save_path="quadratic.png")
    
    # Example 2: Trigonometric function
    print("\n2. Plotting trigonometric function: sin(x) + cos(2*x)")
    graph_equation("sin(x) + cos(2*x)", x_range=(-10, 10), show=False, save_path="trig.png")
    
    # Example 3: Exponential function
    print("\n3. Plotting exponential function: exp(-x**2/4) * sin(3*x)")
    graph_equation("exp(-x**2/4) * sin(3*x)", x_range=(-5, 5), show=False, save_path="exp_sin.png")
    
    # Example 4: Complex rational function
    print("\n4. Plotting rational function: (x**2 - 1)/(x**2 + 1)")
    graph_equation("(x**2 - 1)/(x**2 + 1)", x_range=(-5, 5), show=False, save_path="rational.png")
    
    print("\nAll plots saved as PNG files!")
    print("You can now display them or modify the code to show=True to display interactively.")

if __name__ == "__main__":
    main()
