'''
Docstring for Base.02-Condicionais.atividade_02
Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: 
A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. 
Se algum valor for negativo, mostre uma mensagem informando o erro.
'''

def calcular_tempo():
    atividade_a = int(input('Informe o tempo da atividade A: \n'))
    atividade_b = int(input('Informe o tempo da atividade B: \n'))
    atividade_c = int(input('Informe o tempo da atividade C: \n'))

    if(atividade_a < 0):
        print(f'Valor informado {atividade_a} é invalido.')
    elif(atividade_b < 0):
        print(f'Valor informado {atividade_b} é invalido.')
    elif(atividade_c < 0):
        print(f'Valor informado {atividade_c} é invalido.')
    
    else:
        total = atividade_a + atividade_b + atividade_c
        print(f'O tempo total para realizar as atividades é de {total} dias. \n')

teste = calcular_tempo()
    