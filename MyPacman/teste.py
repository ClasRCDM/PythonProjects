import numpy as np

m = []
Resultado = 0

for y in range(5):
    linha = []
    for x in range(5):
        linha.append(2)
    m.append(linha)

print(np.matrix(m))

for a in range(5):
    Resultado += m[a][a+1]
print(Resultado)
