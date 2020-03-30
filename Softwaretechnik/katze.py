class Katze():
    
    # Konstruktor
    def __init__(self):
        self.__name = ""
        self.__gewicht = 0.0
        self.energie = 100
    
    # Methoden
    def schlafe(self, energiegewinn):
        self.energie += energiegewinn
    
    def friss(self, energiegewinn):
        self.energie += energiegewinn
        
    def __schnurre(self, dauer):
        if dauer < 30:
            return "Grrrrrrrrrr"
        else:
            return "Hrrrrrrmrrrrrrr"
        
    def sageDeinenNamen(self):
        return self.__name
    
        
    