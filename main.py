import unittest
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
