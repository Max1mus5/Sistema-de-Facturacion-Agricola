from models.clientModel import Client
from models.billModel import Bill 
from models.antibioticsModel import Antibiotic
from models.plagueProductControl import PlagueProductControl
from models.fertilizerProductControl import FertilizerProductControl
from models.productControlModel import ProductControl
from app.IStore import StoreInterface
from app.ICrud import CrudInterface
from app.IClient import IClientInterface

class Crud:
#region CLient
  class Client(IClientInterface, CrudInterface):

    def __init__(self):
        super().__init__()
        self.client=None
    
    def create(self, name, identificationNumber, clientList):
        if not name or not identificationNumber:
          return "No fue posible crear el cliente"
        else:
          #verify if the client already exists, if not, create it, else return the client
          if not self.buscarCliente(clientList, identificationNumber):
            client = Client(name, identificationNumber)
            return client
          else:
            return self.buscarCliente(clientList, identificationNumber)
    
    def buscarCliente(self, clientList, identificationNumber):
        for client in clientList:
          if client.identificationNumber == identificationNumber:
            return client
        
    
    def searchBillInClient(self, client, billId):
        for bill in client.billHistory:
          if bill.billId == billId:
            return bill
        return None
    
    def addBill ( self, client, bill):
        self.client = client

        if bill.billId not in [bill.billId for bill in self.client.billHistory]:
          self.client.billHistory.append(bill)
        else:
          Crud.Client().updateBill(self.client, bill, bill.billId)
        return self.client

    def updateBill(self, client, bill, billId):
        self.client = client
        try:
          for bill in self.client.billHistory:
            if bill.billId == billId:
              self.client.billHistory.remove(bill)
              self.client.billHistory.append(bill)
        except:
            raise ValueError("La factura no existe")
        return self.client
    
    def add_product(self, client, billid, product):
        self.client = client
        billInHistory = None
        for bill in self.client.billHistory: 
           if bill.billId == billid: 
                billInHistory = bill
        billadd = billInHistory.add_product(product)
        Crud.Client().updateBill(self.client, billadd, billadd.billId)
        return self.client
    
    def delete(self, bill):
        #Deletes a Bill
        for bill in self.client.billHistory:
          if bill == bill:
            self.client.billHistory.remove(bill)
        return self.client

    def view_bill(self, client, billId):
        if len(client.billHistory) == 0:
          print("No bills found")
        else: 
          for bill in client.billHistory:
            if bill.billId  == billId:
              Crud.Bill().view_bill(bill)
              return bill
            else:
              print("No bills found")
          
    def viewActualClient(self, client):
        self.client = client
        print(f"Nombre: {self.client.name}\nCedula: {self.client.identificationNumber}\n")
        

    #region BILL

  class Bill(CrudInterface):
    def __init__(self):
        super().__init__()

    def create(self, billId, billProductList):
        bill = Bill(billId, billProductList)
        return bill

    def add_product(self, bill, product):
        bill.add_product(product)
        return bill
    
    def delete(self, bill, product):
        #buscar por nombre y borrar si instancia de product entonces es producto.productName sino es producto.antibioticName
        productToDelete = product
        for product in bill.billProductList:
            if productToDelete == product:
              if isinstance(productToDelete, ProductControl):
                print("Se Borrara el producto:", productToDelete.productName)
                bill.billProductList.remove(productToDelete)
                break

              if isinstance(productToDelete, Antibiotic):
                print("Se Borrara el producto:", productToDelete.antibioticName)
                bill.billProductList.remove(productToDelete)
                break
              
              else:
                raise ValueError("El producto es de tipo:", )
        bill.calculate_subtotal()

        
        if productToDelete is not None:

          return bill
        else:
          raise ValueError("El producto no existe")
    
    def view_bill(self, bill):
        products = ""
        for product in bill.billProductList:
          if isinstance(product, ProductControl):
            products += f"{product.productName}, "
          elif isinstance(product, Antibiotic):
            products += f"{product.antibioticName}, "
        print(f"Factura: {bill.billId}\nFecha: {bill.billDate}\nMonto: {bill.billAmount}\nProductos: {products}\n---------------------------------------")
        return products
    
    #region Store

  class Store(StoreInterface):

    def __init__(self):
        super().__init__()

    def create_product(self, productType, productName, productNumIca, productDailyFrecuency, productPrice, aditionalatribute):
        if productType == "plague":
            return PlagueProductControl(productName, productNumIca, productDailyFrecuency, productPrice, plagueCarencyPeriod=aditionalatribute)
        elif productType == "fertilizer":
            return FertilizerProductControl(productName, productNumIca, productDailyFrecuency, productPrice, aplicationDate=aditionalatribute)
        else:
            raise ValueError("Tipo de producto no reconocido")

    def create_antibiotic(self, antibioticName, antibioticObjectPoblation, antibioticPrice, antibioticDosis):
        product = Antibiotic(antibioticName, antibioticObjectPoblation, antibioticPrice, antibioticDosis)
        return product

