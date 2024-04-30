
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
    
    def add_bill(self, bill):
        from database.db import DB
        self._billHistory.append(bill)
        db= DB()
        db.agregar_factura(self.identificationNumber, self._billHistory)

    def view_bill_history(self):
        from database.db import DB
        db= DB()
        return db.ver_historial_facturas(self.identificationNumber)
    
    def delete_bill_from_history(self, billId):
        from database.db import DB
        for bill in self._billHistory:
            if bill.billId == billId:
                self._billHistory.remove(bill)
                #reenumerate bills
                for i in range(len(self._billHistory)):
                    self._billHistory[i].billId = i
                return True
                
                #delete in db
                db= DB()
                db.actualizar_en_archivo(self, self._billHistory)
        raise ValueError("esta factura no esta en tu historial")
