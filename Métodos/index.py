#Métodos de classes

class Pessoa:

    ano_atual = 2020;

    def __init__(self, nome, idade):
        self.nome  = nome;
        self.idade = idade;
    
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade);
    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento;
        return cls(nome, idade);

p1 = Pessoa.por_ano_nascimento('Luiz', 32);
print(p1.nome, p1.idade);
p1.get_ano_nascimento();

#Métodos estáticos

import random;

class Pessoa:

    ano_atual = 2020;

    def __init__(self, nome, idade):
        self.nome  = nome;
        self.idade = idade;
    
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade);
    
    @staticmethod
    def gera_id():
        return random.randint(10000, 19999);


print(Pessoa.gera_id());
