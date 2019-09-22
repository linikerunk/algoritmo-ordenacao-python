
# Metodos O(n²) - Aleatorios

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2100000, 500000)

y = [10, 70, 300, 2180, 10326]
y1 = [5, 16, 87, 488, 2076]
y2 = [4, 16, 70, 627, 2578]

plt.plot(x, y, label='Bubble Sort')
plt.plot(x, y1, label='Selection Sort')
plt.plot(x, y2, label='Insertion Sort')

plt.xlabel('Quantidade de Elementos')
plt.ylabel('Tempo (Segundos)')

plt.title("Ordem complexidade O(n²) \n \
    Ordenações com valores aleatórios")

plt.legend()

plt.show()

# Metodos Log(n log) - Aleatorios

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2100000, 500000)

y = [0.04, 0.09, 0.18, 0.50, 1.10]
y1 = [7.7, 26.22, 105, 646, 2661.1]
y2 = [0.05, 0.08, 0.15, 0.32, 0.68]

plt.plot(x, y, label='ShellSort')
plt.plot(x, y1, label='Merge Sort')
plt.plot(x, y2, label='QuickSort')

plt.xlabel('Quantidade de Elementos')
plt.ylabel('Tempo (Segundos)')

plt.title("Ordem complexidade Log(n log) \n \
    Ordenações com valores aleatórios")

plt.legend()

plt.show()


# Metodos O(n²) - Ordenados

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2100000, 500000)

y = [0.28, 0.44, 0.34, 0.58, 0.62]
y1 = [4.18, 7.34, 33.57, 214.77, 1145]
y2 = [0.22, 0.54, 0.70, 0.70, 0.60]

plt.plot(x, y, label='Bubble Sort')
plt.plot(x, y1, label='Selection Sort')
plt.plot(x, y2, label='Insertion Sort')

plt.xlabel('Quantidade de Elementos')
plt.ylabel('Tempo (Segundos)')

plt.title("Ordem complexidade O(n²) \n \
    Ordenações com valores Ordenados")

plt.legend()

plt.show()

# Metodos Log(n log) - Ordenados

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2100000, 500000)

y = [0.01, 0.03, 0.03, 0.04, 0.06]
y1 = [7.5, 25.60, 102.2, 241.9, 3500]
y2 = [0.02, 0.03, 0.06, 0.11, 0.19]

plt.plot(x, y, label='ShellSort')
plt.plot(x, y1, label='Merge Sort')
plt.plot(x, y2, label='QuickSort')

plt.xlabel('Quantidade de Elementos')
plt.ylabel('Tempo (Segundos)')

plt.title("Ordem complexidade Log(n log) \n \
    Ordenações com valores Ordenados")

plt.legend()

plt.show()


# Metodos O(n²) - Inversamente Ordenados

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2100000, 500000)

y = [9.2, 40.23, 200.47, 1073.6, 5679.6]
y1 = [5.09, 19.26, 85.09, 1169.20, 5526.80]
y2 = [5.08, 18.44, 117.07, 818.67, 2664.85]

plt.plot(x, y, label='Bubble Sort')
plt.plot(x, y1, label='Selection Sort')
plt.plot(x, y2, label='Insertion Sort')

plt.xlabel('Quantidade de Elementos')
plt.ylabel('Tempo (Segundos)')

plt.title("Ordem complexidade O(n²) \n \
    Ordenações com valores Inversamente Ordenados")

plt.legend()

plt.show()

# Metodos Log(n log) - Inversamente Ordenados

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2100000, 500000)

y = [0.02, 0.04, 0.07, 0.13, 0.25]
y1 = [7, 26.2, 102.48, 284.3, 3541]
y2 = [0.02, 0.05, 0.06, 0.11, 0.27]

plt.plot(x, y, label='ShellSort')
plt.plot(x, y1, label='Merge Sort')
plt.plot(x, y2, label='QuickSort')

plt.xlabel('Quantidade de Elementos')
plt.ylabel('Tempo (Segundos)')

plt.title("Ordem complexidade Log(n log) \n \
    Ordenações com valores Inversamente Ordenados")

plt.legend()

plt.show()



