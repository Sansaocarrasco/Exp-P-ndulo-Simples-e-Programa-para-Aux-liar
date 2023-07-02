import math
import matplotlib.pyplot as plt
import numpy as np

print ("\n\n--------------------Seja BEM VINDO ao Ambiente Auxiliar de experimentos de Pêndulo Simples!--------------------\n")
print ("\n O Ambiente Auxiliar possui algumas funcionalidades, que podem ser escolhidas ao digitar o número referente a opção desejada no MENU abaixo\n")
#Sub-Funções
def calculo_Periodo(int):
    #definindo as constantes
    #encontraremos o período ideal para o comprimento do fio em questão
    g = 9.8
    print ("\nVocê escolheu a opção de Cálculo de Período\n")
    print ("Trabalhando com o valor de g= 9.8\nDigite o comprimento do fio (em cm): ")

    l = float(input())

    #convertendo o tamanho do fio de centímetros para metros
    l = l/100

    #Referente a (Equação 4) trabalhada no relatório
    T = 2 * np.pi * np.sqrt(l/g)

    print ("O Período real para o comprimento de fio {} (m) é" .format(l))

    print ("%.3f (s)" % T )

    #voltando para ao menu
    print ("\nVoltando para o MENU...")
    Menu(int)
def calculo_Gravidade(int):
    print ("\nVocê escolheu a opção de Cálculo de Gravidade Local\n")
    print ("Digite os valores dos períodos em (s):")
    t1, t2, t3, t4, t5 = input().split()
    t1 = float(t1)
    t2 = float(t2)
    t3 = float(t3)
    t4 = float(t4)
    t5 = float(t5)

    print ("\nTrabalharemos com o período médio dos dados apresentados\n")
    #calculando o tempo médio
    t_medio = (t1+t2+t3+t4+t5)/5

    print ("Digite o valor do tamanho do fio (l) em cm:")
    l = float(input())
    # convertendo de cm para metros
    l = l/100

    #Encontrando a gravidade local
    #Utilizando a (Equação 5), referenciada no relatório, será obtida a aceleração da gravidade

    g = (4 * math.pow((np.pi),2) * l)/math.pow((t_medio),2)
    print ("\nPara um Periodo médio de {}(s) e um tamanho de fio de {}(m) teremos o seguinte valor de gravidade:".format(t_medio,l))
    print ("%.3f m/s²" % g)

    #Encontrando o erro relativo
    #Utilizando a (Equação 9), referenciada no relatório, será obtido o erro relativo do experimento.

    Er = ((g - 9.8)/9.8) * 100
    Er = abs(Er)
    print ("O erro relativo do experimento em questão é de: %.3f%%" % Er )

    #voltando par ao menu
    print ("\nVoltando para o MENU...")
    Menu(int)

#Funções bases
def realizar_calculo(x):
    print ("Para a opção escolhida, teremos as seguintes sub-opções:")
    print("(0) Voltar para o menu\n(1) Cálculo de Período\n(2) Cálculo da Gravidade local\n")
    x = int(input())
    if x == 1:
        calculo_Periodo(x)
    elif x == 2:
        calculo_Gravidade(x)
    else:
        Menu(x)
def grafico_pendulo(x):
    print ("Digite o valor do comprimento do fio (em cm)")
    L = float(input())
    # convertendo de centimetros para metros
    L = L/100 

    print ("Digite o valor da aceleração da gravidade")
    g = float(input()) # aceleração da gravidade (m/s^2)

    # Utilizando a (Equação 8), referênciada no relatório, realiza-se o cálculo do ângulo em função do tempo 
    def Movimento_pendulo(t, theta0):
        
        theta = theta0 * np.cos(np.sqrt(g/L) * t)  
        return theta

    # Definir valores do tempo
    t = np.linspace(0, 10, 1000)

    # Definir ângulo inicial do pêndulo
    print ("Digite o angulo inicial (em graus): ")
    theta0 = float(input())

    #convertendo para radianos
    theta0 = np.radians(theta0)

    # Calcular movimento do pêndulo
    theta = Movimento_pendulo(t, theta0)

    t = np.linspace(0, 10, 1000)
    s = theta

    # Escolhendo as cores dos parametros do gráfico
    fig, ax = plt.subplots(facecolor=(.13, .31, .31))
   
    ax.set_facecolor('0.8')
    
    ax.set_title('Gráfico do Movimento de um Pêndulo Simples (MHS)', color='white', size= 20)
   
    ax.set_xlabel('Tempo [s]', color='white', size= 16)
    
    ax.set_ylabel('Ângulo [rad]', color='white', size= 16)
    
    ax.tick_params(labelcolor='#d3d3d3', size= 14)

    plt.plot(t,s, marker='x')
    plt.show()

    #voltando par ao menu
    print ("\nVoltando para o MENU...")
    Menu(int)
def Menu(x):
    print ("\n-MENU-\n")
    print ("Digite sua intenção: ")
    print("(0) Para sair\n(1) Para realizar cálculos\n(2) Para o gráfico do movimento harmônico \n")

    x = int(input())
    if x == 1:
        print ("\nVocê escolheu a opção de realizar calculos\n")
        realizar_calculo(int)
    elif x == 2:
        print ("\nVocê escolheu a opção do Gráfico do Movimento Harmônico Simples\n")
        grafico_pendulo(int)
    else:
        print ("\n\n....................OBRIGADO POR UTILIZAR O NOSSO AMBIENTE....................\n")
        print ("--------------------FINALIZANDO O PROGRAMA--------------------\n\n")
        exit()

# Chamando a função principal
Menu(int)