# código para calcular quantos azulejos são necessários para azulejar uma parede
alturaP = float(input (" Digite a altura da parede em metros: "))
larguraP = float(input (" Digite a largura da parede em metros: "))
alturaA = float(input (" Digite a altura do azulejo em centimetros: "))
larguraA = float(input (" Digite a largura do azulejo em centimetros: "))


conversão1 = alturaA / 100 # conversão de cm para metros
conversão2 = larguraA / 100


areaP = alturaP * larguraP  # calcula a área da parede
areaA = conversão1 * conversão2 # calcula a área do azulejo


quant = areaP / areaA  
print (quant)
