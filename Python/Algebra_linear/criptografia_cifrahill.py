import numpy as np
#função para inserir o texto
def inserir_texto():
    texto = input("Digite o texto a ser cifrado (Sem acentuação): ")
    texto = texto.lower().replace(" ","")
    
    print(f"Texto inserido: {texto}")

    if len(texto)%2 != 0:
        texto += "x"
    
    return texto

def equivalente_decimal(letra):
    
    alfabeto = "zabcdefghijklmnopqrstuvwxy"

    return (alfabeto.find(letra))

def equivalente_letra(numero):
   
    alfabeto = "zabcdefghijklmnopqrstuvwxy"
    
    return alfabeto[numero]

#MATRIZ CHAVE
matriz_chave = np.array([[5, 9],[4, 7]])

def cifra_hill(texto, matriz_chave):
    texto_cifrado = ""

    valor_numerico = np.empty([2,1], dtype = int)
    valor_cifrado = np.empty([2,1], dtype = int) 

    for i in range(0, len(texto)):

        if i == 0 or i%2 == 0:
            valor = equivalente_decimal(texto[i])
            valor_numerico[0][0] = valor
        else:
            valor = equivalente_decimal(texto[i])
            valor_numerico[1][0] = valor
        
        if i != 0 and i%2 != 0:
            valor_cifrado = np.dot(matriz_chave, valor_numerico)

            if valor_cifrado[0][0] > 25:
                valor_cifrado[0][0] = valor_cifrado[0][0] % 26
        
            if valor_cifrado[1][0] > 25:
                valor_cifrado[1][0] = valor_cifrado[1][0] % 26

            a = str(equivalente_letra(valor_cifrado[0][0]))
            b = str(equivalente_letra(valor_cifrado[1][0]))

            texto_cifrado += a
            texto_cifrado += b

    texto_cifrado = texto_cifrado[:len(texto)]  
    
    return texto_cifrado



def decifra_hill(texto_cifrado, matriz_inversa):
    texto_decifrado = ""

    valor_numerico = np.empty([2,1], dtype = int)
    valor_decifrado = np.empty([2,1], dtype = int) 

    for i in range(0, len(texto_cifrado)):

        if i == 0 or i%2 == 0:
            valor = equivalente_decimal(texto_cifrado[i])
            valor_numerico[0][0] = valor
        else:
            valor = equivalente_decimal(texto_cifrado[i])
            valor_numerico[1][0] = valor
        
        if i != 0 and i%2 != 0:
            valor_decifrado = np.dot(matriz_inversa, valor_numerico)

            if valor_decifrado[0][0] > 25:
                valor_decifrado[0][0] = valor_decifrado[0][0] % 26
        
            if valor_decifrado[1][0] > 25:
                valor_decifrado[1][0] = valor_decifrado[1][0] % 26

            a = str(equivalente_letra(valor_decifrado[0][0]))
            b = str(equivalente_letra(valor_decifrado[1][0]))

            texto_decifrado += a
            texto_decifrado += b

    texto_decifrado = texto_decifrado[:tamanho_original]  
    
    return texto_decifrado

texto = inserir_texto()

texto_cifrado = cifra_hill(texto, matriz_chave)

print(f"Texto cifrado: {texto_cifrado}")

#descriptografia

residuo = (matriz_chave[0][0]*matriz_chave[1][1] - matriz_chave[0][1]* matriz_chave[1][0])%26

#calculo do inverso multiplicativo com o algoritmo de euclides extendido, para encontrar o inverso da matriz chave independente da matriz utilizada
inverso = mod_inverse(residuo, 26)

descriptografia = np.array([[matriz_chave[1][1], -matriz_chave[0][1]],
                             [-matriz_chave[1][0], matriz_chave[0][0]]])
descriptografia = (descriptografia * inverso)%26

texto_decifrado = decifra_hill(texto_cifrado, descriptografia)

print(f"Texto decifrado: {texto_decifrado}")