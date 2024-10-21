import os
import time
from controller.app import App
from util.inputs import Inputs

class Menu:
    def __init__(self):
        self.app = App()
        self.inpt = Inputs()

    def exibirMenu(self):
        op = -1

        while op != 0:
            os.system('cls')

            print("===== MENU PRINCIPAL =====")
            print("Escolha uma opção: ")
            print("1. Resumo das conversas")
            print("2. Histórico de um remetente")
            print("3. Gráfico de histórico dos remetentes")
            print("4. Gráfico de pizza")
            print("5. Gráfico de linhas")
            print("0. Sair")
            
            op = self.inpt.input("Digite: ", 0, 5)

            os.system('cls')

            if op == 1:
                while op == 1:
                    print("===== RESUMO DAS CONVERSAS =====")

                    self.app.conversationsSummary()

                    print("Deseja voltar ao menu principal: ")
                    print("1. Não")
                    print("2. Sim")

                    op = self.inpt.input("Digite: ", 1, 2)

                    os.system('cls')
                
            elif op == 2:
                while op == 2:
                    print("===== HISTÓRICO DE UM REMETENTE =====")

                    print("Deseja ver a lista de remetentes antes?")
                    print("1. Sim")
                    print("2. Não")
                    
                    op = self.inpt.input("Digite: ", 1, 2)

                    os.system('cls')

                    if op == 1:
                        print("===== LISTA DE REMETENTES =====")

                        self.app.printSendersList()

                    sender = input("Digite o nome do remetente que deseja buscar o histórico: ")

                    if self.app.searchSender(sender):
                        os.system('cls')

                        print(f"===== HISTÓRICO DE {sender} =====")

                        self.app.sendersHistory(sender)

                        print("Deseja voltar ao menu principal: ")
                        print("1. Sim")
                        print("2. Não")

                        op = self.inpt.input("Digite: ", 1, 2)

                        os.system('cls')
                    else:
                        print ("ERRO: Nome inválido!")
                    
            elif op == 3:
                print("===== GRÁFICO DE HISTÓRICO DOS REMETENTES =====")

                print("Mostrando gráfico...")

                self.app.sendersHistograms()
                
            elif op == 4:
                print("===== GRÁFICO DE PIZZA =====")

                print("Mostrando gráfico...")

                self.app.sendersPieGraph()
                
            elif op == 5:
                print("===== GRÁFICO DE LINHAS =====")

                print("Mostrando gráfico...")

                self.app.sendersLineGraph()
                
            elif op == 0:
                print("Saindo do programa...")        
                break

            else:
                print("ERRO: Valor inválido!!!")

            time.sleep(2)