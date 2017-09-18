import re
from random import randint, choice
from operator import add, sub, neg, inv, mul, truediv

from PyQt5.QtWidgets import QLabel
from PyQt5 import QtGui

from sympy import S, pretty, solveset
from sympy.abc import x
from sympy.core.expr import Expr
from sympy.sets.sets import FiniteSet, EmptySet
from sympy.sets.fancysets import Complexes


def decimalizable(fraction):
    """Utility function that says if a sympy fraction
    can be made into a decimal fraction.

    >>> decimalizable(S("3 ,4"))
    True
    >>> decimalizable(S("2, 3"))
    False
    """
    _, d = fraction.as_numer_denom()
    pow2 = 1
    pow5 = 1
    while not d % pow2:
        pow2 *= 2
    while not d % pow5:
        pow5 *= 5
    pow2 /= 2
    pow5 /= 5
    return d == pow2 * pow5


def pretty_print(o, sign=True):
    """Utility function that formats a singleton expression.

    o: expression to format.
    sign: whether the + sign should appear (true by default)
    """
    s = pretty(o)
    s = s.replace("\n", "<br />")
    if sign and o.as_coeff_mul(x)[0] >= 0:
        s = "+" + s
    return s


def expr_to_cells(e, force_sign=False):
    """Format an expression into cells for the table in Equations."""
    e0, e1 = e.as_independent(x, as_Add=True)
    if e0 and e1:
        return (
              "<td>" + pretty_print(e1, sign=force_sign or False) + "</td>"
            + "<td>" + pretty_print(e0) + "</td>"
            )
    elif e1:
        return "<td>" + pretty_print(e1, sign=force_sign or False) + "</td><td/>"
    else:
        return "<td/><td>" + pretty_print(e0, sign=force_sign or False) + "</td>"


class Equation:
    """Inner representation of an equation.
    """
    def __init__(self, s="", random=False):
        """Takes a string in the form "expr1 = expr2" and makes
        an Equation object from it.
        If the string is empty, assumes "0 = 0".
        """

        if random:
            self.left  = choice((1, -1))*randint(1, 9) * x\
                       + choice((1, -1))*randint(0, 9)
            self.right = choice((1, -1))*randint(1, 9) * x\
                       + choice((1, -1))*randint(0, 9)
        elif s == "":
            self.left = S("0")
            self.right = S("0")
        else:
            self.left, self.right = map(S, s.split("="))

    def __str__(self):
        pieces = ["<tr>"]
        pieces += expr_to_cells(self.left)
        pieces += "<td> = </td>"
        pieces += expr_to_cells(self.right)
        pieces += '<td><img src=":/icons/thot.ico" /></td></tr><tr><td colspan="6">' + self.nSolutions() + '</td>' \
                  if self.isSolved()\
                  else ""
        pieces += "</tr>\n"
        return "".join(pieces)

    def __repr__(self):
        return "Equation('"\
               + str(self.left) + '=' + str(self.right)\
               + "')"

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

    def nSolutions(self):
        solutionset = solveset(self.left - self.right)
        if isinstance(solutionset, EmptySet):
            return "L'équation n'a pas de solution."
        if isinstance(solutionset, FiniteSet):
            return "L'équation a une unique solution : "\
                   + str(list(solutionset)[0]) + "."
        if isinstance(solutionset, Complexes):
            return "L'équation a une infinité de solutions."


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

    def __new__(cls, s=None, operator=None, operand=None):
        if s is not None:
            return cls.from_repr(s)
        else:
            return super().__new__(cls)

    def __init__(self, s=None, operator=None, operand=None):
        """Creates an operation wating to be applied to an equation.

        The operator has to be a function from module operator.
        Accepted values are add, sub, mul, truediv, neg and inv.
        An operand must be given for add, sub, mul and truediv,
        and no operand will be accepted for neg and inv. If this
        is not respected, an AttributeError will be raised.
        """

        if s is not None:
            return

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
        pieces = ['<tr class="operation">']

        if self.operator == add:
            pieces += expr_to_cells(self.operand, force_sign=True)
            pieces += "<td />"
            pieces += expr_to_cells(self.operand, force_sign=True)
        if self.operator == sub:
            pieces += expr_to_cells(-self.operand, force_sign=True)
            pieces += "<td />"
            pieces += expr_to_cells(-self.operand, force_sign=True)

        if self.operator == mul:
            pieces += "<td>× " + pretty_print(self.operand, sign=False) + "</td>"
            pieces += "<td>× " + pretty_print(self.operand, sign=False) + "</td>"
            pieces += "<td />"
            pieces += "<td>× " + pretty_print(self.operand, sign=False) + "</td>"
            pieces += "<td>× " + pretty_print(self.operand, sign=False) + "</td>"
        if self.operator == truediv:
            pieces += "<td>÷ " + pretty_print(self.operand, sign=False) + "</td>"
            pieces += "<td>÷ " + pretty_print(self.operand, sign=False) + "</td>"
            pieces += "<td />"
            pieces += "<td>÷ " + pretty_print(self.operand, sign=False) + "</td>"
            pieces += "<td>÷ " + pretty_print(self.operand, sign=False) + "</td>"

        if self.operator == inv:
            pieces += '<td colspan="5">Inversion des membres.</td>'
        if self.operator == neg:
            pieces += '<td colspan="5">Opposé des membres.</td>'

        pieces += "</tr>\n"
        return "".join(pieces)

    def __repr__(self):
        ret = "Operation('"
        if self.operator == add:
            ret += "+(" + repr(self.operand) + ")"
        if self.operator == sub:
            ret += "-(" + repr(self.operand) + ")"
        if self.operator == mul:
            ret += "*(" + repr(self.operand) + ")"
        if self.operator == truediv:
            ret += "/(" + repr(self.operand) + ")"
        if self.operator == inv:
            ret += "~"
        if self.operator == neg:
            ret += "-"
        ret += "')"
        return ret

    @classmethod
    def from_repr(cls, s):
        """Makes an Operation object from a string"""
        m = re.fullmatch("([+\-*/~])(\([\dx[+\-*/ ]+\))?", s)
        if m is None:
            raise ValueError("String is not a valid representation of an operation.")
        if m[1] == "+":
            return cls(operator=add, operand=S(m[2]))
        if m[1] == "-" and m[2]:
            return cls(operator=sub, operand=S(m[2]))
        if m[1] == "-":
            return cls(operator=neg)
        if m[1] == "*":
            return cls(operator=mul, operand=S(m[2]))
        if m[1] == "/":
            return cls(operator=truediv, operand=S(m[2]))
        if m[1] == "~":
            return cls(operator=inv)


class Equations(QLabel):
    """List of all steps made so far to solve the equation.
    """
    def __init__(self, parent=None, equation=Equation()):
        self.data = [equation]
        self.font_size = 18
        QLabel.__init__(self, self.makeHTML(), parent)

    def __repr__(self):
        ret = ["["]
        ret.extend((repr(item) + "," for item in self.data[:-1]))
        ret += [repr(self.data[-1]), "]"]
        return "\n".join(ret)

    def randomEquation(self):
        self.data = [Equation(random=True)]
        self.setText(self.makeHTML())

    def newEquation(self, eq):
        self.data = [eq]
        self.setText(self.makeHTML())

    def update(self, operation=Operation(operator=add, operand=S(0))):
        """Adds and apply an Operation to the list."""

        last_step = self.data[-1]
        result = operation(last_step)
        self.data.extend([operation, result])
        self.setText(self.makeHTML())

    def makeHTML(self):
        return ("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
            <html>
            <head>
            <meta name="qrichtext" content="1" />
            <style type="text/css">
            .frac { display: inline-block;
                position: relative;
                vertical-align: middle;
                letter-spacing: 0.001em;
                text-align: center;
            }
            .frac > span {
                display: block;
                padding: 0.1em;
            }
            .frac span.bottom {
                border-top: thin solid black;
            }
            .frac span.symbol {
                display: none;
            }

            td {
                text-align: center;
                vertical-align: middle;
                padding: 0px 1em 0px 1em;
                font: italic """ + str(self.font_size) + """px "Latin Modern Roman";
            }

            .operation > td {
                color: red;
            }
            </style>
            </head>
            <body style="text-align:center">
            <table>
            """
            + "".join(map(str, self.data))
            + """</table>
            </body>
            </html>
            """)

    def zoom_in(self):
        self.font_size += 2
        self.setText(self.makeHTML())

    def zoom_out(self):
        self.font_size -= 2
        self.setText(self.makeHTML())

    def clear_equation(self):
        """Resets the equation to the basic 0=0 equation."""
        self.data = [Equation()]
        self.setText(self.makeHTML())

    def cancel(self):
        """Cancels the last operation."""
        if len(self.data) >= 3:
            del self.data[-2:]
        self.setText(self.makeHTML())

    def loadFromRepr(self, s):
        self.data = eval(s)
        self.setText(self.makeHTML())

    def loadFromFile(self, fname, filter_):
        r = re.compile("\(\*(.p?tht)\)$")
        if re.search(".p?tht$", fname):
            with open(fname, 'r', encoding="utf-8") as f:
                self.loadFromRepr(f.read())
        else:
            with open(fname + r.search(filter_)[1], 'r', encoding="utf-8") as f:
                self.loadFromRepr(f.read())

    def saveToFile(self, fname, filter_):
        r = re.compile("\(\*(.p?tht)\)$")
        if r.search(fname):
            with open(fname, 'w', encoding="utf-8") as f:
                f.write(repr(self))
        else:
            print(filter_)
            with open(fname + r.search(filter_)[1], 'w', encoding="utf-8") as f:
                f.write(repr(self))

# vim: fdm=indent
