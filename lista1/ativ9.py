#código para calcular uma compra de bananas e maçãs
maças = int(input("Digite a quantidade de maças compradas: "))
banana = float(input("Digite a quantidade de banana comprada em kg: "))


total = (maças * 1.50 ) + (banana * 5) #valor por unid da maçã = 1.50 / valor do kg da banana = 5.00
print ("A sua compra é de " +str(total) +" reais")