#Composição
from classes import Cliente, Endereco;

cliente01 = Cliente('Luiz', 32);
cliente01.inserir_endereco('Lins', 'SP');
print(cliente01.nome);
cliente01.lista_enderecos();
print();

cliente02 = Cliente('Lucas', 20);
cliente02.inserir_endereco('Belo Horizonte', 'MG');
cliente02.inserir_endereco('Rio de Janeiro', 'RJ');
print(cliente02.nome);
cliente02.lista_enderecos();
print();

cliente03 = Cliente('João', 20);
cliente03.inserir_endereco('São Paulo', 'SP');
print(cliente03.nome);
cliente03.lista_enderecos();
print();

print('###############################S');
