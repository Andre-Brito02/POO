class CurrencyConverter:
    def __init__(self, cotacao_dolar:float, qtd_dolar_comprado:float):
        self._cotacao_dolar = cotacao_dolar
        self._qtd_dolar_comprado = qtd_dolar_comprado
        self._IOF = 0.06

    def valor_total(self):
        return (self._qtd_dolar_comprado + (self._qtd_dolar_comprado * self._IOF)) * self._cotacao_dolar

    def __str__(self):
        return f'Amount to be paid in reais: R$ {self.valor_total():.2f}'

cotacao_dolar = float(input("What is the dollar price? "))
qtd_dolar_comprado = float(input("How many dollars will be bought? "))
cc = CurrencyConverter(cotacao_dolar, qtd_dolar_comprado)

print(cc)