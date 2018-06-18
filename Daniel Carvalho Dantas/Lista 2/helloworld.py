'''
esse programa provavelmente foi feito de uma maneira burra,mas faz sentido
levando em consideracao o ingles
as unidades sao repetidas 10x por centena,e 10x as dezenas(ex: vinte,trinta)
contudo nas centenas (ex:de one hundred ate one hundred ninety nine elas aparecem 100x)
os numeros de 11 a 19 acontecem apenas uma vez por centena
o numero hundred aparecera de 100 ate 999 (900x)
o and ocorrera 891x (de onde hundred and one ate nine hundred and ninety nine )
por fim,havera o numero one thousand
o calculo final sera entao 90x len(dezenas) + 10x len(numeros de 10 a 19) +
(100 + 90) * len(unidades) + 900 len(hundred) + len(onethousand)
'''
dezenas = 100*(len("twenty") + len("thirty") + len("forty") + len("fifty") + len("sixty") + len("seventy") + len("eighty")
              + len("ninety"))
zeroadezenove = 10 *(len("ten") +len("eleven") +len("twelve") +len("thirteen") +len("fourteen") +len("fifteen")
                     +len("sixteen") +len("seventeen") +len("eighteen") +len("nineteen"))
unidades = 190 * (len("one") +len("two") +len("three") +len("four") +len("five") +len("six") +len("seven") +len("eight") +len("nine") )

hundred = 900 * (len("hundred"))

thousand = len("onethousand")
contand = 891 * len("and")

print dezenas + zeroadezenove + unidades + hundred + thousand + contand
