# Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

def calcular_tabuada():
    numero = int(input('Informe um numero para mostrar a tabuada :'))
    for multiplicador in range (11):
        resultado = multiplicador * numero
        print(f'A tabuada de {numero} é: {numero} X {multiplicador} = {resultado}\n')
    

calcular_tabuada()
