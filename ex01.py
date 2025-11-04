op = int(input("Escolha uma opção: "))

match op:
    case 1:
        valor = int(input("Escolha um número:"))
        if valor % 2 == 0:
            print("É par")
        else:
            print("É ímpar")
    

    case 2:
        valor1 = int(input("Escolha um número: "))
        valor2 = int(input("Escolha outro número: "))
        if valor1 > valor2:
            print("1° valor é maior que o 2° valor")
        if valor1 < valor2:
            print("1° valor é menor que o 2° valor") 
        if valor1 == valor2:
            print("1° valor e 2° valor são iguais.")


    case 3:
        valor = int(input("Escolha um número: "))
        dobro = valor * 2
        print(f"O resultado é {dobro}")



        



