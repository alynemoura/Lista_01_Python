mb = int(input("Qual tamanho do arquivo que deseja fazer download em MB? "))
link = int(input("Qual a velocidade do seu link em Mbps? "))
tempo = (mb / (link / 8)/ 60)
minuto = hora = dia = 0
hora_total = int(tempo / 60)
dia = int(hora_total/24)
hora = hora_total - (dia * 24)
minuto = int(tempo - ((dia * 24 * 60) + hora * 60))

print(f"Para efetuar um download de {mb} MB com a velocidade de {link} Mbps, irá demorar:"
      f" {dia}dia(s) {hora}h:{minuto} minutos.")
