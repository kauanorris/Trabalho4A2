import pandas as pd
import re
import matplotlib.pyplot as plt

df = pd.DataFrame

with open("Conversa do WhatsApp com Cineminha.txt", "r", encoding="utf-8") as arquivo:
    for texto in arquivo:
        # datas = (re.search(r'^\d+-\d+-\d+?', texto))
        datas = (re.search(r'^.\s?', texto))
        print (datas.group())

"""
def main():
    op = -1
    print(" Análise de Dados de conversas do Whatsapp ")
    while op != 0:
        print("===== MENU PRINCIPAL =====")
        print("Escolha uma opção: ")
        print("1. Resumo das conversas")
        print("2. Histórico de um remetente")
        print("3. Gráfico de histórico de um remetente")
        print("4. Gráfico de pizza")
        print("5. Gráfico de linhas")
        print("0. Sair")
        
        op = int(input("Digite: "))
        
        if op == 1:
            resumo_conversas()
            
        elif op == 2:
            historico_remetente()
            
        elif op == 3:
            grafico_historico()
            
        elif op == 4:
            grafico_pizza()
            
        elif op == 5:
            grafico_linhas()
            
        elif op == 0:
            print("Saindo do programa...")        
            break

        else:
            print("ERRO: Valor inválido!!!")
            
"""