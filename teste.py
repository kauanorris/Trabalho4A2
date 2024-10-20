import pandas as pd
import re
import matplotlib.pyplot as plt
import os
from datetime import datetime

conversationsDf = pd.DataFrame({
    'date':[],
    'hour':[],
    'sender':[],
    'message':[]
})

os.system('cls')

with open("Conversa do WhatsApp com Cineminha.txt", "r", encoding="utf-8") as a:
    for txt in a:
        informations = re.findall (r"(\d{2}/\d{2}/\d{4}) (\d{2}:\d{2}) - ([^:]+): (.+)", txt)
        
        for i in informations:
            date, hour, sender, message = i

            newConversation = {
                'date':datetime.strptime(date, '%d/%m/%Y'),
                'hour':datetime.strptime(hour, '%H:%M').time(),
                'sender':sender,
                'message':message
            }        

            conversationsDf = conversationsDf._append(newConversation, ignore_index = True)
            conversationsDf = conversationsDf.reset_index(drop = True)

    qttyConversationsBySender = pd.DataFrame({
        'sender':[],
        'qttyConversations':[]
    })

    senders = conversationsDf['sender'].unique().tolist()

    for sender in senders:
        qttyConversations = len(conversationsDf.loc[conversationsDf['sender'] == sender])

        qttyConversationsBySender = qttyConversationsBySender._append({
            'sender':sender,
            'qttyConversations':qttyConversations
        }, ignore_index = True)
        qttyConversationsBySender = qttyConversationsBySender.reset_index(drop = True) 
    
    qttyConversationsBySender = qttyConversationsBySender.sort_values('qttyConversations', ascending=False)

    allConversationsBySender = conversationsDf.loc[conversationsDf['sender'] == 'Nathan']

    allYears = {y for y in conversationsDf['date'].dt.year}
    
    qttyConversationsBySenderByYear = 
    print (allYears)
"""
def main():
    op = -1
    print(" Análise de Dados de conversations do Whatsapp ")
    while op != 0:
        print("===== MENU PRINCIPAL =====")
        print("Escolha uma opção: ")
        print("1. Resumo das conversations")
        print("2. Histórico de um sender")
        print("3. Gráfico de histórico de um sender")
        print("4. Gráfico de pizza")
        print("5. Gráfico de linhas")
        print("0. Sair")
        
        op = int(input("Digite: "))
        
        if op == 1:
            resumo_conversations()
            
        elif op == 2:
            historico_sender()
            
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