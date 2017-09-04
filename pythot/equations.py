from PyQt5.QtCore import QStringListModel

from sympy import S
from sympy.abc import x
from sympy.core.expr import Expr


class Equation:
    """Inner representation of an equation.
    """
    def __init__(self, s=""):
        """Takes a string in the form "expr1 = expr2" and makes
        an Equation object from it.
        If the string is empty, assumes "0 = 0".
        """

        if s == "":
            self.left = S("0")
            self.right = S("0")
        else:
            self.left, self.right = map(S, s.split("="))

    def __str__(self):
        return (
            " = ".join(self.left, self.right)
            + '<img src=":/icons/thot.ico" />' if self.isSolved() else ""
            )

    def __add__(self, other):
        res = Equation()
        if isinstance(other, Equation):
            res.left = self.left + other.left
            res.right = self.right + other.right
        elif isinstance(other, Expr):
            res.left = self.left + other
            res.right = self.right + other
        else:
            raise TypeError(
                    "Addition : expected Equation or Expr got "
                    + type(other))
        return res

    def __sub__(self, other):
        res = Equation()
        if isinstance(other, Equation):
            res.left = self.left - other.left
            res.right = self.right - other.right
        elif isinstance(other, Expr):
            res.left = self.left - other
            res.right = self.right - other
        else:
            raise TypeError(
                    "Subtraction : expected Equation or Expr got "
                    + type(other))
        return res

    def __mul__(self, other):
        res = Equation()
        if isinstance(other, Equation):
            res.left = self.left * other.left
            res.right = self.right * other.right
        elif isinstance(other, Expr):
            res.left = self.left * other
            res.right = self.right * other
        else:
            raise TypeError(
                    "Multiplication : expected Equation or Expr got "
                    + type(other))
        return res

    def __truediv__(self, other):
        res = Equation()
        if isinstance(other, Equation):
            res.left = self.left / other.left
            res.right = self.right / other.right
        elif isinstance(other, Expr):
            res.left = self.left / other
            res.right = self.right / other
        else:
            raise TypeError(
                    "Division : expected Equation or Expr got "
                    + type(other))
        return res

    def __neg__(self):
        res = Equation()
        res.left = -self.left
        res.right = -self.right
        return res

    def __invert__(self):
        res = Equation()
        res.left = self.right
        res.right = self.left
        return res

    def isSolved(self):
        # The l0 and r0 are the constant terms
        # and l1 and r1 are the x-dependent ones.
        l0, l1 = self.left.as_independent(x, as_Add=True)
        r0, r1 = self.right.as_independent(x, as_Add=True)
        return (l0 == 0 and l1 == x and self.right.is_number
             or r0 == 0 and r1 == x and self.left.is_number
             or self.left.is_number and self.right.is_number)


class Equations(QStringListModel):
    """List of all steps made so far to solve the equation.
    """
    def __init__(self, base_equation, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.data = [base_equation]

    # Used as a slot
    def update(self, operation, operand):
        rc = self.rowCount()
        last_step = self.data(self.index(rc - 1, 0), 0)
        result = operation(last_step, operand)  # TODO
        if self.insertRow(rc):
            self.setData(self.index(rc, 0), result)

# vim: fdm=indent
