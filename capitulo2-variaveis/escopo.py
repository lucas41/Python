"""
Escopo de variaveis 


1 - variavies globais
    - Reconhecidas por todo o programa

2 - variaveis locais
    - Reconhecida apenas no bloco onde foi declarada
"""

#declaração nome = numero 

numero = 42 #exemplo de variavel global

#tipagem dinamica não precisamos ficar colocando o tipo de cada variavel 

if numero > 10:
    novo = numero + 10 
    print(novo)