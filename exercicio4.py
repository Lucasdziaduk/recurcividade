"""exercicio 4"""

def juros_compostos(valor_investido_mensal, valor_total=0, meses=0, rendimento=1.0005, objetivo=100000):
    if valor_total >= objetivo:
        print(f"Tempo para atingir R$ {objetivo}: {meses // 12} anos e {meses % 12} meses")
        print(f"Valor investido até R$ {objetivo}: R$ {valor_investido_mensal * meses}")
        print(f"Juros compostos até R$ {objetivo}: R$ {valor_total - (valor_investido_mensal * meses)}")
        return valor_total
    else:
        valor_total = (valor_total + valor_investido_mensal) * rendimento

        return juros_compostos(valor_investido_mensal, valor_total, meses + 1, rendimento, objetivo)


valor_investido_mensal = 500

juros_compostos(valor_investido_mensal)

