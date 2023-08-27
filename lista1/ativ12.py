# código para calcular o salário de um vendedor de uma concessionária
carrosVendidos = int (input("Digite a quantidade de carros vendidos: "))
valorVendas = int (input("Digite o valor total das vendas: "))
salárioFixo = float (input("Digite o valor do seu salario fixo: "))
valorComissão = float (input("Digite o valor de comissão por carro vendido: "))


salarioF = salárioFixo + (valorComissão * carrosVendidos) + ((5/100) * valorVendas) # fórmula para cálculo do salário final
print ("Seu salario final é de: " +str(salarioF)+ " reais")