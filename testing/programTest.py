import unittest
from datetime import datetime
from models.clientModel import Client
from models.billModel import Bill
from models.antibioticsModel import Antibiotic
from models.plagueProductControl import PlagueProductControl
from models.fertilizerProductControl import FertilizerProductControl

class TestProductFunctionality(unittest.TestCase):

    def setUp(self):
        # Create a client
        self.client = Client("John Doe", 123456789)
        
        # Create a bill
        self.bill = Bill(1, "2024-04-14 10:00:00", [], 100.0)
        
        # Add the bill to the client's bill history
        self.client.add_bill(self.bill)
        
        # Create test products
        self.antibiotic = Antibiotic("Amoxicillin", "Bovinos", 10.50, 500)
        self.plague_control = PlagueProductControl("Plague Control", 200, 2, 25.00, "30 days")
        self.fertilizer_control = FertilizerProductControl("Fertilizer", 300, 1, 30.00, "2024-05-15")

    def test_add_products_to_bill(self):
        # Aadd products to the bill
        self.bill.add_product(self.antibiotic)
        self.bill.add_product(self.plague_control)
        self.bill.add_product(self.fertilizer_control)
        
        # Verify that the products were added correctly
        self.assertEqual(len(self.bill.billProductList), 3)
        self.assertIn(self.antibiotic, self.bill.billProductList)
        self.assertIn(self.plague_control, self.bill.billProductList)
        self.assertIn(self.fertilizer_control, self.bill.billProductList)

    def test_calculate_subtotal_and_total(self):
        # Add products to the bill
        self.bill.add_product(self.antibiotic)
        self.bill.add_product(self.plague_control)
        self.bill.add_product(self.fertilizer_control)
        
        # Calculate the expected subtotal and total
        expected_subtotal = self.antibiotic.antibioticPrice + self.plague_control.productPrice + self.fertilizer_control.productPrice
        expected_total = expected_subtotal + self.bill.billAmount
        
        # Verify that the subtotal and total were calculated correctly
        self.assertEqual(self.bill.calculate_subtotal(), expected_subtotal)
        self.assertEqual(self.bill.calculate_total(), expected_total)