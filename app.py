import os

restaurantes = ['Shushi Takakara Nomuro', 'Pizza da Mamma']

def iniciar_app():
    print('-----------------------')
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ')
    print('-----------------------\n')


def menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def return_to_menu():
    input('\nDigite qualquer tecla para retornar ao menu principal: \n')
    main()


def sair_app():
    exibir_subtitulo('Saindo...')


def opcao_invalida():
    print('Opção inválida!\n')
    return_to_menu()


def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()


def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    
    return_to_menu()


def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    
    return_to_menu()


def ativar_restaurante():
    exibir_subtitulo('Ativando restaurante')
    
    return_to_menu()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            sair_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()    


def main():
    os.system('cls')
    iniciar_app()
    menu()
    escolher_opcao()
    

if __name__ == '__main__':
    main()