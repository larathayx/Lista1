#código para calcular o espaço percorrido dentro de um determinado tempo
tempo = int(input("digite o tempo gasto em segundos : "))
s0 = 2 #valores estipulados
v0 = 3 #valores estipulados
a = 10 #valores estipulados
espaço = s0 + (v0*tempo) + ((1/2)* a * (tempo**2)) #formula para calcular "MUV"
print (str(espaço) + " metros")