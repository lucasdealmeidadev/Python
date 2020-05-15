from classes import Autor, Livro;

livro01 = Livro('Rasmus Lerdorf', 1, 'PHP POO');

print('\n-------------------AUTOR-------------------\n');
print('Id do autor     = ',livro01.getIdAutor());
print('Nome do autor   = ',livro01.getAutor());

print('\n-------------------LIVRO-------------------\n');
print('Id do livro     = ',livro01.getId());
print('Nome do carro   = ',livro01.getNome());