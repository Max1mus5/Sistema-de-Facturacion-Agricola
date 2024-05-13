import sys
from PyQt6.QtWidgets import QApplication, QMainWindow  # Importa QMainWindow aquí
from GUI.menu import Ui_TiendaDeProductosAgricolas

class TiendaDeProductosAgricolas(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.ui = Ui_TiendaDeProductosAgricolas()
        self.ui.setupUi(self)
        self.show()
