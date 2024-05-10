from abc import ABC, abstractmethod

class StoreInterface(ABC):

    @abstractmethod
    def create_product(self, productType, productName, productNumIca, productDailyFrecuency, productPrice, aditionalatribute):
        """
        Crea un nuevo producto en la tienda.
        """
        pass

    @abstractmethod
    def create_antibiotic(self, antibioticName, antibioticObjectPoblation, antibioticPrice, antibioticDosis):
        """
        Crea un nuevo antibiótico en la tienda.
        """
        pass
