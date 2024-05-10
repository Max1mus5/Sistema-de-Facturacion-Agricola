from abc import ABC, abstractmethod

class IClientInterface(ABC):

    @abstractmethod
    def buscarCliente(self, clientList, identificationNumber):
        """
        Busca un cliente por número de identificación.
        """
        pass

    @abstractmethod
    def addBill(self, client, bill):
        """
        Agrega una factura al historial de facturas de un cliente.
        """
        pass

    @abstractmethod
    def updateBill(self, client, bill, billId):
        """
        Actualiza una factura existente en el historial de facturas de un cliente.
        """
        pass

    @abstractmethod
    def viewActualClient(self, client):
        """
        Visualiza información actual del cliente.
        """
        pass
