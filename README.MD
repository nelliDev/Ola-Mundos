# Esse é o repositório do Olá Mundos!


## Instruções para professores

### Criando labs:
Para criar um novo lab, simplesmente crie uma nova pasta (se ela já não existe) com o nome do lab. Dentro dessa pasta, precisamos criar mais 2 subpastas: ```submissoes``` e ```testes```. Dentro de testes, crie as entradas e saídas de teste como ```i.in``` e ```i.out```, onde i é o número do teste. 
#### Exemplo:
Criando o lab02 com 3 testes, a estrutura final da pasta deve ficar algo assim:
```
lab02/
├─ submissoes/
│  ├─ lima.py
│  ├─ kina.py
├─ testes/
│  ├─ 1.in
│  ├─ 1.out
│  ├─ 2.in
│  ├─ 2.out
│  ├─ 3.in
│  ├─ 3.out
```
### Sobre tester.py:
Eu (nelli) não gostei do codepost por alguns motivos.
1. A submissão é complicada pros alunos miniqueridos
1. Qualquer diferença entre output esperado dá pau nos testes, e corrigir manualmente vendo os resultados é muuuito ruim no codepost
1. O site em si é podre todo cagado lento capenga broxa e ruim
1. Dar acesso aos professores e alunos é mt ruim

Por isso criei esse repositório para os professores, que possibilita, além da correção automática (que é muito mais simples de fazer), uma correção manual intuitiva dos testes.

### Como usar tester.py:

Supondo que os arquivos testes já foram criados corretamente:
1. Clonar o repositório (ou não, acho que dá pra rodar no vscode do navegador que vem com o github).
1. Adicionar o arquivo a ser corrigido em {nome do lab}/submissions (cuidado para não ter nomes de arquivos repetidos).
1. No terminal rode tester.py com os seguintes argumentos: nome do lab, nome do arquivo, modo de correção. (opcional)
1. Pronto!

#### Exemplo:
Supomos que o miniquerido Lucas Baptista acabou de te enviar o código dele do ```lab01``` pronto como ```lucas01.py```. Adicone ```lucas.py``` em ```/lab01/submissoes``` e rode (no terminal):

```
python3 tester.py lab01 lucas.py
``` 

Oh no! Todos os testes deram errados! Será que ele errou tudo mesmo ou só errou a formatação do output? Vamos corrigir manualmente rodando

```
python3 tester.py lab01 lucas.py manual
```

Agora os testes serão executados 1 a 1 automaticamente, com o avaliador apenas dizendo se ele errou ou acertou cada um.

Pronto, agora já podemos saber a nota dos testes (no caso do Lucas 18/21)!


