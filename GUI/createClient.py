from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CrearCliente(object):
    def setupUi(self, CrearCliente):
        CrearCliente.setObjectName("CrearCliente")
        CrearCliente.resize(320, 240)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=CrearCliente)
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=CrearCliente)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 50, 171, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(parent=CrearCliente)
        self.label.setGeometry(QtCore.QRect(50, 30, 49, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=CrearCliente)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 171, 16))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(parent=CrearCliente)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(50, 120, 171, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")

        self.retranslateUi(CrearCliente)
        self.buttonBox.accepted.connect(CrearCliente.accept) # type: ignore
        self.buttonBox.rejected.connect(CrearCliente.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(CrearCliente)


    def retranslateUi(self, CrearCliente):
        _translate = QtCore.QCoreApplication.translate
        CrearCliente.setWindowTitle(_translate("CrearCliente", "Dialog"))
        self.label.setText(_translate("CrearCliente", "Nombre"))
        self.label_2.setText(_translate("CrearCliente", "Numero de Identificación"))
