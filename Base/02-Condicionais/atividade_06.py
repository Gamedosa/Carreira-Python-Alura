'''
Docstring for Base.02-Condicionais.atividade_06
Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar. 
Para isso, ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. 
Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado.
'''

def verificar_acesso():
    hora_atual = int(input('Informe a hora atual (formato 24 horas): \n'))

    if (8 <= hora_atual < 18):
        print("Acesso permitido.")
    else:
        print("Acesso negado.") 
    
teste = verificar_acesso()