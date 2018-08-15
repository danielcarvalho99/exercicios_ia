fibant = 0
fibatual = 1
fibpos = 1
soma = 0
while (fibatual < 4000000):
    fibpos = fibatual + fibant
    fibant = fibatual
    fibatual = fibpos

    if (fibant % 2 == 0):
        print fibant
        soma = soma + fibant
print ("a soma e {}".format(soma))
