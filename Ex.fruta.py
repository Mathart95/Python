fruta = input("escolha a fruta: ")
match fruta:
    case "maçã":
        print("É uma maçã")
    case "banana":
        print("É uma banana")
    case _:
        print("Escolha errada, é uma outra fruta")    
