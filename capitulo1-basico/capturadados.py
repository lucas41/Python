"""
Recebendo dados do usuario por variavel 

"""


"""

Exemplo de print feito em versões + antigas ( versao 2.x)

"""

# emtrada de dados pelo input
nome = input('Qual o seu nome? ')
print("ola muito prazer %s" % nome)

idade = int(input("qual a sua idade ?"))
# o %s referencia onde iria ser colocado os dados
print('O(a) %s tem %s anos' % (nome, idade))


"""

Versão nova 3.x >

"""

print('Seja bem vindo(a) {0}'. format(nome))
print('A {0} tem {1} anos'.format(nome,  idade))


"""
    Exemplo feito da forma mais atual 
"""

print(f'seja bem-vindo(a) {nome}')
print(f'A {nome} tem {idade} anos')

"""

Cast é converter um tipo de dado para outro no caso do exemplo abaixo transformaremos uma string em int
 

"""

print(f'O {nome} nasceu em {2022 - idade}')


