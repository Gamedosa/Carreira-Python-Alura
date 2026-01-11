#Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

numeros = [1,2,3,4,5,6,7,8,9,10]
soma = 0 
for numero in range(1,11,2):
    soma += numero

print(soma)