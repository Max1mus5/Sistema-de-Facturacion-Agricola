from PyQt6 import QtCore, QtGui, QtWidgets
from GUI.createClient import Ui_CrearCliente
from GUI.addproduct import Ui_Dialog
from app.app import Crud
from GUI.productsCreated import store, storeAntibiotics
from GUI.removeProduct import Ui_RemoveProduct
from GUI.actualBill import Ui_MainWindow
from GUI.billHistory import Ui_BillHistory
from GUI.viewProducts import Ui_ViewProducts
from models.antibioticsModel import Antibiotic
from models.productControlModel import ProductControl


class Ui_TiendaDeProductosAgricolas(object):
    def __init__(self):
        self._clientList = []
        self.bill = None
        self.client = None
        

        @property
        def clientList(self):
            return self._clientList
        
        @clientList.setter
        def clientList(self, client):
            self._clientList = client

    def setupUi(self, TiendaDeProductosAgricolas):
        TiendaDeProductosAgricolas.setObjectName("TiendaDeProductosAgricolas")
        TiendaDeProductosAgricolas.resize(800, 577)
        self.centralwidget = QtWidgets.QWidget(parent=TiendaDeProductosAgricolas)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout") 
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.groupBox = QtWidgets.QGroupBox(parent=self.frame)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 4, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout.addWidget(self.frame)
        TiendaDeProductosAgricolas.setCentralWidget(self.centralwidget)

        self.retranslateUi(TiendaDeProductosAgricolas)
        self.pushButton.objectNameChanged['QString'].connect(TiendaDeProductosAgricolas.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(TiendaDeProductosAgricolas)
#region CRUID
        #App CRUD
        # Conectar el botón "Crear Cliente" a la función openCreateClientDialog
        self.pushButton.clicked.connect(self.openCreateClientDialog)

        # Conectar "Crear una factura" a la función createBill
        self.bill=self.pushButton_2.clicked.connect(self.createBill)

        # Conectar "Agregar un producto a la factura" a la función openAddProductDialog
        self.pushButton_3.clicked.connect(self.openAddProductDialog)

        # Conectar "Eliminar un producto de la factura" a la función openRemoveProductDialog
        self.pushButton_4.clicked.connect(self.openRemoveProductDialog)

        # Conectar "Ver factura actual" a la función openActualBill
        self.pushButton_5.clicked.connect(self.openActualBill)

        # Conectar "Calcular el subtotal de la factura" a la función calculateSubtotal
        self.pushButton_6.clicked.connect(self.calculateSubtotal)

        # Conectar "Ver Historial de Facturas" a la función viewBillHistory
        self.pushButton_7.clicked.connect(self.viewBillHistory)

        # Conectar "Ver productos de la tienda" a la función viewProducts
        self.pushButton_8.clicked.connect(self.viewProducts)

        # Conectar "Buscar cliente por cedula" a la función openSearchClientDialog
        self.pushButton_9.clicked.connect(self.openSearchClientDialog)



        


    def retranslateUi(self, TiendaDeProductosAgricolas):
        _translate = QtCore.QCoreApplication.translate
        TiendaDeProductosAgricolas.setWindowTitle(_translate("TiendaDeProductosAgricolas", "MainWindow"))
        self.label.setText(_translate("TiendaDeProductosAgricolas", "Tienda Agricola"))
        self.groupBox.setTitle(_translate("TiendaDeProductosAgricolas", "Elija Una Opcion"))
        self.pushButton.setText(_translate("TiendaDeProductosAgricolas", "Crear Cliente"))
        self.pushButton_8.setText(_translate("TiendaDeProductosAgricolas", "Ver productos de la tienda"))
        self.pushButton_2.setText(_translate("TiendaDeProductosAgricolas", "Crear una factura"))
        self.pushButton_7.setText(_translate("TiendaDeProductosAgricolas", "Ver historial de facturas"))
        self.pushButton_3.setText(_translate("TiendaDeProductosAgricolas", "Agregar un producto a la factura"))
        self.pushButton_6.setText(_translate("TiendaDeProductosAgricolas", "Calcular el subtotal de la factura"))
        self.pushButton_4.setText(_translate("TiendaDeProductosAgricolas", "Eliminar un producto de la factura"))
        self.pushButton_5.setText(_translate("TiendaDeProductosAgricolas", "Ver factura actual"))
        self.pushButton_9.setText(_translate("TiendaDeProductosAgricolas", "Buscar cliente por cedula"))
        
    
    #funciones de conexion
    def openCreateClientDialog(self):
        self.createClientDialog = QtWidgets.QDialog()
        self.createClientDialog.ui = Ui_CrearCliente()
        self.createClientDialog.ui.setupUi(self.createClientDialog)
        self.createClientDialog.ui.buttonBox.accepted.connect(self.createClient)
        self.createClientDialog.exec()
        return self.client
    
    def openAddProductDialog(self):
        self.addProductDialog = QtWidgets.QDialog()
        self.addProductDialog.ui = Ui_Dialog()
        self.addProductDialog.ui.setupUi(self.addProductDialog)
        self.addProductDialog.ui.buttonBox.accepted.connect(self.addProductToBill)
        self.addProductDialog.exec()
        return self.client
    
    def openRemoveProductDialog(self):
        self.removeProductDialog = QtWidgets.QDialog()
        self.removeProductDialog.ui = Ui_RemoveProduct()
        self.removeProductDialog.ui.setupUi(self.removeProductDialog)
        self.removeProductDialog.ui.buttonBox.accepted.connect(self.removeProductFromBill)
        self.removeProductDialog.exec()
        return self.client
    
    def openActualBill(self):
        client= self.client
        self.actualBillDialog = QtWidgets.QMainWindow()
        self.actualBillDialog.ui = Ui_MainWindow()
        self.actualBillDialog.ui.setupUi(self.actualBillDialog)
        self.actualBillDialog.ui.clienteActual.setText(str(client.name))
        self.actualBillDialog.ui.idClienteActual.setText(str(client.identificationNumber))
        bill = Crud.Client().searchBillInClient(client, self.bill.billId)
        self.actualBillDialog.ui.idFactura.setText(str(bill.billId))
        self.actualBillDialog.ui.fechaFactura.setText(str(bill.billDate))
        self.actualBillDialog.ui.montoFactura.setText(str(bill.calculate_subtotal()))
        self.actualBillDialog.ui.productos.setText(Crud.Bill().view_bill(bill))
        self.actualBillDialog.show()
        return self.client
        
    def openSearchClientDialog(self):
        self.addProductDialog = QtWidgets.QDialog()
        self.addProductDialog.ui = Ui_Dialog()

        # Cambiar el texto de la etiqueta a "Ingrese Numero de Cedula"
        self.addProductDialog.ui.setupUi(self.addProductDialog, "Ingrese Cedula")
        self.addProductDialog.ui.buttonBox.accepted.connect(self.searchClient)
        self.addProductDialog.exec()
        return self.client



    
        


    #funciones de CRUD
    #region Crear CLiente
    def createClient(self):
        name = self.createClientDialog.ui.plainTextEdit.toPlainText()
        identification_number = self.createClientDialog.ui.plainTextEdit_2.toPlainText()
        
        if not name.strip() or not identification_number.strip():
            QtWidgets.QMessageBox.critical(self.createClientDialog, "Error", "Por favor, complete todos los campos.")
            return
        clientList = self._clientList
        client=Crud.Client().buscarCliente(clientList, int(identification_number))
        #buscar el cliente en la lista de clientes si ya existe no lo agrega de lo contrario lo agrega
        if client:
            self.client = client
            QtWidgets.QMessageBox.information(self.createClientDialog, "Bienvenido", f"Ya existe un cliente con este numero de cedula.\nBienvenido {self.client.name}")
            return self.client
        else:
            
            client = Crud.Client().create(name, identification_number,clientList)
            self._clientList.append(client)
            self.client = client

        if isinstance(client, str):
            QtWidgets.QMessageBox.critical(self.createClientDialog, "Error", client)
        else:
            QtWidgets.QMessageBox.information(self.createClientDialog, "Éxito", "Cliente creado con éxito.")
            self.createClientDialog.accept()
            return self.client
    

    #region Crear factura
    def createBill(self):
        import random
        billId = random.randint(1, 1000)
        billProductList = []
        bill = Crud.Bill().create(billId, billProductList)
        self.bill = bill

        # Verificar si ya se ha creado un cliente
        if not self.client:
            self.openCreateClientDialog() #pongo a crear un cliente al usuario en caso de que no haya ninguno

        self.client = Crud.Client().addBill(self.client, bill)

        if not bill:
            QtWidgets.QMessageBox.critical(self.createClientDialog, "Error", "No se pudo crear la factura.")
        else:
            QtWidgets.QMessageBox.information(self.createClientDialog, "Éxito", "Factura creada con éxito.")
            self.createClientDialog.accept()
            return self.bill

    #region Agregar producto a la factura
    def addProductToBill(self):
        productName = self.addProductDialog.ui.plainTextEdit_3.toPlainText()
        print(productName)
        #quiero validar si me entran varios productos me entran de la forma:
        productoEncontrado = False
        try:
            for product in store:
                if product.productName == productName:
                    self.client = Crud.Client().add_product(self.client, self.bill.billId, product)
                    self.bill = Crud.Client().searchBillInClient(self.client, self.bill.billId)
                    productoEncontrado=True
                    break
                    
            for antibiotic in storeAntibiotics:
                if antibiotic.antibioticName == productName:
                    self.client = Crud.Client().add_product(self.client, self.bill.billId, antibiotic)
                    self.bill = Crud.Client().searchBillInClient(self.client, self.bill.billId)
                    productoEncontrado =True
                    break

        except Exception as e:
            QtWidgets.QMessageBox.critical(self.addProductDialog, "Error", f"Error al agregar el producto: {e}")
        
        if productoEncontrado:
            QtWidgets.QMessageBox.information(self.addProductDialog, "Éxito", f"Producto {productName} agregado con éxito.")
        else:
            QtWidgets.QMessageBox.critical(self.addProductDialog, "Error", f"Producto {productName} no encontrado.")

        
            
        return self.client


    def removeProductFromBill(self):
        productName = self.removeProductDialog.ui.plainTextEdit_3.toPlainText()
        client = self.client        
        print(len(self.bill.billProductList))
        # Buscar la factura por ID
        for bill in self.client.billHistory:
            if bill.billId == self.bill.billId:
                try:
                    # Iterar sobre los productos de la factura
                    for product in bill.billProductList:
                        # Verificar si el producto es de tipo Antibiotic
                        if isinstance(product, Antibiotic):
                            if product.antibioticName == productName:
                                # Eliminar el producto de la factura
                                self.bill = Crud.Bill().delete(bill, product)
                                self.client = Crud.Client().addBill(client, bill)
                                QtWidgets.QMessageBox.information(self.removeProductDialog, "Producto Eliminado", "El producto ha sido eliminado de la factura.")
                                return self.client
                        # Verificar si el producto es de tipo ProductControl
                        elif isinstance(product, ProductControl):
                            if product.productName == productName:
                                # Eliminar el producto de la factura
                                self.bill = Crud.Bill().delete(bill, product)
                                self.client = Crud.Client().addBill(client, bill)
                                QtWidgets.QMessageBox.information(self.removeProductDialog, "Producto Eliminado", "El producto ha sido eliminado de la factura.")
                                return self.client
                    else:
                        # Si no se encontró el producto, mostrar un mensaje de error
                        QtWidgets.QMessageBox.warning(self.removeProductDialog, "Producto no encontrado", "No se encontró el producto en la factura.")
                except Exception as e:
                    # Manejar cualquier error que ocurra durante el proceso
                    QtWidgets.QMessageBox.warning(self.removeProductDialog, "Error", f"Error al eliminar el producto: {e}")
                    break
                else:
                    # Si se eliminó el producto, salir del bucle
                    break
        else:
            # Si no se encontró la factura, mostrar un mensaje de error
            QtWidgets.QMessageBox.warning(self.removeProductDialog, "Factura no encontrada", "No se encontró la factura.")


    #region Calcular Subtotal 
    def calculateSubtotal(self):
        bill = self.bill
        subtotal = bill.calculate_subtotal()
        QtWidgets.QMessageBox.information(self.createClientDialog, "Subtotal", f"El subtotal de la factura es: {subtotal}")
        self.createClientDialog.accept()        
        return self.client
    
    #region Ver Historial de Facturas
    def viewBillHistory(self):
        client = self.client
        self.billHistoryDialog = QtWidgets.QMainWindow()
        self.billHistoryDialog.ui = Ui_BillHistory()
        self.billHistoryDialog.ui.setupUi(self.billHistoryDialog)
        self.billHistoryDialog.ui.clienteActual.setText(str(client.name))
        self.billHistoryDialog.ui.idClienteActual.setText(str(client.identificationNumber))
        for bill in client.billHistory:
            self.billHistoryDialog.ui.appendBillBox(bill,Crud.Bill().view_bill(bill))
        self.billHistoryDialog.show()
        return self.client
    #region Ver Productos

    def viewProducts(self):
        self.viewProductsDialog = QtWidgets.QMainWindow()
        self.viewProductsDialog.ui = Ui_ViewProducts()
        self.viewProductsDialog.ui.setupUi(self.viewProductsDialog)
        for product in store:
            self.viewProductsDialog.ui.addProduct(product)

        for antibiotic in storeAntibiotics:
            self.viewProductsDialog.ui.addProduct(antibiotic)
        self.viewProductsDialog.show()

    #region Buscar Cliente
    def searchClient(self):
        identification_number = int(self.addProductDialog.ui.plainTextEdit_3.toPlainText())
        clientList = self._clientList
        client = Crud.Client().buscarCliente(clientList, identification_number)
        if client:
            self.client = client
            QtWidgets.QMessageBox.information(self.addProductDialog, "Éxito", f"Cliente encontrado.\nClientes Totales: {len(clientList)}")
            QtWidgets.QMessageBox.information(self.addProductDialog, "Éxito", f"Bienvenido De Nuevo {client.name}")
            self.addProductDialog.accept()
            return self.client
        else:
            print(client)
            QtWidgets.QMessageBox.critical(self.addProductDialog, "Error", "Cliente no encontrado.")
        return self.client