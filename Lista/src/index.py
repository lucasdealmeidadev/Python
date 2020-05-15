from pessoa   import Pessoa;
from telefone import Telefone;
import os;

class Index:

    os.system('cls');
    listaTelefones = [];

    nome   = str(input('Informe seu nome  :'));
    idade  = int(input('Informe sua idade :'));
    cpf    = str(input('Informe seu CPF   :'));
    Pessoa = Pessoa(nome, idade, cpf);

    qtd    = int(input('Informe uma quantidade de telefones que deseja inserir :'));

    for i in range(qtd):

        os.system('cls');
        numero   = str(input('Informe seu número :'));  

        listaTelefones.append(Telefone(numero));

    os.system('cls');
    print('\n-----------------------Minhas Informações-----------------------\n');

    print('\nNome :', Pessoa.getNome());
    print('\nNúmeros de telefones inseridos :');

    Pessoa.setTelefones(listaTelefones);
    
    for telefone in Pessoa.getTelefones():
        
        print(telefone.getNumeroTelefone());
