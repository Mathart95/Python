x = int(input("1° valor: "))
y = int(input("2° valor: "))

print(" + soma")
print(" - subtração")
print(" * multiplicação")
print(" / divisão")

operacao = input("Escolha uma operação: ")
match operacao:
    case "+":
        soma = x + y
        print(f"{x} + {y} = {soma}")
    case "-":
        sub = x - y
        print(f"{x} - {y} = {sub}")
    case "*":
        mult = x * y
        print(f"{x} * {y} = {mult}")
    case "/":
        div = x/y
        print(f"{x} / {y} = {div}")