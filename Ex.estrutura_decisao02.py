nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário: R$").replace(',','.'))

#inss
if salario >= 3000:
    inss = salario * 0.11
elif salario >= 2000:
    inss = salario * 0.09
else:
    inss = salario * 0.08

#vt
if salario >= 2000:
    vt = salario * 0.06
else:
    vt = salario * 0.05

#bonus
if salario >= 3000:
    bonus = 300
else:
    bonus = 200

#cargo
if salario >= 3000:
    cargo = "Acionista"
elif salario >= 2000:
    cargo = "Gerente"
else:
    cargo = "Vendedor"

salarioLiquido = salario - (inss+vt) + bonus

#saídas:
print(f"Nome: {nome}")
print(f"Salário: {salario:.2f}".replace('.',','))
print(f"Cargo: {cargo}".replace('.',','))
print(f"Desconto INSS: {inss:.2f}".replace('.',','))
print(f"Desconto VT: {vt:.2f}".replace('.',','))
print(f"Bônus: {bonus:.2f}".replace('.',','))
print(f"Salário Líquido: {salarioLiquido:.2f}".replace('.',','))