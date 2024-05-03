
class Client():
    # set the base attributes for each client
    def __init__(self, name, identificationNumber, billHistory=None):
        self.name = str(name)
        self.identificationNumber = int(identificationNumber)
        self.billHistory =[]
        

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = str(value)

    @property
    def identificationNumber(self):
        return self._identificationNumber

    @identificationNumber.setter
    def identificationNumber(self, value):
        self._identificationNumber = int(value)

    @property
    def billHistory(self):
        return self._billHistory

    @billHistory.setter
    def billHistory(self, value):
        self._billHistory = value

    def view_bill_history(self):
      billHistory = self.billHistory
      if len(billHistory) == 0:
        return "No bills found"
      else:
          for bill in billHistory:
            print("Historial de facturas: \n", bill.billId)
            #imprimir la informacion usando ${}
            print(f"Fecha: {bill.billDate}\n Monto: {bill.billAmount}\n Productos: {len(bill.billProductList)}\n---------------------------------------")
