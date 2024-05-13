from PyQt6 import QtCore, QtGui, QtWidgets
from models.plagueProductControl import PlagueProductControl
from models.fertilizerProductControl import FertilizerProductControl
from models.antibioticsModel import Antibiotic
from models.productControlModel import ProductControl

class Ui_ViewProducts(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Crear un QVBoxLayout para organizar los productos
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Crear un widget de desplazamiento
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 793, 593))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout.addWidget(self.scrollArea)
        
        # Establecer un QVBoxLayout para organizar los productos dentro del área de desplazamiento
        self.scrollAreaVerticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaVerticalLayout.setObjectName("scrollAreaVerticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def addProduct(self, product):
        groupBox = QtWidgets.QGroupBox()
        groupBox.setObjectName("groupBox")
        
        # Crear un QVBoxLayout para este QGroupBox
        groupBoxLayout = QtWidgets.QVBoxLayout(groupBox)
        groupBoxLayout.setObjectName("groupBoxLayout")
        
        # Agregar la información del producto al QGroupBox
        productLabel = QtWidgets.QLabel(groupBox)
        productLabel.setObjectName("productLabel")
        if isinstance(product, ProductControl):
          productLabel.setText(f"Nombre: {product.productName}\n"
                              f"Número ICA: {product.productNumIca}\n"
                              f"Frecuencia diaria: {product.productDailyFrecuency}\n"
                              f"Precio: {product.productPrice}\n")
        if isinstance(product, Antibiotic):
          productLabel.setText(f"Nombre del antibiótico: {product.antibioticName}\n"
                              f"Población objetivo: {product.antibioticObjectPoblation}\n"
                              f"Precio: {product.antibioticPrice}\n"
                              f"Dosis: {product.antibioticDosis}\n")
        
        # Agregar etiquetas específicas para cada tipo de producto
        if isinstance(product, PlagueProductControl):
            productLabel.setText(productLabel.text() + f"Período de carencia: {product.SpecificAttribute}\n")
        elif isinstance(product, FertilizerProductControl):
            productLabel.setText(productLabel.text() + f"Fecha de aplicación: {product.SpecificAttribute}\n")
        
        groupBoxLayout.addWidget(productLabel)
        
        # Agregar el QGroupBox al QVBoxLayout del área de desplazamiento
        self.scrollAreaVerticalLayout.addWidget(groupBox)
