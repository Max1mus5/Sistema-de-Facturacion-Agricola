from models.productControlModel import ProductControl as ProductControlModel

class FertilizerProductControl(ProductControlModel):
  def __init__(self, productName, productNumIca, productDailyFrecuency, productPrice, aplicationDate):
    super().__init__(productName, productNumIca, productDailyFrecuency, productPrice)
    self.fertilizerSpecificAttribute = aplicationDate