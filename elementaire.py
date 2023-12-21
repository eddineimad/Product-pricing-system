from produit import Produit  
class Elementaire(Produit):
    def __init__(self, nom, code, prixAchat):
        # constructor to initialize
        super().__init__(nom, code)
        self.__prixAchat = prixAchat

    @property
    def GetprixAchat(self):
        # Getter for prixAchat attribute
        return self.__prixAchat
    
    def SetprixAchat(self, prixAchat):
        # Setter for prixAchat attribute
        self.__prixAchat = prixAchat

    def __str__(self):
        return f"{super().__str__()}  Purchase price: {str(self.GetprixAchat)}"

    def GetprixHT(self):
        return super().GetprixHT()
