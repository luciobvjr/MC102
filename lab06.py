#Entrada: tempos em segundos até -1

tempos=[]
t = float(input())
tempos.append(t)
while t!=-1:
    t = float(input())
    if t!=-1:
        tempos.append(t)
tempos.sort()

#Nivel 0: tempo < 180
#Nivel 1: 180 =< tempo > 240
#Nivel 2: tempo >= 240

n_zero = []
n_um = []
n_dois = []

i=0
while i in range(len(tempos)):
    if tempos[i]<180:
        n_zero.append(tempos[i])
    elif tempos[i]>=240:
        n_dois.append(tempos[i])
    else:
        n_um.append(tempos[i])
    i=i+1

#Tempo médio de conclusão do percurso

soma=0
j=0
while j in range(len(tempos)):
    soma = soma + tempos[j]
    j=j+1
medio = soma/len(tempos)

#Maior velocidade (cm/min) dado que o percurso tem 33cm
#A lista já foi organizada com o sort

melhor_tempo_minutos = tempos[0]/60
maior_velocidade = 33/melhor_tempo_minutos

pior_tempo_minutos = tempos[len(tempos)-1]/60
menor_velocidade = 33/pior_tempo_minutos

#Saída

print("Caracóis no nível 0:",len(n_zero))
print("Caracóis no nível 1:",len(n_um))
print("Caracóis no nível 2:",len(n_dois))
print("Tempo médio de conclusão do percurso:",format(medio,'.1f'),"segundos")
print("Maior velocidade:",format(maior_velocidade,'.1f'),"cm/min")
print("Menor velocidade:",format(menor_velocidade,'.1f'),"cm/min")
