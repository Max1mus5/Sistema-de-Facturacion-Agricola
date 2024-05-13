from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_BillHistory(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 595)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 791, 581))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")   
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 51, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 49, 16))
        self.label_2.setObjectName("label_2")
        self.clienteActual = QtWidgets.QLabel(parent=self.frame)
        self.clienteActual.setGeometry(QtCore.QRect(70, 20, 49, 16))
        self.clienteActual.setObjectName("clienteActual")
        self.idClienteActual = QtWidgets.QLabel(parent=self.frame)
        self.idClienteActual.setGeometry(QtCore.QRect(70, 40, 49, 16))
        self.idClienteActual.setObjectName("idClienteActual")
        
        # Cambiar frame_2 a un QScrollArea
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(20, 70, 761, 501))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 759, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        # Establecer un QVBoxLayout para organizar los QGroupBox dentro del scroll area
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cliente:"))
        self.label_2.setText(_translate("MainWindow", "Id:"))
        self.clienteActual.setText(_translate("MainWindow", "TextLabel"))
        self.idClienteActual.setText(_translate("MainWindow", "TextLabel"))

    def appendBillBox(self, bill, productos):
        groupBox = QtWidgets.QGroupBox()
        groupBox.setObjectName("groupBox")
        
        # Crear un QVBoxLayout para este QGroupBox
        groupBoxLayout = QtWidgets.QVBoxLayout(groupBox)
        groupBoxLayout.setObjectName("groupBoxLayout")
        
        # Agregar los widgets al QVBoxLayout del QGroupBox
        idFactura = QtWidgets.QLabel(groupBox)
        idFactura.setObjectName("idFactura")
        idFactura.setText("Factura ID:\t"+ str(bill.billId))
        groupBoxLayout.addWidget(idFactura) 
        
        fechaFactura = QtWidgets.QLabel(groupBox)
        fechaFactura.setObjectName("fechaFactura")
        fechaFactura.setText("Fecha:\t"+str(bill.billDate))
        groupBoxLayout.addWidget(fechaFactura)
        
        montoFactura = QtWidgets.QLabel(groupBox)
        montoFactura.setObjectName("montoFactura")
        montoFactura.setText("Total De Compra:\t"+str(bill.billAmount))
        groupBoxLayout.addWidget(montoFactura)
        
        productosLabel = QtWidgets.QLabel(groupBox)
        productosLabel.setObjectName("productosLabel")
        productosLabel.setText("Productos Comprados:\n"+productos)
        groupBoxLayout.addWidget(productosLabel)
        
        # Agregar el QGroupBox al QVBoxLayout del QScrollArea
        self.verticalLayout.addWidget(groupBox)
        
        return groupBox
