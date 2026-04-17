print("Caixa do Supermercado")
print("Digite o valor dos produtos (ou 0):")
preço = -1 
while preço != 0:
    preço = float(input("Valor do item: R$ "))   
    preço > 0:
        total += preço
    preco < 0:
        print("Valor inválido! Digite um preço positivo.")
print("O total da compra é: R$ {total:2}")