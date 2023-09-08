#projeto barbie

print(f"Olá! Pronta para descobrir qual Barbeie você é?", "\n\nQual a sua atividade favorita?", "\n\nA)Cantar", "\nB)Dançar", "\nC)Codar")

resposta = input("\nDigite sua resposta: ")

if resposta =="A":
    print(f"\nVocê gosta de natureza?", "\n\nA)Sim", "\nB)Não")   
    rsp2 = input("Digite sua resposta: ")
    if rsp2 == "B":
        barbie = "Liana - Barbie em o castelo de diamente"
    else:
        print(f"Essa Barbie não existe")
        if rsp2 == "A":
            print(f"\nvoce e competitiva?", "\n\nA)Sim", "\nB)Nao")
            rsp3 = input("Digite sua resposta: ")
            if rsp3 == "A":
                barbie = "Merliah - Barbie em vida de Sereia"
                if rsp3 == "B":
                    barbie = "Rosella - Barbie em princesa da ilha"            
            else:
                print(f"Essa barbie não existe")
        else:
            print(f"Essa Barbie não existe")
elif resposta == "B":
    print(f"\nQual atividade você gosta mais?", "\n\nA)Dirigir", "\nB)Dançar")
    rsp4 = input("Digite sua resposta: ")
    if rsp4 == "A":
        barbie = "Ryan Gosling"
        print(f"OMG he is literally me, Ryan Gosling")
    elif rsp4 == "a":
        print(f"Essa Barbie não existe")    
    else:
        print(f"\nVocê tem irmãos?", "\n\nA)Sim\nB)Não")
        rsp5 = input("Digite sua resposta: ")
        if rsp5 == "B":
            barbie = "“Odette - Barbie lago dos cisnes"
        else:
            print(f"\nQuantos irmãos você tem?")
            n_irm = input("Digite sua resposta: ")
            if n_irm == "0":
                barbie = "Barbie sem irmãos"
                if n_irm>"0" and n_irm<="3":
                    barbie = "Barbie sem irmãos"
                    if n_irm == "3":
                        barbie = "Corinne - Barbie e as três mosqueteiras"
            else:
                barbie = "Genevieve - Barbie 12 princesas"
elif resposta == "C":
    print(f"\nQual você gosta mais?\n\nA)Moda\nB)Estudar\nC)Brincar com pet")
    rsp6 = input("Digite sua resposta: ")
    if rsp6 == "A":
        barbie = "A Barbie - Moda e Magia"
    elif rsp6 == "B":
            barbie = "Blair - Barbie escola de princesas"
    elif rsp6 == "C":
            barbie = "Elina - Barbie fairytopia"
else:
    print(f"Essa Barbie não existe")
     
if (barbie != "Essa Barbie não existe" and barbie != "OMG he is literally me, Ryan Gosling"):
    print("Parabéns! Sua barbie eh ", barbie)
else:
    print(barbie)