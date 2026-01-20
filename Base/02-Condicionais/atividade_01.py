'''
Docstring for Base.02-Condicionais.atividade_01

Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. 
Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. 
Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.
'''

def quantidade_vendida():
    banana = int(input('Informe a quantidade de bananas vendidas: \n'))

    maca =   int(input('Informe a quantidade de maçãs vendidas: \n'))

    if (maca > banana):
        print(f'As maças tiveram mais vendas: {maca}\n')
    elif (banana > maca):
        print(f'As bananas tiveram mais vendas: {banana}\n')
    elif (banana == maca):
        print(f'As quantidade de maçã e bananas foram iguais.')

teste = quantidade_vendida()
