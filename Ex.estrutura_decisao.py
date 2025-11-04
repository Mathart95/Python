nome = input("Digite o seu nome: ")

salario = float (input("Digite seu salário: R$"))


if salario >= 3000:
    cargo = "Acionista" 
    desconto = salario*0.11
if salario >= 2000:
    cargo ="Gerente"
    desconto = salario*0.09
if salario < 2000:
    cargo = "Vendedor"
    desconto = salario*0.08


if salario >= 2000:
    descontoVt = salario*0.06
else:
    descontoVt = salario*0.05


if salario >= 3000:
    bonus= 300
else:
    bonus = 200    

salarioLiquido = salario -(desconto+descontoVt) + bonus

print(f"Nome: {nome}")
print(f"Salário: {salario:.2f}")
print(f"Desconto: {desconto:.2f}")
print(f"Desconto_vt: {descontoVt:.2f}")
print(f"Salario_liquido: {salarioLiquido:.2f}")