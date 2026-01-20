'''
Docstring for Base.02-Condicionais.atividade_03
Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. 
Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.
'''


def alertar_temperatura(temperatura) -> float: 
    # temperatura = float(input('Informe a temperatura atual da sala de Servidores: \n'))
    limite =25
    if (temperatura > limite):
        print(f'Alerta!!! A temperatura da sala está em {temperatura}° Graus \n')
    else:
        print(f'A temperatura está em {temperatura}. O limite é {limite} ')
teste = alertar_temperatura(20)

