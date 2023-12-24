import os

def iniciar_app():
    print('-----------------------')
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ')
    print('-----------------------\n')


def menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def sair_app():
    os.system('cls')
    print('Saindo...\n')


def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    print(f'Você escolheu a opção {opcao_escolhida}')

    if opcao_escolhida == 1:
        print('Cadastrar restaurante\n')
    elif opcao_escolhida == 2:
        print('Listar restaurantes\n')
    elif opcao_escolhida == 3:
        print('Ativar restaurante\n')
    else:
        sair_app()

def main():
    iniciar_app()
    menu()
    escolher_opcao()
    
if __name__ == '__main__':
    main()