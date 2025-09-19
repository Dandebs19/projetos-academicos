import numpy as np
import matplotlib
import matplotlib.pyplot as plt

A = np.array([0.10, 0.30, 0.15]
             [0.30, 0.40, 0.25]
             [0.10, 0.20, 0.15])

print("A matriz A é\n\n", A)

B = np.array([4000, 4500, 4500, 4000]
              [2000, 2600, 2400, 2200]
              [5800, 6200, 6000, 6000])

print("A matriz A é\n\n", B)

Custos = np.dot(A,B)

print("A matriz com os custos por trimestre é\n\n", Custos)
print("\n")

CustosLabels = ['Matéria prima', 'pessoal', 'Despesas-gerais']
Trimestre = ["Verão","Outono","Inverno","Primavera"]

custos_totais_trimestre = Custos.sum(axis=0)
plt.figure(figsize=(8,5))

plt.xlabel('Custos')

plt.ylabel('Trimestre')


plt.barh(Trimestre, custos_totais_trimestre, label = 'Custos/Trimestre')

plt.legend()

plt.grid(True)

plt.title('Gráfico do Custo total por Trimestre')
plt.show()