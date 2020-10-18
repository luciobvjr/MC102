#Entrada#

massa = float(input("Massa corporal: "))
idade = int(input("Idade: "))
if idade<18 and idade>16:
    doc = input("Documento de autorização: ")
febre = input("Febre ou sintomas gripais: ")
viagem = input("Viagem recente ao exterior: ")
covid = input("Contato com caso de COVID-19: ")
primeira = input("Primeira doação: ")
if primeira=="N":
    ult_ano = int(input("Doações nos últimos 12 meses: "))
    if ult_ano>0:
        meses_ult = int(input("Meses desde a última doação: "))
sexo = input("Sexo biológico: ")
if sexo=="F":
    gravida = input("Grávida ou amamentando: ")

###    Condições    ####

#massa corporal mínima: 50kg
a = True
if a==True:
    if massa<50:
        print("Impedimento: abaixo da massa corporal minima")
        a=False
        
#idade mínima: 16
#idade máxima: 69
#menor de 18 precisa de consentimento dos responsáveis
#Se maior de 60, já deve ter sido doador antes
        
    if idade<16:
        print("Impedimento: menor de 16 anos")
        a=False
    if idade>69:
        print("Impedimento: maior de 69 anos")
        a=False
    if idade==16 or idade==17 and doc=="N":
        print("Impedimento: menor de 18 anos sem consentimento dos responsáveis")
        a=False
    if idade>60 and primeira=="S":
        print("Impedimento: maior de 60 anos e primeira doação")
        a=False

#Não ter tido febre ou sintomas gripais nos últimos 14 dias
    if febre=="S":
        print("Impedimento: febre ou sintomas gripais")
        a=False
        
#Não ter viajado ao exterior nos útimos 30 dias
    if viagem=="S":
        print("Impedimento: viagem recente ao exterior")
        a=False
        
#Contato com caso suspeito ou confirmado de COVID-19 nos útimos 30 dias
    if covid=="S":
        print("Impedimento: contato com caso de COVID-19")
        a=False
        
#Masculino: max 4 anuais e intervalo de 2 meses
    if primeira=="N":
        if sexo=="M" and ult_ano>=4:
            print("Impedimento: número máximo de doações anuais foi atingido")
            a=False
        if ult_ano>0:
            if sexo=="M" and meses_ult<2:
                print("Impedimento: intervalo mínimo entre as doações não foi respeitado")

#Feminino: max 3 anuais e intervalo de 3 meses / não estar grávida ou amamentando
    if primeira=="N":
        if sexo=="F" and ult_ano>=3:
            print("Impedimento: número máximo de doações anuais foi atingido")
            a=False
        if ult_ano>0:
            if sexo=="F" and meses_ult<3:
                print("Impedimento: intervalo mínimo entre as doações não foi respeitado")
    if sexo=="F" and gravida=="S":
        print("Impedimento: grávida ou amamentando")
        a=False
        
if a==True:
    print("Agende um horário para triagem completa")
