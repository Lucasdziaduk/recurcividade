"""exercicio 3"""

def string_invertida(string):
    if len(string) == 0:
        return string
    return string[-1] + string_invertida(string[:-1])

print(string_invertida('lucas'))