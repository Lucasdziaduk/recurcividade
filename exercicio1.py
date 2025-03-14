"""exercicio 1"""

num = int(input("digite um numero para fatorar"))
def fatorial(num):
    if num == 1:
        return 1
    else:
        return num * fatorial(num-1)

print(fatorial(num))