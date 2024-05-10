from app.app import Crud
from models.antibioticsModel import Antibiotic
from models.productControlModel import ProductControl


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
    #region Selecionar Opcion
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
    #region Primera Opcion
    def first_menu_option(self):
        print("Crear un cliente")
        name = input("Ingrese el nombre del cliente: ")
        identificationNumber = input("Ingrese el numero de identificacion del cliente: ")
        client = Crud.Client().create(name, identificationNumber)
        return client
        #region segunda Opcion

    def second_menu_option(self):
        print("Crear una factura")
        billId = input("Ingrese el id de la factura: ")
        billProductList = []
        bill = Crud.Bill().create(billId, billProductList)
        self.client = Crud.Client().addBill(self.client, bill)
        return bill
    #region Tercera Opcion
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
            self.client = Crud.Client().add_product(self.client, self.bill.billId,product)
          
        for antibiotic in storeAntibiotics:
          if antibiotic.antibioticName == productName:
            self.client = Crud.Client().add_product(self.client, self.bill.billId,antibiotic)
        return self.client
    #region Cuarta Opcion
    def fourth_menu_option(self, billId):
      print("Eliminar un producto de la factura")
      client = self.client
      for bill in self.client.billHistory:
          if bill.billId == billId:
              Crud.Client().view_bill(self.client, billId)
              productName = input("Ingrese el nombre del producto a eliminar: ")
              try:
                  for product in bill.billProductList:
                      if isinstance(product, Antibiotic):
                         if product.antibioticName == productName:
                            self.bill = Crud.Bill().delete(bill, product)
                            self.client = Crud.Client().addBill(client, bill)
                            break 
                      if isinstance(product, ProductControl):   
                          if product.productName == productName:
                            self.bill = Crud.Bill()().delete(bill, product)
                            self.client = Crud.Client().addBill(client, bill)
                            break 
                      else:
                          raise ValueError("Producto no encontrado")  
              except Exception as e:
                  print(f"Error al eliminar el producto: {e}")
                  continue 
              break 
      else:
          print("No se encontró la factura con el ID proporcionado.")

    #region Quinta Opcion
    def fifth_menu_option(self):
        print("Ver factura actual")
        Crud.Client().view_bill(self.client,self.bill.billId)    
    #region Sexta Opcion
    def sixth_menu_option(self, billId):
        print("Calcular el subtotal de la factura")
        billId = input("Ingrese el id de la factura: ")
        bill=None
        for bill in self.client.billHistory:
          if bill.billId == billId:
            print("El subtotal de la factura es: ", bill.calculate_subtotal())
        return self.client
    #region Septima Opcion
    def seventh_menu_option(self):
        print("Ver historial de facturas")
        self.client.view_bill_history()
    #region Octava Opcion
    def eigth_menu_option(self, store, storeAntibiotics):
        print("Ver productos de la tienda")
        print("Productos disponibles:")
        for product in store:
          print(f"{product.productName}: ${product.productPrice} - Caducate: ${product.SpecificAttribute}\n")
        for product in storeAntibiotics:
          print(f"{product.antibioticName}: ${product.antibioticPrice} - Dosis: ${product.antibioticDosis}\n")
    #region Novena Opcion
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
    #region Decima Opcion
    def tenth_menu_option(self):
        print("Salir")
        print("Gracias por usar la tienda de productos agricolas")
        exit()      