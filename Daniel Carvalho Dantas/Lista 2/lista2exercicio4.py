string1 = raw_input("digite uma string: ")
string2  = raw_input("digite uma outra string: ")
print ("a primeira string e " + string1 + " e tamanho dela e {}".format(len(string1)))
print ("a segunda string e " + string2 + " o tamanho dela e {}".format(len(string2)))
if (len(string1) == len(string2)):
    print ("as duas strings sao do mesmo tamanho")
    if (string1 == string2):
        print "as strings sao iguais"
    else: print "as strings nao sao iguais"
else:
    print ("as duas strings nao sao do mesmo tamanho e nao sao iguais")
