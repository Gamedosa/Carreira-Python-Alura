# Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.


numeros = [1,2,3,'a',5,6,7,8,9,10]
soma = 0
try:
    for numero in numeros:
        soma += numero
    
    print(f'A soma dos numeros da lista é: {soma}\n')

except:
    numero != int
    print(f'Caracter ({numero}) é inválido')
    
