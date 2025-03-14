"""exercicio 2"""

def soma_lista(lista):
    if len(lista) == 1:
        soma = lista[0]
        return soma
    else:
        soma = lista[0] + soma_lista(lista[1:])
        return soma
lista = [1,3,5,7]      


print(soma_lista(lista))