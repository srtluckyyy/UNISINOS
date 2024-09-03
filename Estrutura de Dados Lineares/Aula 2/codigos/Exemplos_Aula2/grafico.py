# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 2:23:45 2024
@author: vinic
"""

import time
import math
import numpy as np
import matplotlib.pyplot as plt

# Define a quantidade de elementos, ajustando para uma escala menor
n = np.arange(1, 21)  # Tamanho de entrada limitado a 20 para o gráfico fatorial e exponencial

# Funções representando diferentes complexidades
O_1 = np.ones_like(n)  # O(1) - Constante
O_log_n = np.log2(n)  # O(log n) - Logarítmico
O_n = n  # O(n) - Linear
O_n_log_n = n * np.log2(n)  # O(n log n) - Linearítmico
O_n2 = n ** 2  # O(n²) - Quadrático
O_2n = 2 ** n  # O(2^n) - Exponencial
O_fatorial = [math.factorial(x) for x in n]  # O(n!) - Fatorial
O_sqrt_n = np.sqrt(n)  # O(√n) - Sublinear
O_log_log_n = np.log2(np.log2(n + 1))  # O(log log n) - Logaritmo Duplo
O_log_n2 = np.log2(n) ** 2  # O(log(n)^2) - Polilogaritmo

# Define o gráfico
plt.figure(figsize=(10, 8))

# Plotando cada complexidade
plt.plot(n, O_1, label="O(1) - Constante", color='blue', linestyle='-')
plt.plot(n, O_log_n, label="O(log n) - Logarítmico", color='green', linestyle='--')
plt.plot(n, O_n, label="O(n) - Linear", color='orange', linestyle='-.')
plt.plot(n, O_n_log_n, label="O(n log n) - Linearítmico", color='red', linestyle=':')
plt.plot(n, O_n2, label="O(n²) - Quadrático", color='purple', linestyle='-')
plt.plot(n, O_sqrt_n, label="O(√n) - Sublinear", color='cyan', linestyle='--')
plt.plot(n, O_log_log_n, label="O(log log n) - Logaritmo Duplo", color='magenta', linestyle='-.')
plt.plot(n, O_2n, label="O(2^n) - Exponencial", color='black', linestyle='--')
plt.plot(n, O_fatorial, label="O(n!) - Fatorial", color='brown', linestyle=':')
plt.plot(n, O_log_n2, label="O(log(n)^2) - Polilogaritmo", color='pink', linestyle='-.')

# Configuração do gráfico
plt.ylim(0, 1000)  # Ajusta o limite do eixo y para evitar que o fatorial e exponencial dominem o gráfico
plt.title('Gráfico Comparativo de Complexidades')
plt.xlabel('Tamanho da Entrada (n)')
plt.ylabel('Número de Operações')
plt.legend(loc='upper left')

# Exibe o gráfico
plt.grid(True)
plt.show()
