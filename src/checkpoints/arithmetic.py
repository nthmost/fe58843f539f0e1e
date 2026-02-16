"""Computational assessment checkpoint."""

import ast
import math
import re
import operator


def extract_expression(prompt: str) -> str:
    """Extract math expression from prompt."""
    # Look for expression after colon
    if ":" in prompt:
        parts = prompt.split(":", 1)
        if len(parts) > 1:
            expr = parts[1].strip()
            return expr

    # Fallback: find math expression
    match = re.search(r"\([^)]+Math\.[^)]+\)|Math\.\w+\([^)]+\)", prompt, re.IGNORECASE)
    if match:
        return match.group(0)

    raise ValueError(f"No math expression found in: {prompt}")


def convert_js_math(expr: str) -> str:
    """Convert JavaScript Math.* functions to Python equivalents."""
    expr = expr.replace("Math.floor", "math.floor")
    expr = expr.replace("Math.ceil", "math.ceil")
    expr = expr.replace("Math.round", "math.round")
    expr = expr.replace("Math.abs", "math.abs")
    return expr


def safe_eval(expr: str) -> int:
    """Safely evaluate math expression using AST."""
    python_expr = convert_js_math(expr)

    allowed_ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
    }

    try:
        return int(eval(python_expr, {"__builtins__": {}}, {"math": math}))
    except Exception as e:
        raise ValueError(f"Failed to evaluate {expr}: {e}")


def needs_pound_suffix(prompt: str) -> bool:
    """Check if result needs pound key suffix."""
    return "pound key" in prompt.lower() or "followed by #" in prompt.lower()


def handle_arithmetic(prompt: str) -> dict:
    """Handle computational assessment checkpoint."""
    expr = extract_expression(prompt)
    result = safe_eval(expr)
    digits = str(result)

    if needs_pound_suffix(prompt):
        digits += "#"

    return {"type": "enter_digits", "digits": digits}
