def menu() :
    print("\n\n\t\t\t>>> MENU PRINCIPAL <<<\n\n");
    print('(1) - Adição\n');
    print('(2) - Subtração\n');
    print('(3) - Multiplicação\n');
    print('(4) - Divisão\n');
    print("\n\t\t\t>>> ------ X ------ <<<\n");


def operacao(n1, n2, op) :

    if (op == 1):
        return print('Adição = ', n1 + n2);

    elif (op == 2):
        return print('Subtração = ', n1 - n2);

    elif (op == 3):
        return print('Multiplicação = ', n1 * n2);

    elif (op == 4):
        return print('Divisão = ', n1 / n2);

    else:
        return print('Erro : informe uma opção válida');

def main() :

  import os;

  n1 = float(input('Informe o 1° número : '));
  n2 = float(input('Informe o 2° número : '));
  os.system('cls');

  menu();
  op = int(input('Informe uma opção : '));
  os.system('cls');
  operacao(n1, n2, op);

main();