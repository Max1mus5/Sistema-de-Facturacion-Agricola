from datetime import datetime
from models.productControlModel import ProductControl
from models.antibioticsModel import Antibiotic

class Bill():
    def __init__(self, billId, billDate, billProductList=None, billAmount=0.0):
        self.billId = int(billId)
        if isinstance(billDate, str):
            self.billDate = datetime.strptime(billDate, '%Y-%m-%d %H:%M:%S')
        else:
            self.billDate = billDate
        self._billProductList = billProductList if billProductList is not None else []
        self.billAmount = float(billAmount)

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
        #add product to the list of products
        self._billProductList.append(product)

    def remove_product(self, product):
        #remove product from the list of products
        if product in self._billProductList:
            self._billProductList.remove(product)
        else:
            raise ValueError("El producto no se encuentra en la lista de productos de la factura")

    def calculate_subtotal(self):
        # Calculate the subtotal by summing the price of each product
        subtotal = 0
        for product in self._billProductList:
            if isinstance(product, ProductControl):
                subtotal += product.productPrice
            elif isinstance(product, Antibiotic):
                subtotal += product.antibioticPrice
        return subtotal
       
    def calculate_total(self):
        # Calculate the total by summing the subtotal and the bill amount
        return self.calculate_subtotal() + self.billAmount