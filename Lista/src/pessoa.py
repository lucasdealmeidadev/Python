class Pessoa():
    def __init__(self, nome, idade, cpf):
        self.__nome      = nome;
        self.__idade     = idade;
        self.__cpf       = cpf;
        self.__telefones = [];
    
    def setNome(self, nome):
        self.__nome  = nome;

    def getNome(self):
        return self.__nome;

    def setIdade(self, idade):
        self.__idade = idade;

    def getIdade(self):
        return self.__idade;
    
    def setCpf(self, cpf):
        self.__cpf   = cpf;
    
    def getCpf(self):
        return self.__cpf;
    
    def setTelefones(self, telefones):
        self.__telefones = telefones;
    
    def getTelefones(self):
        return self.__telefones;