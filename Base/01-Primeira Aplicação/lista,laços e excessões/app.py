import os
restaurantes = ['Barnabé', 'Caipirão']
def exibir_nome_do_progama(): 
    print('''
                                                                                                   
  ▄▄▄▄         █                           ▄▄▄▄▄▄                                          
 █▀   ▀  ▄▄▄   █▄▄▄    ▄▄▄    ▄ ▄▄         █      ▄   ▄  ▄▄▄▄    ▄ ▄▄   ▄▄▄    ▄▄▄    ▄▄▄  
 ▀█▄▄▄  ▀   █  █▀ ▀█  █▀ ▀█   █▀  ▀        █▄▄▄▄▄  █▄█   █▀ ▀█   █▀  ▀ █▀  █  █   ▀  █   ▀ 
     ▀█ ▄▀▀▀█  █   █  █   █   █            █       ▄█▄   █   █   █     █▀▀▀▀   ▀▀▀▄   ▀▀▀▄ 
 ▀▄▄▄█▀ ▀▄▄▀█  ██▄█▀  ▀█▄█▀   █            █▄▄▄▄▄ ▄▀ ▀▄  ██▄█▀   █     ▀█▄▄▀  ▀▄▄▄▀  ▀▄▄▄▀ 
                                                         █                                 
                                                         ▀                                 
          ''')

def exibir_opcoes():
    print('1.Cadastrar Restaurante\n')
    print('2.Listar Restaurante\n')
    print('3.Ativar Restaurante\n')
    print('4.Sair\n')

def voltar_ao_menu_principal():
    input('\nAperte uma tecla para voltar ao menu anterior.\n')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def finalizar_app():
    exibir_subtitulo('\n Finalizando Aplicativo')
    
def opcao_invalida():
    print('Opção invalida.\n')
    voltar_ao_menu_principal()

def cadastrar_restaurante():

    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do Restaurante que deseja cadastrar:\n')
    restaurantes.append(nome_restaurante)
    print(f'O Restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurante():
    
    exibir_subtitulo('Listando Restaurantes...')
    
    for restaurante in restaurantes:
        print(f'Resturante {restaurante}')
    
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante')
        elif opcao_escolhida == 4:
            finalizar_app( )
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_progama()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()