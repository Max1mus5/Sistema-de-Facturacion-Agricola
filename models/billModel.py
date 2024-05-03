from datetime import datetime
from models.productControlModel import ProductControl
from models.antibioticsModel import Antibiotic

class Bill():
    def __init__(self, billId, billProductList, billAmount=0.0):
        self.billId = int(billId)
        self.billDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._billProductList = billProductList if billProductList is not None else []
        self.billAmount = float(self.calculate_subtotal())

    @property
    def billProductList(self):
        return self._billProductList

    @billProductList.setter
    def billProductList(self, value):
        if not isinstance(value, list):
            raise ValueError("billProductList debe ser una lista")
        self._billProductList = value

    @property
    def billId(self):
        return self._billId
    
    @billId.setter
    def billId(self, value):
        self._billId = value

    @property
    def billDate(self):
        return self._billDate
    
    @billDate.setter
    def billDate(self, value):
        self._billDate = value

    @property
    def billAmount(self):
        return self._billAmount
    
    @billAmount.setter
    def billAmount(self, value):
        self._billAmount = value

    def add_product(self, product):
        self._billProductList.append(product)
        self.calculate_subtotal()
        return self

    
    def calculate_subtotal(self):
      # Calculate the subtotal by summing the price of each product
      subtotal = 0
      for product in self._billProductList:
        if isinstance(product, ProductControl):
          subtotal += product.productPrice
        elif isinstance(product, Antibiotic):
          subtotal += product.antibioticPrice
      self.billAmount = subtotal
      return subtotal


    