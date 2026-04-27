import math
import re

def calculate_hypotenuse(a: float, b: float) -> float:
    return math.sqrt(a**2 + b**2)

def solve_quadratic(a: float, b: float, c: float) -> str:
    d = b**2 - 4*a*c
    if d < 0: return "Roots are complex."
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    return f"Roots: {r1}, {r2}"

def compound_interest(p: float, r: float, t: float, n: float = 12) -> float:
    return p * (1 + (r/100)/n)**(n * t)

def calculate_simple_interest(p: float, r: float, t: float) -> float:
    return (p * r * t) / 100

def general_calculator(expression: str) -> str:
    try:
        clean_expr = re.sub(r'[^0-9+\-*/().]', '', expression)
        allowed_names = {"math": math, "__builtins__": {}}
        return str(eval(clean_expr, allowed_names))
    except:
        return "Calculation error."