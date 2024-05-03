import unittest
from app.app import Crud
from models.plagueProductControl import PlagueProductControl

class AppTesting(unittest.TestCase):
    def setUp(self):
        self.client = None
        self.bill = None

        # Populate the store with products
        self.store = []
        self.store.append(Crud.Store.create_product("plague", "herbicida", 123456, 5, 150000.3))
        self.store.append(Crud.Store.create_product("plague", "fungicida", 123457, 3, 12000.5))
        self.store.append(Crud.Store.create_product("plague", "insecticida", 123458, 4, 5000.2))
        self.store.append(Crud.Store.create_product("plague", "acaricida", 123459, 12, 10000.1))
        self.store.append(Crud.Store.create_product("plague", "nematicida", 123460, 7, 20000.4))
        self.store.append(Crud.Store.create_product("fertilizer", "nitrogeno", 123461, 5, 150000.3))
        self.store.append(Crud.Store.create_product("fertilizer", "fosforo", 123462, 3, 12000.5))
        self.store.append(Crud.Store.create_product("fertilizer", "potasio", 123463, 4, 5000.2))
        self.store.append(Crud.Store.create_product("fertilizer", "calcio", 123464, 12, 10000.1))
        self.store.append(Crud.Store.create_product("fertilizer", "magnesio", 123465,  7, 20000.4))
  

        # Populate the store with antibiotics
        self.storeAntibiotics = []
        self.storeAntibiotics.append(Crud.Store.create_antibiotic("penicilina", "Bovinos", 150000.3, 402))
        self.storeAntibiotics.append(Crud.Store.create_antibiotic("amoxicilina", "Caprinos", 12000.5, 500))
        self.storeAntibiotics.append(Crud.Store.create_antibiotic("cefalosporina", "Porcinos", 5000.2, 599))
        self.storeAntibiotics.append(Crud.Store.create_antibiotic("tetraciclina", "Bovinos", 10000.1, 505))

            
    def test_create_client(self):
      self.client = Crud.Client().create_client("John Doe", "123456789")
      self.assertEqual(self.client.name, "John Doe")
      self.assertEqual(self.client.identificationNumber, 123456789)

    def test_add_product_to_bill(self):
      #addBill
      self.client = Crud.Client().create_client("John Doe", "123456789")
      productList = [self.store[0]]
      self.bill = Crud.Bill.create_bill(1, productList)
      self.client = Crud.Client().addBill(self.client, self.bill)
      self.assertEqual(len(self.client.billHistory), 1)


