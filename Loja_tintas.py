area_cobertura = 3
capacidade_lata = 18
valor_lata = 80.0

tamanho_area = float(input("Digite o tamanho da área a ser pintada (em m²): "))

litros = round(tamanho_area/area_cobertura, 2)
latas_inteiras = int(litros/capacidade_lata)
if litros % capacidade_lata != 0:
    latas_inteiras += 1
valor_total = latas_inteiras * valor_lata

print("Quantidade de litros de tinta necessários", litros)
print("Quantidade de latas de tinta necessárioa", latas_inteiras)
print("Valor total da compra: R$ ", valor_total)

