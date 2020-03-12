class Pessoa:

    def __init__(self, nome, idade):
        self.nome  = nome;
        self.idade = idade;
     
    @property
    def nome(self):
        return self._nome;

    @nome.setter
    def nome(self, nome):
        self._nome = nome;

    @property
    def idade(self):
        return self._idade;

    @idade.setter
    def idade(self, idade):
        self._idade = idade;

