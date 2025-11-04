# O usuário entra com dois valores inteiros e o programa responde quem é o maior entre eles
A=int (input("Escolha o 1° número: "))
B=int (input("Escolha o 2° número: "))
if(A > B): 
    print(A, "é maior que", B)
else:
    print(A, "é menor que", B)
#f = format = formata a variável
if(A > B): 
    print(f"O {A} é maior que {B}")
else:
    print(f"O {B} é menor que {A}")
    #{} interpolação = coloca o valor da variável nas Strings