medida = float(input("Digite uma medida em metros: "))
cm = medida * 100

print("A medida de {} metros corresponde a {} centímetros.".format(medida, '{:.3f}'.format(cm)))