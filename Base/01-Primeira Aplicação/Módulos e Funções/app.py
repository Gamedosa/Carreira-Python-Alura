import os
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

def finalizar_app():
    os.system('cls')
    print('Finalizando app')
def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        print('Cadastrar Restaurante')
    elif opcao_escolhida == 2:
        print('Listar Restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar Restaurante')
    else:
        finalizar_app()

def main():
    exibir_nome_do_progama()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()