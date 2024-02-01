valor_por_hora = float(input("Digite o valor recebido por hora trabalhada: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
minutos_trabalhados = float(input("Digite o número de minutoss trabalhados no mês (além das horas): "))

minutos_em_decimal = round(minutos_trabalhados/60, 2)

salario_bruto = round((horas_trabalhadas+minutos_em_decimal)*valor_por_hora, 2)
ir = round((salario_bruto *11/100),2)
inss = round((salario_bruto*8/100),2)
sindicato = round((salario_bruto*5/100),2)
salario_liquido = round((salario_bruto - ir -inss - sindicato),2)

print("+ Salario Bruto: R$ ", salario_bruto)
print("- IR(11%): R$ ", ir)
print("- INSS(8%): R$ ", inss)
print("- Sindicato(5%): R$ ", sindicato)
print(" = Salario Líquido: R$ ", salario_liquido)

