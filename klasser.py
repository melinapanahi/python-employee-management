class Allmän:
    def __init__(self,namn, lön, avdelning):
        self.namn = namn
        self.lön = lön
        self.avdelning = avdelning

    def salary(self):
        print(f"{self.namn} jobbar på {self.avdelning} och tjänar {self.lön} kr per månad!")

class Chefer(Allmän):
    def __init__(self, namn, lön, avdelning,chef):
        super().__init__(namn, lön, avdelning) 
        self.chef = chef

    def person(self):
        print(f"chefen för {self.avdelning} avdelningen heter {self.chef}!")