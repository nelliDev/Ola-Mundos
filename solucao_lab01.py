def branch_tres():
    print("Qual você gosta mais?")
    print("A) moda")
    print("B) estudar")
    print("C) brincar com pet")
    resp = input()
    if(resp == "A"):
        return "A Barbie - Moda e Magia"
    elif(resp == "B"):
        return "Blair - Barbie escola de princesas"
    elif(resp == "C"):
        return "Elina - Barbie fairytopia"
    else:
        return "Essa Barbie não existe!"




def branch_dois():
    print("Qual atividade você gosta mais?")
    print("A) dirigir")
    print("B) dançar")
    resp = input()
    if(resp == "A"):
        return  "OMG he’s literally me, Ryan Gosling"
    elif(resp == "B"):
        print("Você tem irmãos?")
        print("A) Sim")
        print("B) Não")
        resp2 = input()
        if(resp2 == "B"):
            return "Odette - Barbie lago dos cisnes"
        elif(resp2 == "A"):
            print("Quantos irmãos você tem?")
            irmoes = int(input())
            if(irmoes < 3 and irmoes > 0):
                return "Tori - Barbie: a princesa e a popstar"
            elif(irmoes == 3):
                return "Corinne - Barbie e as três mosqueteiras"
            elif(irmoes > 3):
                return "Genevieve - Barbie 12 princesas" 
            elif(irmoes == 0):
                return "Barbie sem irmãos"
    return "Essa Barbie não existe!"
            


def branch_um():
    print("Você gosta de natureza?")
    print("A) Sim")
    print("B) Não")
    resp = input()
    if(resp == "B"):
        return "Liana - Barbie em o Castelo de Diamante"
    elif(resp == "A"):
        print("Você é competitiva?")
        print("A) Sim")
        print("B) Não")
        resp2 = input()
        if(resp2 == "A"):
            return "Merliah - Barbie em  vida de Sereia"
        elif(resp2 == "B"):
            return "Rosella - Barbie em  princesa da ilha"
    return "Essa Barbie não existe!"


def primeira_pergunta():
    print("Qual a sua atividade favorita?")
    print("A) cantar")
    print("B) dançar")
    print("C) codar")
    resp = input()
    if(resp == "A"):
        barbie = branch_um()
    elif(resp == "B"):
       barbie = branch_dois()
    elif(resp == "C"):
        barbie = branch_tres()
    else:
        barbie = "Essa Barbie não existe!"
    return barbie

def main():
    print("Olá! Pronta pra descobrir qual barbie você é?")
    barbie = primeira_pergunta()
    if(barbie != "Essa Barbie não existe!" and barbie != "OMG he’s literally me, Ryan Gosling"):
        print(f"Parabéns! Sua Barbie é {barbie}")
    else:
        print(barbie)

if __name__ == "__main__":
    main()