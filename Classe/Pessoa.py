class Pessoa :
    
    def __init__(self, nome, idade):
        self.nome  = nome;
        self.idade = idade;
    
    def setNome(self, nome):
        self.nome  = nome;
    
    def setIdade(self, idade):
        self.idade = idade;
    
    def getNome(self):
        return self.nome;
    
    def getIdade(self):
        return self.idade;

if __name__ == "__main__":
    
    pessoa = Pessoa('Lucas de Almeida Monteiro', 23);
    print('Nome  = ', pessoa.nome);
    print('Idade = ', pessoa.idade);