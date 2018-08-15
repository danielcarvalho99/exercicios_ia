A = "A.M"
P = "P.M."
horas = 0
minutos = 0
while (1):
    horas = int(raw_input("informe as horas: "))
    minutos = int(raw_input("informe os minutos: "))
    if (horas >= 24 or horas <0 or minutos<0 or minutos >59):
        print "horario invalido"
        break
    if (horas > 12):
        print ("o horario e {}:{} {}".format(horas-12,minutos,P))
    else:
        print ("o horario e {}:{} {}".format(horas,minutos,A))
