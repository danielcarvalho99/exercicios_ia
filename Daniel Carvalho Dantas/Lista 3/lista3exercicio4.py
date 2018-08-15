print "PEDRA.PAPEL E TESOURA"
possibilidades = ['pedra','papel','tesoura']
valido = 1
while (valido):
    jogador1 = raw_input("escolha sua jogada,p1: ")
    jogador2 = raw_input("escolha sua jogada,p2: ")
    if((jogador1 or jogador2) not in possibilidades):
        print "jogada invalida"
        break
    if (jogador1 == "pedra"):

        if(jogador2 == "pedra"):
            print "empate"
        elif(jogador2 == "papel"):
            print "jogador2 ganhou"
        elif(jogador2 == "tesoura"):
            print "jogador1 ganhou"
    if (jogador1 == "papel"):
        if(jogador2 == "pedra"):
            print "jogador1 ganhou"
        elif(jogador2 == "papel"):
            print "empate"
        elif(jogador2 == "tesoura"):
            print "jogador2 ganhou"
    if (jogador1 == "tesoura"):
        if(jogador2 == "pedra"):
            print "jogador2 ganhou"
        elif(jogador2 == "papel"):
            print "jogador1 ganhou"
        elif(jogador2 == "tesoura"):
            print "empate"
    resposta = raw_input("voce quer um novo jogo: ")
    if (resposta == "sim"):
        valido = 1
    if (resposta == "nao"):
        valido = 0
        print "FIM DE JOGO"
