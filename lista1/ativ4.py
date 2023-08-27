# código para calcular a área e o perímetro de um retângulo
ladoA = float(input (" Digite a altura do retangulo:  "))
ladoB = float(input (" Digite a largura ddo retangulo: "))


area = ladoA * ladoB # cálculo da área
perimetro = (2 * ladoA) + (2 * ladoB) # calculo do perímetro


print ("A area do retangulo é: " + str(area))
print ("O perimetro do retangulo é: " + str(perimetro))