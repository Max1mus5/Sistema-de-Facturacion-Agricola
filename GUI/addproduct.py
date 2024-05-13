from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog, labelText="Nombre del Producto"):  # Agregar un parámetro predeterminado para el texto de la etiqueta
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 240)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 301, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(70, 70, 121, 21))
        self.label.setObjectName("label")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(parent=Dialog)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(70, 90, 171, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")

        self.retranslateUi(Dialog, labelText)  # Pasar el labelText al método retranslateUi
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog, labelText):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", labelText))  # Usar el labelText para establecer el texto de la etiqueta en lugar de "Nombre del Producto"
