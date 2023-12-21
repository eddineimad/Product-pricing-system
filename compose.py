from produit import Produit
from composition import Composition
from elementaire import Elementaire

class Compose(Produit):
    def __init__(self, nom, code, frais, tva, liste):
        # Constructor
        super().__init__(nom, code)
        self.__frais = frais
        self.__tva = tva
        self.__liste = liste

    @property
    def Getfrais(self):
        # Getter for frais attribute
        return self.__frais
    
    @property
    def Gettva(self):
        # Getter for tva attribute
        return self.__tva
    
    @property
    def Getliste(self):
        # Getter for liste attribute
        return self.__liste
    
    def Setfrais(self, frais):
        # Setter for frais attribute
        self.__frais = frais

    def Settva(self, tva):
        # Setter for tva attribute
        self.__tva = tva
    
    def Setliste(self, liste):
        # Setter for liste attribute
        self.__liste = liste

    def __str__(self):
        p = ""
        for i in range(len(self.Getliste)):
            p += self.__liste[i].__str__()
        return f"{super().__str__()} Manufacturing costs: {str(self.Getfrais)}; VAT: {str(self.Gettva)}; List of constituents: {p}"

    @property
    def GetprixHT(self):
        prix = 0
        for i in range(len(self.__liste)):
            prix += self.__liste[i].Getproduit.GetprixAchat
        return prix + self.__frais
