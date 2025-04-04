nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))

media = (nota1 + nota2)/2
print(media)
if media >=9:
    print("passou com mérito")

elif media >= 8:
    print("passou como se esperava")
else:
    print("Reprovado. Estude mais, filho")
