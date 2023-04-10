a = int(input("Digite um número para o lado a: "))
b = int(input("Digite um número para o lado b: "))
c = int(input("Digite um número para o lado c: "))


if (a + b > c) and (a + c > b) and (b + c > a):
    if (a==b) and (a==c) and (b==c):
        print("Equilátero")
    elif (a==b) or (a==c) or (b==c):
        print("Isósceles")
    else:
        print("Escaleno")
else: 
    print("Não é um triângulo")

    
    
        
