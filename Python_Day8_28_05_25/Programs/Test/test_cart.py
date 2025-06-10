import unittest
from App.cart import Cart
class TestCart(unittest.TestCase):
  def setUp(self):
    self.cart = Cart()
  def test_add_item(self):
    self.cart.add_item("Apple", 5)
    self.assertEqual(self.cart.total_items(), 5)
    self.cart.add_item("Cherry", -2)
    self.assertEqual(self.cart.total_items(), 3)
    self.assertEqual(self.cart.total_items(), 5)
  def test_add_zero_quantity(self):
    with self.assertRaises(ValueError):
      self.cart.add_item('Banana', 0)
if __name__ == 'main':
  unittest.main()