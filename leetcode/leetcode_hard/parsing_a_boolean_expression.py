"""
Leetcode 1106: Parsing a Boolean expression

A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

- 't' that evaluates to true.
- 'f' that evaluates to false.
- '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
- '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
- '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.

Given a string expression that represents a boolean expression,
return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.
"""


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if expression[0] == "t":
            return True
        if expression[0] == "f":
            return False
        if expression[0] == "!":
            return not self.parseBoolExpr(expression[2:-1])

        sub_expr = []
        depth = 0

        start = 2
        for i in range(2, len(expression) - 1):
            if expression[i] == "," and depth == 0:
                sub_expr.append(expression[start:i])
                start = i + 1
                i = start + 1
            elif expression[i] == "(":
                depth += 1
            elif expression[i] == ")":
                depth -= 1

        sub_expr.append(expression[start:-1])

        if expression[0] == "&":
            return all(self.parseBoolExpr(expr) for expr in sub_expr)

        elif expression[0] == "|":
            return any(self.parseBoolExpr(expr) for expr in sub_expr)
