limite = 50
excesso = 0
multa_por_kg = 4

peso = float(input("Digite o peso total dos peixes: "))
if peso > limite:
    excesso = peso - limite
    multa = excesso * multa_por_kg
    print("Peso acima do limite de ",limite,"Kg. Multado em R$ ", multa, "pelo excesso de ", excesso, "kG")

else:
    print("Peso abaixo do limite de ",limite, "Kg. Não foi multado")