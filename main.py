from app.app import Crud 

#crear productos de para la tienda
store = []
#productos de control de plagas:
store.append(Crud.Store.create_product("plague", "herbicida", 123456, 5, 150000.3))
store.append(Crud.Store.create_product("plague", "fungicida", 123457, 3, 12000.5))
store.append(Crud.Store.create_product("plague", "insecticida", 123458, 4, 5000.2))
store.append(Crud.Store.create_product("plague", "acaricida", 123459, 12, 10000.1))
store.append(Crud.Store.create_product("plague", "nematicida", 123460, 7, 20000.4))

#productos de control de fertilizantes:
store.append(Crud.Store.create_product("fertilizer", "nitrogeno", 123461, 5, 150000.3))
store.append(Crud.Store.create_product("fertilizer", "fosforo", 123462, 3, 12000.5))
store.append(Crud.Store.create_product("fertilizer", "potasio", 123463, 4, 5000.2))
store.append(Crud.Store.create_product("fertilizer", "calcio", 123464, 12, 10000.1))
store.append(Crud.Store.create_product("fertilizer", "magnesio", 123465,  7, 20000.4))

storeAntibiotics = []
#productos de antibioticos:
storeAntibiotics.append(Crud.Store.create_antibiotic("penicilina", "Bovinos", 150000.3, 402))
storeAntibiotics.append(Crud.Store.create_antibiotic("amoxicilina", "Caprinos", 12000.5, 500))
storeAntibiotics.append(Crud.Store.create_antibiotic("cefalosporina", "Porcinos", 5000.2, 599))
storeAntibiotics.append(Crud.Store.create_antibiotic("tetraciclina", "Bovinos", 10000.1, 505))

clientlist = []
options = Crud.Menu()
op = options

while op!= 10:
    op = options.show_menu()
    options.seleccionar_opcion(opcion=op, store=store, storeAntibiotics=storeAntibiotics)



""" # Crear un cliente
client=Crud.Client.create_client("Juan", 1234567890)

# Crear una factura
productList = [store[0], store[5], storeAntibiotics[2]]
bill1 = Crud.Bill.create_bill(1, productList)

#añadir una factura al usuario
client = Crud.Client.addBill(client, bill1)

#añadir un producto a la factura
bill1 = Crud.Bill.add_product(bill1, store[6])
client = Crud.Client.addBill(client, bill1)

#añadir un producto a la factura desde el cliente
client = Crud.Client.addProduct(client, 1, store[7])
Crud.Client.viewSingleBill(client,1)

#eliminar un producto de la factura
bill1 = Crud.Bill.delete_product(bill1, store[0])
client = Crud.Client.addBill(client, bill1)
Crud.Client.viewSingleBill(client,1) """


""" import unittest
from unittest import TestLoader

# Cargar las pruebas desde el archivo clientTest.py
test_loader = TestLoader()
test_suite_client = test_loader.loadTestsFromName('testing.clientTest.TestClient')

# Ejecutar las pruebas del cliente
test_runner = unittest.TextTestRunner()
test_runner.run(test_suite_client)

# Cargar las pruebas desde el archivo productsTest.py
test_suite_products = test_loader.loadTestsFromName('testing.productsTest.TestProducts')

# Ejecutar las pruebas de productos
test_runner.run(test_suite_products)

#load the tests from the programTest.py file
test_suite_program = test_loader.loadTestsFromName('testing.programTest.TestProductFunctionality')

#run the program tests
test_runner.run(test_suite_program)
 """