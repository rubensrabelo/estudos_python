from services.CurrencyConverter import CurrencyConverter

current_value = float(input("Digite o valor atual: "))
quantity_buy = float(input("Digite a quantidade da compra: "))

converter = CurrencyConverter(current_value, quantity_buy)
print(converter)
