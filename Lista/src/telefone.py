class Telefone():
    def __init__(self, numero):
        self.__numero = numero;
    
    def setNumeroTelefone(self, numero):
        self.__numero = numero;
    
    def getNumeroTelefone(self):
        return self.__numero;
