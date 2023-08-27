#código para calcular o custo de um carro novo ao consumidor
custoFab = int(input ("Digite o custo de fábrica do carro: "))
porcentagem = custoFab * (28/100) #taxas em cima do valor de fábrica
imposto = custoFab * (45/100)


custoTotal = custoFab + porcentagem + imposto #custo total para o consumidor
print ("O custo total do carro será de : " +str(custoTotal)+ " reais")