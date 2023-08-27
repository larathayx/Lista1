# código para calcular o IMC de uma pessoa
massa = float(input (" Digite o seu peso em kg:  "))
altura = float(input (" Digite sua altura em metros: "))
imc = massa / (altura **2) # formula para o cálculo


print ("O seu Indice de Massa Corporal é: " + str(imc))
