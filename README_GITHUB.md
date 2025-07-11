# Abdullah Graph Equation

A Python package for graphing mathematical equations from string input.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![PyPI](https://img.shields.io/pypi/v/abdullah-graph-eq)

## 🚀 Features

- **Easy to use**: Simply pass an equation as a string
- **Flexible**: Support for various mathematical functions
- **Customizable**: Adjust plot ranges, styling, and more
- **Save plots**: Export graphs to image files
- **Multiple equations**: Plot multiple equations on the same graph

## 📦 Installation

```bash
pip install abdullah_graph_eq
```

## 🎯 Quick Start

```python
from abdullah_graph_eq import graph_equation

# Graph a simple quadratic equation
graph_equation("x**2 + 2*x + 1")

# Graph a trigonometric function
graph_equation("sin(x)")

# Graph with custom range
graph_equation("x**3 - 2*x**2 + x - 1", x_range=(-5, 5))

# Save the plot
graph_equation("cos(x) + sin(2*x)", save_path="my_graph.png")
```

## 📊 Examples

### Linear Function
```python
graph_equation("2*x + 3")
```

### Quadratic Function
```python
graph_equation("x**2 - 4*x + 3")
```

### Trigonometric Function
```python
graph_equation("sin(x) + cos(2*x)")
```

### Exponential Function
```python
graph_equation("exp(-x**2) * sin(5*x)")
```

### Multiple Equations
```python
from abdullah_graph_eq import EquationGrapher

grapher = EquationGrapher()
grapher.plot_multiple([
    "x**2", 
    "x**3", 
    "sin(x)"
], x_range=(-3, 3))
```

## 🔧 API Reference

### `graph_equation(equation_str, **kwargs)`

**Parameters:**
- `equation_str` (str): The mathematical equation as a string
- `x_range` (tuple): Range of x values, default `(-10, 10)`
- `num_points` (int): Number of points to plot, default `1000`
- `title` (str): Plot title, default auto-generated
- `save_path` (str): Path to save the plot, optional
- `show` (bool): Whether to display the plot, default `True`

**Returns:**
- `matplotlib.figure.Figure`: The matplotlib figure object

### Supported Functions

| Function | Example | Description |
|----------|---------|-------------|
| `sin(x)` | `"sin(x)"` | Sine function |
| `cos(x)` | `"cos(x)"` | Cosine function |
| `tan(x)` | `"tan(x)"` | Tangent function |
| `exp(x)` | `"exp(x)"` | Exponential function |
| `log(x)` | `"log(x)"` | Natural logarithm |
| `sqrt(x)` | `"sqrt(x)"` | Square root |
| `abs(x)` | `"abs(x)"` | Absolute value |
| `x**n` | `"x**2"` | Power function |

## 🛠️ Development

### Setup Development Environment

```bash
git clone https://github.com/abdullahmashhadi/abdullah_graph_eq.git
cd abdullah_graph_eq
pip install -e .
```

### Run Tests

```bash
python -m pytest tests/ -v
```

### Build Package

```bash
python -m build
```

## 🧪 Testing

The package includes comprehensive tests for both parsing and graphing functionality:

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=abdullah_graph_eq

# Run specific test file
python -m pytest tests/test_parser.py -v
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📬 Contact

Abdullah Mashhadi - abdullah6blue@gmail.com

Project Link: [https://github.com/abdullahmashhadi/abdullah_graph_eq](https://github.com/abdullahmashhadi/abdullah_graph_eq)

## 🙏 Acknowledgments

- Built with [matplotlib](https://matplotlib.org/) for plotting
- Uses [sympy](https://www.sympy.org/) for mathematical expression parsing
- Powered by [numpy](https://numpy.org/) for numerical computations
