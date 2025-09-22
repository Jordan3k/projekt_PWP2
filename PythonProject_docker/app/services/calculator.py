
import ast
from dataclasses import dataclass
from typing import Any

class CalculatorError(ValueError):
    pass

class Calculator:

    def evaluate(self, expression: str) -> float:
        if not expression:
            raise CalculatorError("Puste wyrażenie.")


        try:
            parsed = ast.parse(expression, mode="eval")
            value = self._eval_node(parsed.body)
        except CalculatorError:
            raise
        except Exception as exc: # pragma: no cover - breadth of ast errors
            raise CalculatorError(f"Błędne wyrażenie: {exc}") from exc


        # Normalize -0.0 to 0.0 and round tiny fp artifacts
        result = float(value)
        if abs(result) < 1e-12:
            result = 0.0
        return result


    # --- internal helpers -------------------------------------------------


    def _eval_node(self, node: ast.AST) -> float:
        if isinstance(node, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            return self._apply_binop(node.op, left, right)
        if isinstance(node, ast.UnaryOp):
            operand = self._eval_node(node.operand)
            return self._apply_unary(node.op, operand)
        if isinstance(node, ast.Num): # Python <=3.7
            return float(node.n)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        raise CalculatorError("Dozwolone są tylko liczby i operatory + - * / oraz nawiasy.")


    def _apply_binop(self, op: ast.AST, left: float, right: float) -> float:
        if isinstance(op, ast.Add):
            return left + right
        if isinstance(op, ast.Sub):
            return left - right
        if isinstance(op, ast.Mult):
            return left * right
        if isinstance(op, ast.Div):
            if right == 0:
                raise CalculatorError("Dzielenie przez zero.")
                return left / right
        raise CalculatorError("Niedozwolony operator.")


    def _apply_unary(self, op: ast.AST, value: float) -> float:
        if isinstance(op, ast.UAdd):
            return +value
        if isinstance(op, ast.USub):
            return -value
        raise CalculatorError("Niedozwolony operator unarny.")