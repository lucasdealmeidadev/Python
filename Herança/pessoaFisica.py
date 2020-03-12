from pessoa import Pessoa;

class PessoaFisica(Pessoa):

    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade);
        self.cpf = cpf;
    
    @property
    def cpf(self):
        return self._cpf;
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf;
