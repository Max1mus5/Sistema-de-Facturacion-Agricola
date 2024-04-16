import unittest
from datetime import datetime
from models.clientModel import Client
from models.billModel import Bill

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client("John Doe", 123456789)
        self.bill1 = Bill(1, "2024-04-14 10:00:00", ["Product1", "Product2"], 100.0)
        self.bill2 = Bill(2, "2024-04-15 11:00:00", ["Product3", "Product4"], 200.0)

    def test_create_client(self):
        self.assertEqual(self.client.name, "John Doe")
        self.assertEqual(self.client.identificationNumber, 123456789)

    def test_add_bill(self):
        self.client.add_bill(self.bill1)
        self.client.add_bill(self.bill2)
        self.assertEqual(len(self.client.billHistory), 2)
        self.assertIn(self.bill1, self.client.billHistory)
        self.assertIn(self.bill2, self.client.billHistory)

    def test_bill_has_product_list(self):
        self.client.add_bill(self.bill1)
        self.client.add_bill(self.bill2)
        self.assertEqual(self.client.billHistory[0].billProductList, ["Product1", "Product2"])
        self.assertEqual(self.client.billHistory[1].billProductList, ["Product3", "Product4"])

    def test_bill_is_has_relation_with_billModel(self):
        # Asociate the bills with the client
        self.client.add_bill(self.bill1)
        self.client.add_bill(self.bill2)
        
        # Verify that the bills are instances of the Bill class
        self.assertIsInstance(self.client.billHistory[0], Bill)
        self.assertIsInstance(self.client.billHistory[1], Bill)

    def test_setters(self):
        self.client.name = "Jane Doe"
        self.client.identificationNumber = 987654321
        self.assertEqual(self.client.name, "Jane Doe")
        self.assertEqual(self.client.identificationNumber, 987654321)