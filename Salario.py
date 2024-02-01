valor_hora = float(input("Por favor, digite o valor da sua hora de trabalho: "))
horas_trabalhadas = int(input("Informe o número de horas trabalhadas no mês: "))
minutos_trabalhados = int(input("Informe a quantidade de minutos trabalhados no mês, além das horas: "))

minutos_decimal = round(minutos_trabalhados/60, 2)

salario = round((horas_trabalhadas + minutos_decimal) * valor_hora, 2)

print("O seu salário deste mês é de: ", salario)