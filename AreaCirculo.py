import math

raio = float(input("Informe o raio do círculo: "))
area = math.pi * (raio ** 2)

print(f"A área do círculo é: {'{:.2f}'.format(area)} cm^2")