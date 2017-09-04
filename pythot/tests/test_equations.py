import unittest
from sympy.abc import x
from ..equations import Equation


class testEquation(unittest.TestCase):
    def test_empty_init(self):
        eq = Equation()
        self.assertEqual(eq.left, 0)
        self.assertEqual(eq.right, 0)

    def test_init(self):
        eq = Equation("3*x+2 = 2*x-6")
        self.assertEqual(eq.left, 3*x+2)
        self.assertEqual(eq.right, 2*x-6)

    def test_add_equation(self):
        eq = Equation()
        eq2 = Equation("x=2*x")
        res = eq + eq2
        self.assertEqual(res.left, x)
        self.assertEqual(res.right, 2*x)

    def test_sub_equation(self):
        eq = Equation()
        eq2 = Equation("x=2*x")
        res = eq - eq2
        self.assertEqual(res.left, -x)
        self.assertEqual(res.right, -2*x)

    def test_mul_equation(self):
        eq = Equation("x=x")
        eq2 = Equation("x=2*x")
        res = eq * eq2
        self.assertEqual(res.left, x**2)
        self.assertEqual(res.right, 2*x**2)

    def test_div_equation(self):
        eq = Equation("x=2*x")
        eq2 = Equation("x=x")
        res = eq / eq2
        self.assertEqual(res.left, 1)
        self.assertEqual(res.right, 2)

    def test_add_expr(self):
        eq = Equation()
        res = eq + x
        self.assertEqual(res.left, x)
        self.assertEqual(res.right, x)

    def test_sub_expr(self):
        eq = Equation()
        res = eq - x
        self.assertEqual(res.left, -x)
        self.assertEqual(res.right, -x)

    def test_mul_expr(self):
        eq = Equation("x=x")
        res = eq * x
        self.assertEqual(res.left, x**2)
        self.assertEqual(res.right, x**2)

    def test_div_expr(self):
        eq = Equation("x=2*x")
        res = eq / x
        self.assertEqual(res.left, 1)
        self.assertEqual(res.right, 2)

    def test_inv(self):
        eq = Equation("x=2*x")
        res = ~eq
        self.assertEqual(res.left, 2*x)
        self.assertEqual(res.right, x)

    def test_neg(self):
        eq = Equation("x=2*x")
        res = -eq
        self.assertEqual(res.left, -x)
        self.assertEqual(res.right, -2*x)

    def test_is_solved(self):
        self.assertFalse(Equation("x=2*x").isSolved())
        self.assertFalse(Equation("2=2*x").isSolved())
        self.assertTrue(Equation("x=2").isSolved())
        self.assertTrue(Equation("2=2").isSolved())
        self.assertTrue(Equation("1=2").isSolved())
        self.assertTrue(Equation("2=x").isSolved())


if __name__ == "__main__":
    unittest.main()

# vim: fdm=indent
