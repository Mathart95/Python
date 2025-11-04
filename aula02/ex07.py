preco = float(input("Digite o preço do produto: R$ "))

if preco <= 100:
  desconto = preco * 0.10
else:
  desconto = preco * 0.20

valor = preco - desconto
print(f"desconto aplicado: R${desconto:.2f}")
print(f"preço final com desconto: R${valor:.2f}")