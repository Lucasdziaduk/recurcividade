"""Exercicio 5"""

preco_mes_bitcoin = [212335, 306600, 359693, 316571, 355299, 352600, 368540, 333842, 345411, 409131, 580819, 583265] 

def calcular_bitcoin(valor_investido_mensal, saldo_total=0, meses=0, bitcoins_comprados=0, preco_mes_bitcoin=preco_mes_bitcoin, objetivo=100000):
    preco_atual = preco_mes_bitcoin[meses % len(preco_mes_bitcoin)]
    

    bitcoins_comprados += valor_investido_mensal / preco_atual

    saldo_total = bitcoins_comprados * preco_atual

    if saldo_total >= objetivo:
        anos = meses // 12
        meses_restantes = meses % 12
        print(f"Tempo para atingir R$ {objetivo}: {anos} anos e {meses_restantes} meses")
        print(f"Valor investido até R$ {objetivo}: R$ {valor_investido_mensal * meses}")
        print(f"Lucro sobre investimento é de R$ {objetivo}: R$ {saldo_total - (valor_investido_mensal * meses)}")
        return saldo_total
    else:
        return calcular_bitcoin(valor_investido_mensal, saldo_total, meses + 1, bitcoins_comprados, preco_mes_bitcoin, objetivo)


valor_investido_mensal = 250  
calcular_bitcoin(valor_investido_mensal)
