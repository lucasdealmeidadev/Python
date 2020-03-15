"""
    public, protected, private 
    _privado / protected (public _)
    __ privado (_NOMECLASSE_nomeatributo)
"""

class Base:
    def __init__(self):
        self.__dados = {}; 
    
    def inserir_cliente(self, id, nome):

        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome};
        
        else:
            self.__dados['clientes'].update({id: nome});

    def listar_clientes(self):

        for id, nome in self.__dados['clientes'].items():
            print(id, nome);

    def apaga_cliente(self, id):

        del self.__dados['clientes'][id];

bd = Base();
bd.inserir_cliente(1, 'Lucas de Almeida');
bd.inserir_cliente(2, 'André');
bd.inserir_cliente(3, 'Maria');
bd.apaga_cliente(2);
bd.listar_clientes();