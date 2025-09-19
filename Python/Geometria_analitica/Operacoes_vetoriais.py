import numpy as np
from numpy.linalg import det

print('Adição/Subtração ')
print('Multiplicação por escalar')
print('Produto interno')
print('Produto vetorial')
print('Produto misto')
operação = input("Qual operação você quer realizar: ")
operação = operação.lower()

if operação == "adição" or operação == "subtração":
    while True:
        try:
            dimensao = float(input("Digite 2 para vetor 2D ou 3 para vetor 3D: "))
            if dimensao == 2 or dimensao == 3:
                break
            else:
                print("Digite um valor válido.")
        except ValueError:
            print("Digite um número(2 ou 3) ")
    while True:   
        try:
            if dimensao == 2:
                x1,y1 = map(float, input("Digite o primeiro vetor(Separe com espaços): ").split())
                x2,y2 = map(float, input("Digite o segundo vetor(Separe com espaços): ").split())
            
            else:
                x1,y1,z1 = map(float, input("Digite o primeiro vetor(Separe com espaços): ").split())
                x2,y2,z2 = map(float, input("Digite o segundo vetor(Separe com espaços): ").split())
            break
        except ValueError:
            print("Entrada inválida. Digite os valores separados por espaço ou todos/somente os vetores necessários.")
        
    
    while True:
        operacao = input("Escolha soma(+) ou subtração(-): ")
        if operacao == '+':
            if dimensao == 2:
                print(f'({x1 + x2},{y1+y2})')
            else:
                print(f'({x1 + x2},{y1 + y2},{z1 + z2})')   
            break
        elif operacao == "-":        
            if dimensao == 2:
                print(f'({x1 - x2},{y1 - y2})')
            else:
                print(f'({x1 - x2},{y1 - y2},{z1 - z2})')
            break
        else:
            print('Digite um operador válido(+/-)')

elif operação == "multiplicação por escalar":
    while True:
        try:
            dimensao = float(input("Digite 2 para vetor 2D ou 3 para vetor 3D: "))
            if dimensao == 2 or dimensao == 3:
                break
            else:
                print ("Entrada inválida.")
        except ValueError:
            print ("Entrada inválida.")
    if dimensao == 2:
        while True:
            try:
                x = float(input("Digite a coordenada x: "))
                break
            except ValueError:
                print ('Entrada inválida.')
        while True:
            try:
                y = float(input("Digite a coordenada y: "))
                break
            except ValueError:
                print ('Entrada inválida.')
        vetor = [x, y]
    else:
        while True:
            try:
                x = float(input("Digite a coordenada x: "))
                break
            except ValueError:
                print ("Entrada inválida.")
        while True:
            try:
                y = float(input("Digite a coordenada y: "))
                break
            except ValueError:
                print ("Entrada inválida.")
        while True:
            try:
                z = float(input("Digite a coordenada z: "))
                break
            except ValueError:
                print ("Entrada inválida.")
        vetor = [x, y, z]
    while True:
        try:
            escalar = float(input("Digite o escalar: "))
            break
        except ValueError:
            print ("Entrada inválida.")
    if dimensao == 2:
        produto_x = x * escalar
        produto_y = y * escalar
        resultado = [produto_x, produto_y]
    else:
        produto_x = x * escalar
        produto_y = y * escalar
        produto_z = z * escalar
        resultado = [produto_x, produto_y, produto_z]
    
    print(f'A multiplicação do vetor {vetor} pelo escalar {escalar} resultou no vetor {resultado}.')
    
elif operação == "produto interno":
    vetorum = list(map(int, input("Digite os valores do primeiro vetor: ").split()))
    vetordois= list(map(int, input("Digite os valores do segundo vetor: ").split()))
    
    multiplicação = 0
    
    for i in range(len(vetorum)):
        multiplicação += (vetorum[i] * vetordois[i])
    
    print(f'resultado do produto interno entre os vetores: {multiplicação}')
    
elif operação == "produto vetorial":
    # entrada dos vetores
    vetor1 = input("Digite o primeiro vetor: ")
    vetor2 = input("Digite o segundo vetor: ")
    
    #tratamento dos dados para realizar o cálculo 
    vetor1 = vetor1.strip("()")
    vetor2 = vetor2.strip("()")
    x1, y1, z1 = map(int,vetor1.split(","))
    x2, y2, z2 = map(int,vetor2.split(","))
    
    #cálculo do produto vetorial
    x3 = (y1 * z2) - (z1 * y2)
    y3 = ((x1 * z2) - (z1 * x2))*(-1)
    z3 = (x1 * y2) - (y1 * x2)
    
    vetor3 = (x3,y3,z3)

    print(f"O produto vetorial resultante dos vetores ({vetor1}) e ({vetor2}) é igual a {vetor3}")
    
elif operação == "produto misto":
    while True:
        try:
            print(' ')
            print('A formula do produto misto é: ( v1 X v2 )⋅v3')
            print(' ')
            x, y, z = map(float, input('Digite o vetor 1 (formato x,y,z): ').split(','))
            x1, y1, z1 = map(float, input('Digite o vetor 2 (formato x,y,z): ').split(','))
            x2, y2, z2 = map(float, input('Digite o vetor 3 (formato x,y,z): ').split(','))
            print(' ')
            print(f'Seu vetor 1: ({x} , {y} , {z})')
            print(f'Seu vetor 2: ({x1} , {y1} , {z1})')
            print(f'Seu vetor 3: ({x2} , {y2} , {z2})')
            print(' ')
            prosseguir = input('deseja prosseguir? S ou N: ')
            if prosseguir=='N':
                continue
            else:
                matriz = np.array([[x, y, z], 
                                   [x1,y1,z1], 
                                   [x2,y2,z2]])
                print(' ')
                print('Matriz:')
                for row in matriz:
                    print(" ".join(str(elem) for elem in row))
                print(' ')
                determinante = det(matriz)
                print('O resultado da determinante dessa matriz é o produto misto dos vetores')
                print(' ')
                print(f'resultado da determinante = {determinante:.2f}')
            print(' ')
            stop = input('Quer parar? S ou N: ').upper()
            if stop=='S':
                break 
    
        except ValueError:
            print("Erro: Você deve não digitou os vetores corretamente")
