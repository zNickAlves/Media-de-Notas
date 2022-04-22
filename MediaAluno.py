n1 = float(input("Informe a Nota 1 "))
n2 = float(input("Informe a Nota 2 "))
n3 = float(input("Informe a Nota 3 "))

media= (n1 + n2 + n3)/3

print("A média das notas é", {media})

if media >= 6:
    print("Aluno Aprovado")

else:
    print("Aluno Reprovado")