from PyQt5.QtCore import QStringListModel, Qt

from operator import add, sub, neg, inv, mul, truediv

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
            " = ".join(str(self.left), str(self.right))
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
        """Tells whether the equation is solved or not.

        >>> Equation("x=2").isSolved()
        True
        >>> Equation("2=x").isSolved()
        True
        >>> Equation("0=2").isSolved()
        True
        >>> Equation("x=2*x").isSolved()
        False
        """
        # The l0 and r0 are the constant terms
        # and l1 and r1 are the x-dependent ones.
        l0, l1 = self.left.as_independent(x, as_Add=True)
        r0, r1 = self.right.as_independent(x, as_Add=True)
        return (l0 == 0 and l1 == x and self.right.is_number
             or r0 == 0 and r1 == x and self.left.is_number
             or self.left.is_number and self.right.is_number)


class Operation:
    """Callable class that stores and applies an operation on
    an equation.
    """
    def __call__(self, equation):
        """Applies the operation to an equation."""

        if self.operand is None:
            return self.operator(equation)
        else:
            return self.operator(equation, self.operand)

    def __init__(self, operator, operand=None):
        """Creates an operation wating to be applied to an equation.

        The operator has to be a function from module operator.
        Accepted values are add, sub, mul, truediv, neg and inv.
        An operand must be given for add, sub, mul and truediv,
        and no operand will be accepted for neg and inv. If this
        is not respected, an AttributeError will be raised.
        """

        # Testing the arguments.
        if operator in [inv, neg] and operand is not None:
            raise AttributeError("No operand allowed with " + str(operator))
        if operator in [add, sub, mul, truediv]:
            if operand is None:
                raise AttributeError("Operand is compulsory with " + str(operator))
            elif not isinstance(operand, Equation) and not isinstance(operand, Expr):
                raise AttributeError("Operand must be an Equation or a sympy Expr")
        if operator not in [add, sub, mul, truediv, inv, neg]:
            raise AttributeError("Unknown operator " + str(operator))

        self.operator = operator
        self.operand = operand

    def __str__(self):
        if self.operator == add:
            return '+ ' + str(self.operand)
        if self.operator == sub:
            return '- ' + str(self.operand)
        if self.operator == mul:
            return '* ' + str(self.operand)
        if self.operator == mul:
            return '/ ' + str(self.operand)
        if self.operator == inv:
            return 'Inversion des membres.'
        if self.operator == neg:
            return 'Négation des membres.'


class Equations(QStringListModel):
    """List of all steps made so far to solve the equation.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = []

    # Used as a slot
    def update(self, operation):
        rc = self.rowCount()
        last_step = self.data(
            self.index(rc - 1, Qt.DisplayRole),
            Qt.DisplayRole)
        result = operation(last_step)
        if self.insertRows(rc, 2):
            self.setData(self.index(rc, Qt.DisplayRole), operation)
            self.setData(self.index(rc + 1, Qt.DisplayRole), result)

# vim: fdm=indent
