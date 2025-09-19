import numpy as np
while True:
    
    print("Olá, este programa realiza matrizes inversas de 2x2 \n")
    
    entrada_user = input("Insira os 4 numeros da matriz de forma espaçada (somente números):\n")
    entrada = list(map(int, entrada_user.split( )))
    matriz = np.array(entrada).reshape(2,2)
    print("Matriz original:\n", matriz)
    
    a,b = matriz[0][0], matriz[0][1]
    c,d = matriz[1][0], matriz[1][1]
    
    determinante = ((a * d) - (b * c))
    
    if not np.isclose(determinante, 0):
        matriz_inversa = (1/determinante) * np.array([[d, -c], [-b, a]])
        print("A matriz inversa é:\n", matriz_inversa)
    else:
        print("A determinante da matriz é 0, portanto não é possível calcular a matriz inversa.")

    while True:
        continuar = int(input("0 - Sair\n1 - Calcular nova matriz "))
        if continuar == 0:
            exit()
        elif continuar == 1:    
              break
        else:
            print("Número inválido.")
            continue