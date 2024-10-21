import os
import time
from app import App

class Menu:
    def __init__(self):
        self.app = App()


    def exibirMenu(self):
        op = -1

        while op != 0:
            os.system('cls')

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
                self.app.conversationsSummary()
                
            elif op == 2:
                self.app.sendersHistory("Kauã")
                
            elif op == 3:
                self.app.sendersHistograms()
                
            elif op == 4:
                self.app.sendersPieGraph()
                
            elif op == 5:
                self.app.sendersLineGraph()
                
            elif op == 0:
                print("Saindo do programa...")        
                break

            else:
                print("ERRO: Valor inválido!!!")

            time.sleep(2)