# código para calcular a média semestral de um aluno
prova1 = float(input ("Digite o valor da primeira prova:  "))
prova2 = float(input ("Digite o valor da segunda prova:  "))
atividade = float(input ("Digite o valor da atividade:  "))
media = ((4 * prova1) + (3 * prova2) + (2 * atividade)) / 9


print ("A media semestral é de: " + str(media))