from abc import ABCMeta, abstractmethod

class Produit(metaclass=ABCMeta):
    def __init__(self, nom, code):
        self.__nom = nom
        self.__code = code

    @property
    def Getnom(self):
        # Getter for nom attribute
        return self.__nom
    
    @property
    def Getcode(self):
        # Getter for code attribute
        return self.__code
    
    def Setnom(self, nom):
        # Setter for nom attribute
        self.__nom = nom

    def Setcode(self, code):
        # Setter for code attribute
        self.__code = code

    def __str__(self):
        return f'Name : {str(self.Getnom)}    ;Code:  {str(self.Getcode)} ;'

    def __eq__(self, other):
        return self.__code == other.__code
    
    @abstractmethod
    def GetprixHT(self):
        # Abstract method
        pass
