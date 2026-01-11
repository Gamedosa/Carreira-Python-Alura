# Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

# numeros = [1,2,3,4,5,6,7,8,9,10]
numeros = []

try:
    soma = 0
    for valor in numeros:
        soma += valor

    media = soma / len(numeros)
    print(f'A média da lista é {media}')

except ZeroDivisionError:
    print('Lista vazia')
