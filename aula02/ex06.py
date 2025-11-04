preco = float(input("Digite o preço do produto: R$"))

if preco <= 100:
  desconto = 0.10
else:
  desconto = 0.20

valor = preco - (preco*desconto)
print(f"desconto aplicado: {desconto*100}%")
print(f"preço final com desconto: {valor:.2f}")