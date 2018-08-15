# como a raiz de n e aproximadamente 780000
divisores = []
i = 0
n = 600851475143
print "esses sao os divisores de n"
for d in range (1,780000):
    if (n % d == 0):
        divisores.append(d)
print divisores
for a in divisores:
    for x in range (1,(a+1)/2):
        if (a%x == 0):
            print a
#Os numeros mostrados unicamente na tela sao os fatores primos e,no caso,o maior
#eh o 6857
