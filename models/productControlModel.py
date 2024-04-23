class ProductControl():
  def __init__ (self, productName, productNumIca, productDailyFrecuency, productPrice):
    self.productName = str(productName);
    self.productNumIca = int(productNumIca);
    self.productDailyFrecuency = int(productDailyFrecuency);
    self.productPrice = float(productPrice);

  #define properties and setters for the new attribute
  @property
  def productName(self):
      return self._productName
  
  @productName.setter
  def productName(self, value):
      self._productName = value

  @property
  def productNumIca(self):
      return self._productNumIca
  
  @productNumIca.setter
  def productNumIca(self, value):
      self._productNumIca = value

  @property
  def productDailyFrecuency(self):
      return self._productDailyFrecuency
  
  @productDailyFrecuency.setter
  def productDailyFrecuency(self, value):
      self._productDailyFrecuency = value

  @property
  def productPrice(self):
      return self._productPrice
  
  @productPrice.setter
  def productPrice(self, value):
      self._productPrice = value

  