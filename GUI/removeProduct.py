# removeProduct.py
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_RemoveProduct(object):
    def setupUi(self, RemoveProduct):
        RemoveProduct.setObjectName("RemoveProduct")
        RemoveProduct.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=RemoveProduct)  
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(parent=RemoveProduct)  
        self.label.setGeometry(QtCore.QRect(70, 70, 121, 21))
        self.label.setObjectName("label")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(parent=RemoveProduct)  
        self.plainTextEdit_3.setGeometry(QtCore.QRect(70, 90, 171, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")

        self.retranslateUi(RemoveProduct)  
        self.buttonBox.accepted.connect(RemoveProduct.accept)  
        self.buttonBox.rejected.connect(RemoveProduct.reject)  
        QtCore.QMetaObject.connectSlotsByName(RemoveProduct)  

    def retranslateUi(self, RemoveProduct):
        _translate = QtCore.QCoreApplication.translate
        RemoveProduct.setWindowTitle(_translate("Eliminar Producto", "Dialog"))
        self.label.setText(_translate("Eliminar", "Nombre del Producto"))
