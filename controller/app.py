import pandas as pd
import matplotlib.pyplot as plt
from util.readData import ReadData

class App:
    def __init__(self):
        readData = ReadData()

        self.conversationsDf = readData.readData()

        self.senders = self.conversationsDf['sender'].unique().tolist()
        self.conversationsBySender = self.conversationsDf.groupby(["sender"]).size().reset_index(name="qtty")
        self.conversationsByDate = self.conversationsDf.groupby(["date", "sender"]).size().reset_index(name="qtty")

    def conversationsSummary (self):
        print (self.conversationsBySender.sort_values(by=['qtty']))

    def printSendersList(self):
        i = 0

        for sender in self.senders:
            print(f"{i}. {sender}")

            i += 1

    def searchSender (self, sender):
        return sender in self.senders
    
    def sendersHistory (self, sender):
        print(self.conversationsDf.loc[self.conversationsDf['sender'] == sender].reset_index())

    def sendersHistograms (self):
        for sender in self.senders:
            conversationsByDateBySender = self.conversationsByDate[self.conversationsByDate['sender'] == sender]

            plt.figure(figsize=(10, 6))

            plt.hist(conversationsByDateBySender['date'], label=sender)

            plt.title(f'Histograma da qntd. de conversas de {sender}')
            plt.xlabel('Datas')
            plt.ylabel('Quantidade de conversas')
            
            plt.show()
    
    def sendersPieGraph (self):
        plt.figure(figsize=(7, 9))

        plt.pie(self.conversationsBySender['qtty'], labels = self.conversationsBySender['sender'], autopct='%1.1f%%', colors=plt.cm.Paired.colors)

        plt.title("Percentual de Mensagens por Remetente")

        plt.show()

    def sendersLineGraph (self):
        plt.figure(figsize=(10, 6))

        pivot = self.conversationsByDate.pivot(index='date', columns='sender', values='qtty').fillna(0)

        for sender in self.senders:

            plt.plot(pivot.index, pivot[sender], label=sender)

            plt.title('Quantidade de conversas ao longo do tempo (data) por remetente')

            plt.xlabel('Datas')
            plt.ylabel('Quantidade de conversas')

            plt.legend(title="Remetente")

        plt.show()