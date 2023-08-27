#código para calcular a idade de uma pessoa em dias
idadeA= int(input("Digite sua idade em anos: "))
idadeM= int(input("Digite sua idade em meses: "))
idadeD= int(input("Digite sua idade em dias: "))


idade = (idadeA * 365) + (idadeM * 30) + idadeD #considerando 1 ano=365 dias e 1 mês=30 dias
print ("Sua idade em dias é: " +str(idade)+ " dias")