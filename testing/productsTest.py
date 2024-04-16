import unittest
from datetime import datetime
from models.billModel import Bill
from models.antibioticsModel import Antibiotic
from models.plagueProductControl import PlagueProductControl
from models.fertilizerProductControl import FertilizerProductControl

class TestProducts(unittest.TestCase):

  def setUp(self):
    # Create test products
    self.antibiotic = Antibiotic("Amoxicillin", "Bovinos", 10.50, 500)
    self.plague_control = PlagueProductControl("Plague Control", 200, 2, 25.00, "30 days")
    self.fertilizer_control = FertilizerProductControl("Fertilizer", 300, 1, 30.00, "2024-05-15")
    
    # Create a test bill
    self.bill = Bill(1, "2024-04-14 10:00:00", [], 100.0)

  def test_add_product(self):
    # Add products to the bill
    self.bill.add_product(self.antibiotic)
    self.bill.add_product(self.plague_control)
    self.bill.add_product(self.fertilizer_control)
    
    # Verify that the products were added correctly
    self.assertEqual(len(self.bill.billProductList), 3)
    self.assertIn(self.antibiotic, self.bill.billProductList)
    self.assertIn(self.plague_control, self.bill.billProductList)
    self.assertIn(self.fertilizer_control, self.bill.billProductList)

  def test_remove_product(self):
    # Add and then remove a product
    self.bill.add_product(self.antibiotic)
    self.bill.remove_product(self.antibiotic)
    
    # Verify that the product was removed correctly
    self.assertEqual(len(self.bill.billProductList), 0)
    self.assertNotIn(self.antibiotic, self.bill.billProductList)

  def test_product_types(self):
    # Add products and verify their types
    self.bill.add_product(self.antibiotic)
    self.bill.add_product(self.plague_control)
    self.bill.add_product(self.fertilizer_control)
    
    # Verify that the products are instances of the expected classes
    self.assertIsInstance(self.bill.billProductList[0], Antibiotic)
    self.assertIsInstance(self.bill.billProductList[1], PlagueProductControl)
    self.assertIsInstance(self.bill.billProductList[2], FertilizerProductControl)

  def test_product_superProduct_herency(self):
    # Verify that the products inherit the attributes of the ProductControl class
    self.assertEqual(self.plague_control.productName, "Plague Control")
    self.assertEqual(self.plague_control.productNumIca, 200)
    self.assertEqual(self.plague_control.productDailyFrecuency, 2)
    self.assertEqual(self.plague_control.productPrice, 25.00)
    
    self.assertEqual(self.fertilizer_control.productName, "Fertilizer")
    self.assertEqual(self.fertilizer_control.productNumIca, 300)
    self.assertEqual(self.fertilizer_control.productDailyFrecuency, 1)
    self.assertEqual(self.fertilizer_control.productPrice, 30.00)

    with self.assertRaises(AttributeError):
            # try to access an attribute that is not in the class antibioticº
            productNumIca = self.antibiotic.productNumIca



