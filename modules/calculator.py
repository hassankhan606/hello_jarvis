"""modules/calculator.py — Safe mathematical expression evaluator."""

import ast, math, operator

_SAFE_FUNCS = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
_SAFE_FUNCS.update({"abs": abs, "round": round, "pow": pow})

class _SafeEval(ast.NodeVisitor):
    OPS = {
        ast.Add: operator.add, ast.Sub: operator.sub,
        ast.Mult: operator.mul, ast.Div: operator.truediv,
        ast.Pow: operator.pow,  ast.Mod: operator.mod,
        ast.FloorDiv: operator.floordiv,
        ast.USub: operator.neg, ast.UAdd: operator.pos,
    }

    def visit_Expression(self, node): return self.visit(node.body)
    def visit_Num(self, node): return node.n          # py <3.8
    def visit_Constant(self, node): return node.value
    def visit_BinOp(self, node):
        return self.OPS[type(node.op)](self.visit(node.left),
                                       self.visit(node.right))
    def visit_UnaryOp(self, node):
        return self.OPS[type(node.op)](self.visit(node.operand))
    def visit_Call(self, node):
        name = node.func.id if isinstance(node.func, ast.Name) else None
        if name not in _SAFE_FUNCS:
            raise ValueError(f"Forbidden function: {name}")
        args = [self.visit(a) for a in node.args]
        return _SAFE_FUNCS[name](*args)
    def visit_Name(self, node):
        if node.id in _SAFE_FUNCS:
            return _SAFE_FUNCS[node.id]
        raise ValueError(f"Unknown name: {node.id}")
    def generic_visit(self, node):
        raise ValueError(f"Unsupported: {type(node).__name__}")

def calculate(expr: str) -> str:
    expr = expr.strip().replace("^", "**")
    if not expr:
        return "Please enter an expression."
    try:
        tree   = ast.parse(expr, mode="eval")
        result = _SafeEval().visit(tree)
        return f"{expr} = {result}"
    except ZeroDivisionError:
        return "Division by zero."
    except Exception as e:
        return f"Calculation error: {e}"
