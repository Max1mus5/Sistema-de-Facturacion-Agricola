from models.clientModel import Client
from models.billModel import Bill 
from models.antibioticsModel import Antibiotic
from models.plagueProductControl import PlagueProductControl
from models.fertilizerProductControl import FertilizerProductControl
from models.productControlModel import ProductControl

class Crud:

  class Menu():
    def __init__(self, clientList=None):
        self._clientList = []
        self.bill = None
        self.client = None

    @property
    def clientList(self):
        return self._clientList
    
    @clientList.setter
    def clientList(self, client):
        self._clientList = client
        


    def show_menu(self):
        print("--------------------------------------------Bienvenido a la tienda de productos agricolas----------------------------------")
        print("1. Crear un cliente")
        print("2. Crear una factura")
        print("3. Agregar un producto a la factura")
        print("4. Eliminar un producto de la factura")
        print("5. Ver factura actual")
        print("6. Calcular el subtotal de la factura")
        print("7. Ver historial de facturas")
        print("8. Ver productos de la tienda")
        print("9. Buscar cliente por cedula")
        print("10. Salir")
        return input("Seleccione una opcion: ")
    
    def seleccionar_opcion(self, opcion, store, storeAntibiotics):
        print("----------------------------------------------------------------------------------------------------------------------------")
        if opcion == "1":
          client = self.first_menu_option()
          self._clientList.append(client)
          self.client=client

          return client
        elif opcion == "2":
          self.bill = self.second_menu_option()
          return self.bill
        elif opcion == "3":
          self.client = self.third_menu_option( store, storeAntibiotics)
          return self.client
        elif opcion == "4":
          self.fourth_menu_option(self.bill.billId)
          return self.client
        elif opcion == "5":
          self.fifth_menu_option()
          return self.client
        elif opcion == "6":
          self.sixth_menu_option(self.bill.billId)
          return self.client
        elif opcion == "7":
          self.seventh_menu_option()
        elif opcion == "8":
          self.eigth_menu_option(store, storeAntibiotics)
        elif opcion == "9":
          self.client = self.nineth_menu_option()
          return self.client
        elif opcion == "10":
          self.tenth_menu_option()
        elif opcion == "11":
          self.view_actualBill()
        else:
          print("Opcion no valida")
          return self.show_menu()
    
    def first_menu_option(self):
        print("Crear un cliente")
        name = input("Ingrese el nombre del cliente: ")
        identificationNumber = input("Ingrese el numero de identificacion del cliente: ")
        client = Crud.Client().create_client(name, identificationNumber)
        return client
    
    def second_menu_option(self):
        print("Crear una factura")
        billId = input("Ingrese el id de la factura: ")
        billProductList = []
        bill = Crud.Bill.create_bill(billId, billProductList)
        self.client = Crud.Client().addBill(self.client, bill)
        return bill
    
    def third_menu_option(self, store, storeAntibiotics):
        print("Agregar un producto a la factura")
        print("Productos disponibles:")
        for product in store:
          print(f"{product.productName}: ${product.productPrice}\n")
        for product in storeAntibiotics:
          print(f"{product.antibioticName}: ${product.antibioticPrice}\n")
        productName = input("Ingrese el nombre del producto: ")
        for product in store:
          if product.productName == productName:
            self.client = Crud.Client().addProduct(self.client, self.bill.billId,product)
          
        for antibiotic in storeAntibiotics:
          if antibiotic.antibioticName == productName:
            self.client = Crud.Client().addProduct(self.client, self.bill.billId,antibiotic)
        return self.client
    
    def fourth_menu_option(self,billId):
       print("Eliminar un producto de la factura")
       client = self.client
       for bill in self.client.billHistory:
          if bill.billId == billId:
            Crud.Client().viewSingleBill(self.client,billId)
            productName = input("Ingrese el nombre del producto a eliminar: ")
            for product in bill.billProductList:
              if product.productName == productName:
                self.bill = Crud.Bill.delete_product(bill, product)
                self.client = Crud.Client().addBill(client, bill)
              elif product.antibioticName == productName:
                self.bill = Crud.Bill.delete_product(bill, product)
                self.client = Crud.Client().addBill(client, bill)

    def fifth_menu_option(self):
        print("Ver factura actual")
        Crud.Client().viewSingleBill(self.client,self.bill.billId)    

    def sixth_menu_option(self, billId):
        print("Calcular el subtotal de la factura")
        billId = input("Ingrese el id de la factura: ")
        bill=None
        for bill in self.client.billHistory:
          if bill.billId == billId:
            print("El subtotal de la factura es: ", bill.calculate_subtotal())
        return self.client
    
    def seventh_menu_option(self):
        print("Ver historial de facturas")
        self.client.view_bill_history()

    def eigth_menu_option(self, store, storeAntibiotics):
        print("Ver productos de la tienda")
        print("Productos disponibles:")
        for product in store:
          print(f"{product.productName}: ${product.productPrice}\n")
        for product in storeAntibiotics:
          print(f"{product.antibioticName}: ${product.antibioticPrice}\n")
    
    def nineth_menu_option(self):
        print("Buscar cliente por cedula")
        print("Clientes disponibles:", len(self.clientList))
        identificationNumber = int(input("Ingrese el numero de identificacion del cliente: "))
        client = Crud.Client().buscarCliente(self.clientList, identificationNumber)
        if client is not None:
         Crud.Client().viewActualClient(client)
        else:
          print("El cliente no existe")
          return None
        
        return client
    
    def tenth_menu_option(self):
        print("Salir")
        print("Gracias por usar la tienda de productos agricolas")
        exit()        
        
  
  class Client():

    def __init__(self):
        self.client=None
    
    def create_client(self, name, identificationNumber):
        self.client = Client(name, identificationNumber)
        return self.client
    
    def buscarCliente(self, clientList, identificationNumber):
        for client in clientList:
          if client.identificationNumber == identificationNumber:
            self.client = client
            return self.client
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
        for bill in self.client.billHistory:
          if bill.billId == billId:
            self.client.billHistory.remove(bill)
            self.client.billHistory.append(bill)
          else:
            raise ValueError("La factura no existe")
        return self.client
    
    def addProduct(self, client, billid, product):
        self.client = client
        billInHistory = None
        for bill in self.client.billHistory: 
           if bill.billId == billid: 
                billInHistory = bill
        billadd = billInHistory.add_product(product)
        Crud.Client().updateBill(self.client, billadd, billadd.billId)
        return self.client
    
    def deleteBill(self, bill):
        for bill in self.client.billHistory:
          if bill == bill:
            self.client.billHistory.remove(bill)
        return self.client

    def viewSingleBill(self, client, billId):
        print(client.billHistory)
        if len(client.billHistory) == 0:
          print("No bills found")
        else: 
          for bill in client.billHistory:
            if bill.billId == billId:
              Crud.Bill.view_bill(bill)
              return bill
            else:
              print("No bills found")
          
    def viewActualClient(self, client):
        self.client = client
        print(f"Nombre: {self.client.name}\nCedula: {self.client.identificationNumber}\n")
        

    
  class Bill:
    def __init__(self):
        pass
    
    def create_bill(billId, billProductList):
        bill = Bill(billId, billProductList)
        return bill

    def add_product(bill, product):
        bill.add_product(product)
        return bill
    
    def delete_product(bill, product):
        #buscar por nombre y borrar si instancia de product entonces es producto.productName sino es producto.antibioticName
        productToDelete = product
        for product in bill.billProductList:
            if productToDelete == product:
              if isinstance(product, ProductControl):
                print("Se Borrara el producto:", product.productName)
                bill.billProductList.remove(productToDelete)

              elif isinstance(product, Antibiotic):
                print("Se Borrara el producto:", product.antibioticName)
                bill.billProductList.remove(productToDelete)
        bill.calculate_subtotal()

        
        if productToDelete is not None:

          return bill
        else:
          raise ValueError("El producto no existe")
      
    
    def change_product( bill, product, newProduct):
        for product in bill.billProductList:
          if product == product:
            bill.billProductList.remove(product)
            bill.billProductList.append(newProduct)
        return bill
    
    def view_bill(bill):
        products = ""
        for product in bill.billProductList:
          if isinstance(product, ProductControl):
            products += f"{product.productName}, "
          elif isinstance(product, Antibiotic):
            products += f"{product.antibioticName}, "
        print(f"Factura: {bill.billId}\nFecha: {bill.billDate}\nMonto: {bill.billAmount}\nProductos: {products}\n---------------------------------------")
    
  class Store:
    def __init__(self):
        pass

    def create_product(productType, productName, productNumIca, productDailyFrecuency, productPrice, **kwargs):
      if productType == "plague":
          return PlagueProductControl(productName, productNumIca, productDailyFrecuency, productPrice, kwargs.get('plagueCarencyPeriod'))
      elif productType == "fertilizer":
          return FertilizerProductControl(productName, productNumIca, productDailyFrecuency, productPrice, kwargs.get('applicationDate'))
      else:
          raise ValueError("Tipo de producto no reconocido")

    
    def create_antibiotic( antibioticName, antibioticObjectPoblation, antibioticPrice, antibioticDosis):
      product = Antibiotic(antibioticName, antibioticObjectPoblation, antibioticPrice, antibioticDosis)
      return product
