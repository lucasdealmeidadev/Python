from pessoaFisica   import PessoaFisica;
from pessoaJuridica import PessoaJuridica;

pessoaFisica   = PessoaFisica('Lucas de Almeida',   20, '932.488.490-53');
pessoaJuridica = PessoaJuridica('Lucas de Almeida', 21, '96.273.389/0001-18');

print('\nNome :', pessoaFisica.nome, 'Idade :', pessoaFisica.idade, 'CPF :', pessoaFisica.cpf);
print('Nome :', pessoaJuridica.nome, 'Idade :', pessoaJuridica.idade, 'CPF :', pessoaJuridica.cnpj, '\n');