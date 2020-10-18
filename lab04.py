a = float(input())
b = float(input())
c = float(input())

#Lados#
if a<=0 or b<=0 or c<=0 or a>b+c or b>a+c or c>a+b:
    print("Valores inválidos na entrada")
else:
    if a == b == c:
        print("Triângulo equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")

#Angulos#
    if a>b and a>c:
        if a**2 < b**2 + c**2:
            print("Triângulo acutângulo")
        elif a**2 == b**2 + c**2:
            print("Triângulo retângulo")
        else:
            print("Triângulo obtusângulo")
    elif b>a and b>c:
        if b**2 < a**2 + c**2:
            print("Triângulo acutângulo")
        elif b**2 == a**2 + c**2:
            print("Triângulo retângulo")
        else:
            print("Triângulo obtusângulo")
    else:
        if c**2 < a**2 + b**2:
            print("Triângulo acutângulo")
        elif c**2 == a**2 + b**2:
            print("Triângulo retângulo")
        else:
            print("Triângulo obtusângulo")
