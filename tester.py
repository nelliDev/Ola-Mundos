import sys
import os
from colorama import Fore, Back, Style

def mostra_errados(errados):
    os.system('clear')
    print()
    print("TESTES ERRADOS:")
    for erro in errados:
        print(f"teste {erro[0]}:")
        print("===========================================================================")
        print("=========== Resultado obtido: ================")
        print(erro[1])
        print("========== Resultado esperado: ===============")
        print(erro[2])
        print()


def teste_auto(absolute_path, submission_path, lab, num_testes):
    errados = []
    for i in range(1, num_testes+1):
        test_path = os.path.join(absolute_path, f"{lab}/testes/{i}")
        
        result = os.popen(f"python3 {submission_path} < {test_path}.in").read()
        expected = os.popen(f"cat {test_path}.out").read()
        
        if result == expected:
            print(Fore.GREEN + f"teste {i}: Correto")
        else:
            errados.append((i, result, expected))
            print(Fore.RED + f"teste {i}: Incorreto")
    return errados
    
    
def teste_semimanual(absolute_path, submission_path, lab, num_testes):
    errados = []
    for i in range(1, num_testes+1):
        os.system('clear')
        test_path = os.path.join(absolute_path, f"{lab}/testes/{i}")
        
        result = os.popen(f"python3 {submission_path} < {test_path}.in").read()
        expected = os.popen(f"cat {test_path}.out").read()

        print(f"teste {i}:")
        print("=========== Resultado obtido: ================")
        print(result)
        print("========== Resultado esperado: ===============")
        print(expected)
        print()
        
        avaliacao = input("Vc acha que ta certo(s/n)? ")[0].lower()
        if avaliacao != 's':
            errados.append((i, result, expected))
            
    return errados

def teste_manual(absolute_path, submission_path, lab, num_testes):
    errados = []
    for i in range(1, num_testes+1):
        os.system('clear')
        test_path = os.path.join(absolute_path, f"{lab}/testes/{i}")
        
        expected_input = os.popen(f"cat {test_path}.in").read()
        
        print(f"Anote a entrada padrão desse teste (teste{i})")
        print("Digite a entrada adaptada abaixo:")
        print(expected_input)
        
        result = os.popen(f"python3 {submission_path}").read()
        expected = os.popen(f"cat {test_path}.out").read()
        
        print(f"teste {i}:")
        print("=========== Resultado obtido: ================")
        print(result)
        print("========== Resultado esperado: ===============")
        print(expected)
        print()
        
        avaliacao = input("Vc acha que ta certo(s/n)? ")[0].lower()
        if avaliacao != 's':
            errados.append((i, result, expected))
            
    return errados


def main():
    os.system('clear')
    absolute_path = os.path.dirname(__file__)
    
    lab = sys.argv[1]
    nome = sys.argv[2]
    
    submission_path = os.path.join(absolute_path, f"{lab}/submissoes/{nome}")
    num_testes = len(os.listdir(os.path.join(absolute_path, f"{lab}/testes/"))) // 2
    
    if len(sys.argv) == 3 or sys.argv[3] == "auto":
        errados = teste_auto(absolute_path, submission_path, lab, num_testes)
    elif sys.argv[3] == "semi":
        errados = teste_semimanual(absolute_path, submission_path, lab, num_testes)
    elif sys.argv[3] == "manual":
        errados = teste_manual(absolute_path, submission_path, lab, num_testes)
    else:
        print(Fore.RED + "Esse modo de correção não existe!")
        print(Style.RESET_ALL)
        sys.exit()
            

    print(Style.RESET_ALL)
    if len(errados) > 0:
        mostra_errados(errados)
    
    print(f"nota: {num_testes-len(errados)}/{num_testes}")

main()