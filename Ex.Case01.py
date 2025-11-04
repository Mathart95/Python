print("========= Opções =========")
print("1 - Par ou Ímpar")
print("2 - Maior ou Menor")
print("3 - Dobro")

op = int(input("Escolha uma opção: "))

match op:
    case 1:
        print("1- Par ou Ímpar")
        valor = int(input("Escolha um número: "))
        if valor % 2 == 0:
            print(f"{valor} é par")
        else:
            print(f"{valor} é ímpar")
    

    case 2:
        print("2- Maior ou Menor")
        valor1 = int(input("Escolha um número: "))
        valor2 = int(input("Escolha outro número: "))
        if valor1 > valor2:
            print(f"{valor1} é maior que {valor2}")
        if valor1 < valor2:
            print(f"{valor1} é menor que {valor2}") 
        if valor1 == valor2:
            print(f"{valor1} e {valor2} são iguais.")

    case 3:
        print("3- Dobro")
        valor = int(input("Escolha um número: "))
        dobro = valor * 2
        print(f"O resultado é {dobro}")
    
    case _:
        print("Opção inválida!")