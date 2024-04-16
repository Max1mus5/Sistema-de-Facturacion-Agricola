class Client():
    # set the base attributes for each client
    def __init__(self, name, identificationNumber, billHistory=None):
        self.name = str(name)
        self.identificationNumber = int(identificationNumber)
        self.billHistory = billHistory if billHistory is not None else []

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
        self._billHistory = value if value is not None else []

    def add_bill(self, bill):
        self._billHistory.append(bill)
