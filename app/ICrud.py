from abc import ABC, abstractmethod

class CrudInterface(ABC):

    @abstractmethod
    def create(self, **kwargs):
        """
        Crea un nuevo objeto.
        """
        return NotImplementedError

    @abstractmethod
    def add_product(self, **kwargs):
        """
        Agrega un producto 
        """
        return NotImplementedError


    @abstractmethod
    def delete(self,**kwargs):
        """
        Elimina un objeto
        """
        return NotImplementedError

    @abstractmethod
    def view_bill(self, **kwargs):
        """
        Visualiza 
        """
        return NotImplementedError
