'''
Docstring for Base.02-Condicionais.atividade_05
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. 
Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. 
O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.
'''

def monitorar_orcamento():
    limite = 3000
    despesa = float(input('Digite o total de despesas do mês (R$): \n'))
    
    if (despesa > limite):
        print('Atenção!!! Você ultrapassou o limite do orçamento')
    else:
        print('Limite não ultrapassado.')
    
teste = monitorar_orcamento()
