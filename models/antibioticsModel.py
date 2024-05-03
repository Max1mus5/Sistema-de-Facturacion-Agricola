class Antibiotic():
    def __init__(self, antibioticName, antibioticObjectPoblation, antibioticPrice, antibioticDosis):
        self._antibioticName = str(antibioticName)
        self._antibioticObjectPoblation = self.validate_poblation(antibioticObjectPoblation)
        self._antibioticPrice = float(antibioticPrice)
        self._antibioticDosis = int(antibioticDosis)

    @property
    def antibioticName(self):
        return self._antibioticName
    
    @antibioticName.setter
    def antibioticName(self, value):
        self._antibioticName = value

    @property
    def antibioticObjectPoblation(self):
        return self._antibioticObjectPoblation
    
    @antibioticObjectPoblation.setter
    def antibioticObjectPoblation(self, value):
        self._antibioticObjectPoblation = value

    @property
    def antibioticPrice(self):
        return self._antibioticPrice
    
    @antibioticPrice.setter
    def antibioticPrice(self, value):
        self._antibioticPrice = self.validate_dosis(value)

    @property
    def antibioticDosis(self):
        return self._antibioticDosis
    
    @antibioticDosis.setter
    def antibioticDosis(self, value):
        self._antibioticDosis = value

    def validate_poblation(self, poblation):
        valid_poblations = ["Bovinos", "Caprinos", "Porcinos"]
        if poblation not in valid_poblations:
            print(poblation)
            raise ValueError(f"La población objetivo debe ser una de las siguientes: {', '.join(valid_poblations)}")
        return poblation

    def validate_dosis(self, dosis):
        if not 400 <= dosis <= 600:
            raise ValueError("La dosis debe estar entre 400Kg y 600Kg")
        return dosis
