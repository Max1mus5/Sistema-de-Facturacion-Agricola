from models.productControlModel import ProductControl as ProductControlModel

class FertilizerProductControl(ProductControlModel):
  def __init__(self, productName, productNumIca, productDailyFrecuency, productPrice, aplicationDate):
    super().__init__(productName, productNumIca, productDailyFrecuency, productPrice)
    self.fertilizerSpecificAttribute = aplicationDate

    #define properties and setters for the new attribute
    @property
    def fertilizerSpecificAttribute(self):
        return self._fertilizerSpecificAttribute
    
    @fertilizerSpecificAttribute.setter
    def fertilizerSpecificAttribute(self, value):
        self._fertilizerSpecificAttribute = value

    