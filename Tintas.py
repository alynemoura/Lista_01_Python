import math

print("######## LOJA DE TINTAS ######## ")

area = int(input("Quantos m² deseja pintar? --> "))

litros = (area / 6) * 1.1

latas = math.ceil(litros / 18)
valor_lata = latas * 80
galao = math.ceil(litros / 3.6)
valor_galao = galao * 25

mix_latas = round(litros / 18)
mix_galao = round((litros - mix_latas *18) / 3.6)

if (litros - (mix_galao*18) % 3.6 != 0) :
    mix_galao += 1
    total_mix = (mix_galao * 80) + (mix_galao * 25)

print(f"Se for comprar apenas latas de 18 litros, irá precisar de  {latas} latas e irá custar o valor de R$ {valor_lata:.2f}")
print(f"Se for comprar apenas galões de 3.6 litros, irá precisar de {galao} galão(ões) e irá custar o valor de R$ {valor_galao:.2f}")
print(f"Se deseja mesclar latas e galões para dar o que precisar, realmente será necessário {mix_latas} latas(s)"
      f" e {mix_galao} galão(ões) e irá custar R$ {total_mix:.2f}")