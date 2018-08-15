qsoma = 0
somaq = 0
soma = 0
for n in range (1,101):
    somaq = somaq + n**2
print somaq
for n in range (1,101):
    soma = soma + n
qsoma = soma**2
print qsoma
diferenca = somaq - qsoma
print ("a diferenca e {}".format(diferenca))
