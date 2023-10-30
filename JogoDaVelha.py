from tkinter import *
from tkinter import messagebox
from datetime import datetime

#VARIÁVEIS GLOBAIS
cor1 = "#3b119c" #roxo azulado
cor2 = "#11669c" #azul escuro
cor3 = "#2d9906" #verde
cor4 = "#0f0f0f" #cinza
cor5 = "#faf8f7" #branco
cor6 = "#b00d02" #vermelho
cor7 = "#02dded" #azul claro
cor8 = "#b6ed02" #verde limão

#Variáveis necessárias

# Variavel Mestre
matrizjogo = [[" "," "," "],[" "," "," "],[" "," "," "]]
# jv - jogador da vez - se true jogador1 se false jogador2
jv = True
# recebe X ou O
jogando = ""
# cotador de pontos jogador1
contjo1 = 0
#contador de pontos do jogador2
contjo2 = 0
#analisa se o jogo deu velha
con = 0
# Variavel para organizar a data e a hora no while
comand = 1

# FUNÇÃO PARA MOSTRAR O JOGO COMPLETO
def MostrarJogo():
    #Variáveis para botão e para salvar os pontos
    pontosjo1 = StringVar()
    pontosjo2 = StringVar()
    
    #Verificar se há algum erro nos nomes
    if jo1.get() == "" or jo2.get() == "" or jo1.get() == jo2.get():
        messagebox.showerror(title="Impossível continuar", message="Algum dos jogadores não escreveu um nome ou os dois nomes são iguais, por favor, tente novamente!")
    else:
        #Definir os botôes globais para usar na função Reiniciar
        global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
        
        global comand
        
        #Função para reiniciar todos os botões
        def Reiniciar():
            global vez, vez2, vez3, vez4, vez5, vez6, vez7, vez8, vez9
            global matrizjogo, jv
            
            
            #Apagar o botão e a mensagem de ganhador
            fr_jogo.winfo_children()[-1].destroy()
            fr_jogo.winfo_children()[9].destroy()
            
            #Reiniciar o valor de cada botão no game
            vez.set(" ")
            vez2.set(" ")
            vez3.set(" ")
            vez4.set(" ")
            vez5.set(" ")
            vez6.set(" ")
            vez7.set(" ")
            vez8.set(" ")
            vez9.set(" ")
            
            #Reiniciando matriz
            matrizjogo = [[" "," "," "],[" "," "," "],[" "," "," "]]
            
            #Deixando os botões clicáveis novamente
            btn1['state'] = NORMAL
            btn2['state'] = NORMAL
            btn3['state'] = NORMAL
            btn4['state'] = NORMAL
            btn5['state'] = NORMAL
            btn6['state'] = NORMAL
            btn7['state'] = NORMAL
            btn8['state'] = NORMAL
            btn9['state'] = NORMAL
        
        #Função para definir ganhador ou velha
        def GanhadorPerdedor(btnclicado):
            global matrizjogo
            global jv  
            global jogando  
            global contjo1
            global contjo2  
            global con
            
            #Jogador que está jogando
            if jv == True:
                jogando = "X"
            else:
                jogando = "O"        
            
            #Salvar o X ou o O nos botões clicados e salvar na matriz os valores
            if btnclicado == "btn1":
                if jv == True:
                    vez.set("X")
                    jv = False
                    matrizjogo[0][0] = "X"
                else:
                    vez.set("O")
                    jv = True
                    matrizjogo[0][0] = "O"
                # O comando abaixo vai impedir o botão que foi clicado, ser clicado novamente    
                btn1['state'] = DISABLED
                  
            elif btnclicado == "btn2":
                if jv == True:
                    vez2.set("X")
                    jv = False
                    matrizjogo[0][1] = "X"
                else:
                    vez2.set("O")
                    jv = True
                    matrizjogo[0][1] = "O"
                btn2['state'] = DISABLED
                
            elif btnclicado == "btn3":
                if jv == True:
                    vez3.set("X")
                    jv = False
                    matrizjogo[0][2] = "X"
                else:
                    vez3.set("O")
                    jv = True
                    matrizjogo[0][2] = "O"
                btn3['state'] = DISABLED
                
            elif btnclicado == "btn4":
                if jv == True:
                    vez4.set("X")
                    jv = False
                    matrizjogo[1][0] = "X"
                else:
                    vez4.set("O")
                    jv = True
                    matrizjogo[1][0] = "O"
                btn4['state'] = DISABLED
                
            elif btnclicado == "btn5":
                if jv == True:
                    vez5.set("X")
                    jv = False
                    matrizjogo[1][1] = "X"
                else:
                    vez5.set("O")
                    jv = True
                    matrizjogo[1][1] = "O"
                btn5['state'] = DISABLED
                
            elif btnclicado == "btn6":
                if jv == True:
                    vez6.set("X")
                    jv = False
                    matrizjogo[1][2] = "X"
                else:
                    vez6.set("O")
                    jv = True
                    matrizjogo[1][2] = "O"
                btn6['state'] = DISABLED
                
            elif btnclicado == "btn7":
                if jv == True:
                    vez7.set("X")
                    jv = False
                    matrizjogo[2][0] = "X"
                else:
                    vez7.set("O")
                    jv = True
                    matrizjogo[2][0] = "O"
                btn7['state'] = DISABLED
                
            elif btnclicado == "btn8":
                if jv == True:
                    vez8.set("X")
                    jv = False
                    matrizjogo[2][1] = "X"
                else:
                    vez8.set("O")
                    jv = True
                    matrizjogo[2][1] = "O"
                btn8['state'] = DISABLED
                
            elif btnclicado == "btn9":
                if jv == True:
                    vez9.set("X")
                    jv = False
                    matrizjogo[2][2] = "X"
                else:
                    vez9.set("O")
                    jv = True
                    matrizjogo[2][2] = "O"
                btn9['state'] = DISABLED
            
            #Verificar se alguém ganhou
            if matrizjogo[0][0] == jogando and matrizjogo[0][1] == jogando and matrizjogo[0][2] == jogando:
                #Se jogador 1 ganhou
                if jv == False:
                    # A variavel jo1 é referente ao primeiro jogador
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo1.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo1 += 1
                    pontosjo1.set(contjo1)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
                #Se jogador 2 ganhou    
                if jv == True:
                    # A variavel jo2 é referente ao segundo jogador
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo2.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo2 += 1
                    pontosjo2.set(contjo2)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
            elif matrizjogo[0][0] == jogando and matrizjogo[0][1] == jogando and matrizjogo[0][2] == jogando:
                if jv == False:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo1.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo1 += 1
                    pontosjo1.set(contjo1)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
                    
                if jv == True:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo2.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo2 += 1
                    pontosjo2.set(contjo2)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
            elif matrizjogo[1][0] == jogando and matrizjogo[1][1] == jogando and matrizjogo[1][2] == jogando:
                if jv == False:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo1.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo1 += 1
                    pontosjo1.set(contjo1)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
                    
                if jv == True:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo2.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo2 += 1
                    pontosjo2.set(contjo2)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
            elif matrizjogo[2][0] == jogando and matrizjogo[2][1] == jogando and matrizjogo[2][2] == jogando:
                if jv == False:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo1.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo1 += 1
                    pontosjo1.set(contjo1)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
                    
                if jv == True:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo2.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo2 += 1
                    pontosjo2.set(contjo2)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
            elif matrizjogo[0][1] == jogando and matrizjogo[1][1] == jogando and matrizjogo[2][1] == jogando:
                if jv == False:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo1.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo1 += 1
                    pontosjo1.set(contjo1)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
                    
                if jv == True:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo2.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo2 += 1
                    pontosjo2.set(contjo2)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
            elif matrizjogo[0][0] == jogando and matrizjogo[1][0] == jogando and matrizjogo[2][0] == jogando:
                if jv == False:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo1.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo1 += 1
                    pontosjo1.set(contjo1)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
                    
                if jv == True:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo2.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo2 += 1
                    pontosjo2.set(contjo2)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
            elif matrizjogo[0][2] == jogando and matrizjogo[1][2] == jogando and matrizjogo[2][2] == jogando:
                if jv == False:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo1.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo1 += 1
                    pontosjo1.set(contjo1)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
                    
                if jv == True:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo2.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo2 += 1
                    pontosjo2.set(contjo2)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
            elif matrizjogo[0][0] == jogando and matrizjogo[1][1] == jogando and matrizjogo[2][2] == jogando:
                if jv == False:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo1.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo1 += 1
                    pontosjo1.set(contjo1)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
                    
                if jv == True:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo2.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo2 += 1
                    pontosjo2.set(contjo2)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
            elif matrizjogo[0][2] == jogando and matrizjogo[1][1] == jogando and matrizjogo[2][0] == jogando:
                if jv == False:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo1.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo1 += 1
                    pontosjo1.set(contjo1)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
                    
                if jv == True:
                    vencedor = Label(fr_jogo, text=(f"Parabéns {jo2.get()}, você venceu!!"), bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    contjo2 += 1
                    pontosjo2.set(contjo2)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                    
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
            #Se der velha o jogo       
            else:
                for l in range(3):
                    for c in range(3):
                        if matrizjogo[l][c] == "X" or matrizjogo[l][c] == "O":
                            con += 1
                if con != 9:
                    con = 0
                else:                    
                    vencedor = Label(fr_jogo, text="Jogadores ruins, ninguém ganhou hahaha!!", bg=cor4, fg=cor5, font=("Arial 10 bold italic"))
                    vencedor.place(x=50, y=295, width=300, height=30)
                    jono = Button(fr_jogo, text="Jogar Novamente", bg=cor7, fg=cor4, relief=SOLID,borderwidth=0, font=("Arial 10 bold italic"), command=Reiniciar)
                    jono.place(x=140,y=340,width=120,height=30)
                        
                    btn1['state'] = DISABLED
                    btn2['state'] = DISABLED
                    btn3['state'] = DISABLED
                    btn4['state'] = DISABLED
                    btn5['state'] = DISABLED
                    btn6['state'] = DISABLED
                    btn7['state'] = DISABLED
                    btn8['state'] = DISABLED
                    btn9['state'] = DISABLED
                    
            
        jogo.geometry("400x450")   
        
        messagebox.showinfo(title="Informações Necessárias", message=(f"O jogador {jo1.get()} fica com o X e ele começa a partida. O jogador {jo2.get()} fica com o O."))             
        
        comand = 2
          
        #Frame dos pontos
        fr_pontos = Frame(jogo, borderwidth=0, bg=cor4,relief=SOLID)
        fr_pontos.place(x=0, y=0, width=500, height=50)
        
        #Nome dos nomes dos jogadores e pontos
        nome_jo1 = Label(fr_pontos, text=jo1.get(), font=("Arial 15 bold italic"), bg=cor8, fg=cor2)
        nome_jo1.place(x=0, y=0, width=150, height=50)
        
        nome_jo2 = Label(fr_pontos, text=jo2.get(), font=("Arial 15 bold italic"), bg=cor8, fg=cor2)
        nome_jo2.place(x=400, y=25, width=150, height=50, anchor=E)
        
        pon_jo1 = Label(fr_pontos, textvariable=pontosjo1, bg=cor4, fg=cor3, font=("Arial 30 bold"))
        pon_jo1.place(x=150, y=0, width=50, height=50)
        pontosjo1.set("0")
        
        pon_jo2 = Label(fr_pontos, textvariable=pontosjo2, bg=cor4, fg=cor6, font=("Arial 30 bold"))
        pon_jo2.place(x=200, y=0, width=50, height=50)
        pontosjo2.set("0")
        
        #Frame do jogo
        fr_jogo = Frame(jogo, borderwidth=0, bg=cor4, relief=SOLID)
        fr_jogo.place(x=0, y=50, width=400, height=400)
        
        #BOTÕES DO JOGO
        
        btn1 = Button(fr_jogo, textvariable=vez, bg=cor5, fg="#000",relief=RAISED, borderwidth=1, font="Arial 15", command=lambda m="btn1":GanhadorPerdedor(m))
        btn1.place(x=80, y=50, width=80, height=80)
        btn2 = Button(fr_jogo, textvariable=vez2, bg=cor5,fg="#000",relief=RAISED, borderwidth=1, font="Arial 15", command=lambda m="btn2":GanhadorPerdedor(m))
        btn2.place(x=160, y=50, width=80, height=80)
        btn3 = Button(fr_jogo, textvariable=vez3, bg=cor5, fg="#000",borderwidth=1, font="Arial 15", command=lambda m="btn3":GanhadorPerdedor(m))
        btn3.place(x=240, y=50, width=80, height=80)
          
        btn4 = Button(fr_jogo, textvariable=vez4, bg=cor5, fg="#000",relief=RAISED, borderwidth=1, font="Arial 15", command=lambda m="btn4":GanhadorPerdedor(m))
        btn4.place(x=80, y=130, width=80, height=80)
        btn5 = Button(fr_jogo, textvariable=vez5, bg=cor5,fg="#000", relief=RAISED, borderwidth=1, font="Arial 15", command=lambda m="btn5":GanhadorPerdedor(m))
        btn5.place(x=160, y=130, width=80, height=80)
        btn6 = Button(fr_jogo, textvariable=vez6, bg=cor5, fg="#000",borderwidth=1, font="Arial 15", command=lambda m="btn6":GanhadorPerdedor(m))
        btn6.place(x=240, y=130, width=80, height=80)
         
        btn7 = Button(fr_jogo, textvariable=vez7, bg=cor5, fg="#000",relief=RAISED, borderwidth=1, font="Arial 15", command=lambda m="btn7":GanhadorPerdedor(m))
        btn7.place(x=80, y=210, width=80, height=80)        
        btn8 = Button(fr_jogo, textvariable=vez8, bg=cor5, fg="#000",relief=RAISED, borderwidth=1, font="Arial 15", command=lambda m="btn8":GanhadorPerdedor(m))
        btn8.place(x=160, y=210, width=80, height=80)
        btn9 = Button(fr_jogo, textvariable=vez9, bg=cor5, fg="#000", borderwidth=1, font="Arial 15", command=lambda m="btn9":GanhadorPerdedor(m))
        btn9.place(x=240, y=210, width=80, height=80)   
        
'CORPO PRINCIPAL'

# Criando Janela
jogo = Tk()
jogo.title("Jogo da Velha")
jogo.configure(bg=cor4)
# Deixa a janela impossivel de maximizar e diminuir o seu tamanho
jogo.resizable(False, False)
# Centralizar janela do game
largura = 500
altura = 500
largura_screen = jogo.winfo_screenwidth()
altura_screen = jogo.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - largura/2
jogo.geometry('%dx%d+%d+%d' %(largura,altura,posx,posy))

#Variáveis para mostrar ou X ou O no jogo quando clicado um botao na funcao MostrarJogo()
vez = StringVar()
vez2 = StringVar()
vez3 = StringVar()
vez4 = StringVar()
vez5 = StringVar()
vez6 = StringVar()
vez7 = StringVar()
vez8 = StringVar()
vez9 = StringVar()         

#PARTE QUE PEDE O NOME DOS JOGADORES

#Nome maior que aparece na janela
velha = Label(jogo, text="Jogo da Velha", font=("Arial 30 italic bold"), bg=cor4, fg=cor7)
velha.place(x=113, y=50, width=280, height=50)

jo1 = StringVar() #jogador 1
jo2 = StringVar() #jogador 2

#Nome jogador 1
j1 = Label(jogo, text="Nome do Jogador 1", font=("Arial 15 italic bold"), bg=cor4, fg=cor7)
j1.place(x=120, y=150, width=250, height=25)
nm_j1 = Entry(jogo, textvariable=jo1)
nm_j1.insert(0, "Jogador 1")
nm_j1.place(x=170, y=180, width=150, height=20)

#Nome jogador 2
j2 = Label(jogo, text="Nome do Jogador 2", font=("Arial 15 italic bold"), bg=cor4, fg=cor7)
j2.place(x=120, y=230, width=250, height=25)
nm_j2 = Entry(jogo, textvariable=jo2)
nm_j2.insert(0, "Jogador 2")
nm_j2.place(x=170, y=260, width=150, height=20)

#Botão Iniciar Jogo
btn = Button(jogo, text="Iniciar Jogo", bg=cor3, fg=cor5, font=("Arial 20 italic bold"), command=MostrarJogo, relief=SOLID, borderwidth=0)
#relief (flat, raised, sunken, solid)
btn.place(x=140, y=330, width=210, height=50)

#Mostrar Hora, Data e Nome do Criador
while comand < 2:
    #Hora
    hora = Label(jogo, text=f"Hora: {datetime.now(): %H:%M:%S}", bg=cor4, fg=cor5)
    hora.update()
    hora.place(x=20, y=470)
    #Data
    data = Label(jogo, text=f"Data: {datetime.now(): %d/%m/%Y}", bg=cor4, fg=cor5)
    data.update()
    data.place(x=120, y=470)
    #Criador
    criado = Label(jogo, text="By: José Fernando e Jhonnata Virginio", bg=cor4, fg=cor5)
    criado.place(x=235, y=470)

    
jogo.mainloop()