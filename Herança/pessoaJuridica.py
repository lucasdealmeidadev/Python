from pessoa import Pessoa;

class PessoaJuridica(Pessoa):

    def __init__(self, nome, idade, cnpj):
        super().__init__(nome, idade);
        self.cnpj = cnpj;
    
    @property
    def cnpj(self):
        return self._cnpj;
    
    @cnpj.setter
    def cnpj(self, cnpj):
        self._cnpj = cnpj;
    