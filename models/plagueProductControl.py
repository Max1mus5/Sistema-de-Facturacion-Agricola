from models.productControlModel import ProductControl as ProductControlModel

class PlagueProductControl(ProductControlModel):
    def __init__(self, productName, productNumIca, productDailyFrecuency, productPrice, plagueCarencyPeriod):
        super().__init__(productName, productNumIca, productDailyFrecuency, productPrice)
        self.SpecificAttribute =  str(plagueCarencyPeriod)

    #define properties and setters for the new attribute
    @property
    def plagueSpecificAttribute(self):
        return self._SpecificAttribute
    
    @plagueSpecificAttribute.setter
    def plagueSpecificAttribute(self, value):
        self._SpecificAttributee = value

        
    