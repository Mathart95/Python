# O usuário entra com dois valores inteiros e o programa responde se: 1° valor é maior que o 2° valor; 2° valor é maior que o 1° valor; 1° valor é igual ao 2° valor
A= int (input("Escolha o 1° número: "))
B= int (input("Escolha o 2° número: "))

if (A == B): 
    print(f"O número {A} é igual ao número {B}")
elif (A > B):
    print(f"O número {A} é maior que o número {B}")
else:
    print(f"O número {A} é menor que o número {B}")
    