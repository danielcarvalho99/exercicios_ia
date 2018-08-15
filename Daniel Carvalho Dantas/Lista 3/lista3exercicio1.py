string = raw_input("digite uma string: ")
n = len(string)
contador = 0
if (n%2==0):
    for a in range (0,(n/2)):
        if (string[a] == string [n-1-a]):
            contador = contador + 1
    if contador == (n/2):
        print "a string e um palindromo"
    else:
        print "a string nao e um palindromo"
if (n%2 ==1):
    contador = 0
    for b in range (0,(n-1)/2):
        if (string[b] == string [n-1-b]):
            contador = contador + 1
    if contador == ((n-1)/2):
        print "a string e um palindromo"
    else:
         print "a string nao e um palindromo"
