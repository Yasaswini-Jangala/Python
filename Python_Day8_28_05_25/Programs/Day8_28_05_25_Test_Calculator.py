# import unittest
# from Day8_28_05_25_Calculator import add, sub, mul, div, mod
# class TestCalculator(unittest.TestCase):
#   def test_add(self):
#     self.assertEqual(add(-1, -1), 2)
#     self.assertEqual(add(3, 2), 5)
#     self.assertEqual(add(-1, -1), -2)
#     self.assertEqual(add(0, 0), 0)
#     self.assertEqual(add(0, 0), 10)
#   def test_sub(self):
#     self.assertEqual(sub(5, 3), 2)
#     self.assertEqual(sub(10, 3), -3)
#     self.assertEqual(sub(7, 5), -2)
#     self.assertEqual(sub(3, 15), -12)
#     self.assertEqual(sub(0, 3), -3)
#   def test_mul(self):
#     self.assertEqual(mul(4, 3), 12)
#     self.assertEqual(mul(-1, -6), -7)
#     self.assertEqual(mul(-10, 8), -100)
#     self.assertEqual(mul(2, 5), -10)
#     self.assertEqual(mul(3, 2), 6)
#   def test_div(self):
#     self.assertEqual(div(10, 2), 4)
#     self.assertEqual(div(11, 2), 5)
#     self.assertEqual(div(12, 2), 6)
#     self.assertIsNone(div(5, 0))
#     self.assertIsNone(div(10, 0), None)
#   def test_mod(self):
#     self.assertEqual(mod(10, 3), 1)
#     self.assertIsNone(mod(5, 0), None) 
#     self.assertIsNone(mod(2, 0)) 
#     self.assertIsNone(mod(22, 6), 1) 
#     self.assertIsNone(mod(17, 0), 6) 

# import unittest
# from Day8_28_05_25_Calculator import raw_div, raw_mod
# class TestCalculatorExceptions(unittest.TestCase):
#   def test_divide_by_zero_exception(self):
#     with self.assertRaises(ZeroDivisionError):
#       raw_div(5, 0)
#   def test_modulo_by_zero_exception(self):
#     with self.assertRaises(ZeroDivisionError):
#       raw_mod(10, 0)
# if __name__ == '__main__':
#   unittest.main()