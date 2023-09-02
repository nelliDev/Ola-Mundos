ryan = 0
barbie = "0"
print("Olá! Pronta pra descobrir qual barbie você é?")
print("Qual a sua atividade favorita?")
print("A) cantar")
print("B) dançar")
print("C) codar")
resposta = input()
if resposta == 'A':
    print("Você gosta de natureza?")
    print("A) Sim")
    print("B) Não")
    resposta2 = input()
    if resposta2 == 'A':
        print("Você é competitiva?")
        print("A) Sim")
        print("B) Não")
        resposta3 = input()
        if resposta3 == 'A':
            barbie = "Merliah - Barbie em  vida de Sereia"
        elif resposta3 == 'B':
            barbie = "Rosella - Barbie em  princesa da ilha"
    elif resposta2 == 'B':
        barbie = "Liana - Barbie em o Castelo de Diamante"
elif resposta == 'B':
    print("Qual atividade você gosta mais?")
    print("A) dirigir")
    print("B) dançar")
    resposta4 = input()
    if resposta4 == 'A':
        ryan = 1
    elif resposta4 == 'B':
        print("Você tem irmãos?")
        print("A) Sim")
        print("B) Não")
        resposta5 = input()
        if resposta5 == 'B':
            barbie = "Odette - Barbie lago dos cisnes"
        elif resposta5 == 'A':
            print("Quantos irmãos você tem?")
            irmaos = int(input())
            if irmaos == 0:
                barbie = "Barbie sem irmãos"
            elif irmaos > 0 and irmaos<3:
                barbie = "Tori - Barbie: a princesa e a popstar"
            elif irmaos==3:
                barbie = "Corinne - Barbie e as três mosqueteiras"
            else:
                barbie = "Genevieve - Barbie 12 princesas"
elif resposta == 'C':
    print("Qual você gosta mais?")
    print("A) moda")
    print("B) estudar")
    print("C) brincar com pet")
    resposta2 = input()
    if resposta2 == 'A':
        barbie = "A Barbie - Moda e Magia"
    elif resposta == 'B':
        barbie = "Blair - Barbie escola de princesas"
    elif resposta == 'C':
        barbei = "Elina - Barbie fairytopia"
 
if ryan :
    print("OMG he’s literally me, Ryan Gosling")
elif barbie == "0":
    print("Essa Barbie não existe!")
else:
    print("Parabéns! Sua Barbie é", barbie)