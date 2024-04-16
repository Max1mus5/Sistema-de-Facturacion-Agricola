from models.productControlModel import ProductControl as ProductControlModel

class PlagueProductControl(ProductControlModel):
    def __init__(self, productName, productNumIca, productDailyFrecuency, productPrice, plagyeCarencyPeriod):
        super().__init__(productName, productNumIca, productDailyFrecuency, productPrice)
        self.plagueSpecificAttribute =  str(plagyeCarencyPeriod)