import os
import time
from controller.controller import Controller
from util.inputPlus import inputPlus

class Menu:
    def __init__(self):
        self.controller = Controller()

    def exibirMenu(self):
        op = -1

        while op:
            os.system('cls')

            print("===== MENU PRINCIPAL =====")
            print("Escolha uma opção: ")
            print("1. Exibir Resumo das conversas")
            print("2. Exibir Histórico de um remetente")
            print("3. Exibir Gráfico de histórico dos remetentes")
            print("4. Exibir Gráfico de pizza")
            print("5. Exibir Gráfico de linhas")
            print("6. Exibir Exportar conversas para CSV")
            print("0. Sair")
            
            op = inputPlus("Digite: ", 0, 6)

            os.system('cls')

            if op == 1:
                while op:
                    print("===== RESUMO DAS CONVERSAS =====")

                    self.controller.conversationsSummary()

                    print("Deseja voltar ao menu principal: ")
                    print("0. Sim")
                    print("1. Não")

                    op = inputPlus("Digite: ", 0, 1)

                    os.system('cls')

                print("Voltando ao menu principal...")

                op = 1
                
            elif op == 2:
                while op:
                    print("===== HISTÓRICO DE UM REMETENTE =====")

                    print("Deseja ver a lista de remetentes antes?")
                    print("0. Sim")
                    print("1. Não")
                    
                    op = inputPlus("Digite: ", 0, 1)

                    os.system('cls')

                    if op == 1:
                        print("===== LISTA DE REMETENTES =====")

                        self.controller.printSendersList()

                    sender = input("Digite o nome do remetente que deseja buscar o histórico: ")

                    if self.controller.searchSender(sender):
                        os.system('cls')

                        print(f"===== HISTÓRICO DE {sender} =====")

                        self.controller.sendersHistory(sender)

                        print("Deseja voltar ao menu principal: ")
                        print("0. Sim")
                        print("1. Não")

                        op = inputPlus("Digite: ", 0, 1)

                        os.system('cls')
                    else:
                        print ("ERRO: Nome inválido!")

                print("Voltando ao menu principal...")

                op = 2
                    
            elif op == 3:
                print("===== GRÁFICO DE HISTÓRICO DOS REMETENTES =====")

                print("Mostrando gráfico...")

                self.controller.sendersHistograms()
                
            elif op == 4:
                print("===== GRÁFICO DE PIZZA =====")

                print("Mostrando gráfico...")

                self.controller.sendersPieGraph()
                
            elif op == 5:
                print("===== GRÁFICO DE LINHAS =====")

                print("Mostrando gráfico...")

                self.controller.sendersLineGraph()

            elif op == 6:
                print("===== EXPORTAR CONVERSAS PARA CSV =====")

                print("Exportando dados para CSV...")

                self.controller.exportCsv()
                
            else:
                print("Saindo do programa...")        
                break

            time.sleep(2)