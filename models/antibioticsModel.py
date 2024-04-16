class Antibiotic():
    def __init__(self, antibioticName, antibioticObjectPoblation, antibioticPrice, antibioticDosis):
        self.antibioticName = str(antibioticName)
        self.antibioticObjectPoblation = self.validate_poblation(antibioticObjectPoblation)
        self.antibioticPrice = float(antibioticPrice)
        self.antibioticDosis = self.validate_dosis(antibioticDosis)

    def validate_poblation(self, poblation):
        valid_poblations = ["Bovinos", "Caprinos", "Porcinos"]
        if poblation not in valid_poblations:
            raise ValueError(f"La población objetivo debe ser una de las siguientes: {', '.join(valid_poblations)}")
        return poblation

    def validate_dosis(self, dosis):
        if not 400 <= dosis <= 600:
            raise ValueError("La dosis debe estar entre 400Kg y 600Kg")
        return dosis
