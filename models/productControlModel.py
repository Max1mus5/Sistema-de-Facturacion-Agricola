class ProductControl():
  def __init__ (self, productName, productNumIca, productDailyFrecuency, productPrice):
    self.productName = str(productName);
    self.productNumIca = int(productNumIca);
    self.productDailyFrecuency = int(productDailyFrecuency);
    self.productPrice = float(productPrice);