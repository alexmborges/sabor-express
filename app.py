import os

restaurantes = [{'nome': 'Takakara Nomuro', 'categoria': 'Japa', 'ativo': False},
                {'nome': 'Pizza da Mamma', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Churrascolândia', 'categoria': 'Churrascaria', 'ativo': False}]

def iniciar_app():
    '''Exibe o nome estilizado do app'''
    print('-------------------------')
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ')
    print('-------------------------\n')


def menu():
    '''Exibe o menu com as funções disponíveis do app'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar status restaurante')
    print('4. Sair\n')


def return_to_menu():
    '''Usada ao final de cada operação para retornar ao menu principal
    Outputs: 
    - Retorna ao menu principal
    '''
    input('\nDigite qualquer tecla para retornar ao menu principal: \n')
    main()


def sair_app():
    '''Encerra o app'''
    exibir_subtitulo('Saindo...')


def opcao_invalida():
    '''Exibe a mensagem de opção inválida e retorna ao menu principal
    Outputs: 
    - Retorna ao menu principal
    '''
    print('Opção inválida!\n')
    return_to_menu()


def exibir_subtitulo(texto):
    '''Exibe um subtítulo padrão para cada operação
    Inputs:
    - texto: str - o texto do subtítulo
    '''
    os.system('cls')
    linha = '-' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


# Definições das opções:


def cadastrar_restaurante():
    '''Essa função permite cadastrar novos restaurantes
    Inputs:
    - Nome do restaurante
    - Categoria
    
    OUtputs:
    - Add um nome de restaurante e sua categoria a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurantes = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurantes)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    
    return_to_menu()


def listar_restaurantes():
    '''Lista os restaurantes cadastrados
    Outputs:
    - Exibe na tela a lista de restaurantes
    '''
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(22)} | {'Status'}') 
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    return_to_menu()


def alterar_ativo_restaurante():
    '''Alterna o status do restaurante ente ativ0/inativo
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alterando o estado ativo/inativo do restaurante')
    nome_restaurante = input('Digite o nome do restalrante que você deseja alterar o ativo: ')
    restaurante_encontrado = False # Pelo padrão que definimos todos inicial como False ou inativo
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] # O 'not' alterna o valor True/False para seu oposto
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    
    return_to_menu()


def escolher_opcao():
    '''Solicita e executa a opção do usuário
    Outputs:
    - Executa a opção escolhida
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_ativo_restaurante()
        elif opcao_escolhida == 4:
            sair_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()    


def main():
    '''Função principal que executa o programa'''
    os.system('cls')
    iniciar_app()
    menu()
    escolher_opcao()
    

if __name__ == '__main__':
    main()