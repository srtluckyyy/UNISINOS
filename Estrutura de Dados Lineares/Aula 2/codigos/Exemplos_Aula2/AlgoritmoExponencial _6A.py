# Função recursiva para calcular o n-ésimo número de Fibonacci
def fibonacci(n):
    # Base da recursão: os primeiros dois números de Fibonacci são 0 e 1.
    if n <= 1:
        return n
    # Chamada recursiva que segue a definição de Fibonacci: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Exemplo: Calcular o Fibonacci de 5 com explicações passo a passo

# Etapa 1: Chamada fibonacci(5)
# Como 5 > 1, a função faz as chamadas recursivas fibonacci(4) e fibonacci(3)
resultado_f5 = fibonacci(5)  # A função retornará o resultado de F(5)

# Etapa 2: Chamada fibonacci(4)
# Como 4 > 1, a função faz as chamadas recursivas fibonacci(3) e fibonacci(2)

# Etapa 3: Chamada fibonacci(3)
# Como 3 > 1, a função faz as chamadas recursivas fibonacci(2) e fibonacci(1)

# Etapa 4: Chamada fibonacci(2)
# Como 2 > 1, a função faz as chamadas recursivas fibonacci(1) e fibonacci(0)
# Retorna: fibonacci(2) = fibonacci(1) + fibonacci(0) = 1 + 0 = 1

# Etapa 5: Chamada fibonacci(1)
# Como 1 <= 1, a função retorna 1 diretamente
# Agora, temos: F(2) = 1

# Etapa 6: Chamada fibonacci(0)
# Como 0 <= 1, a função retorna 0 diretamente
# Agora, temos: F(1) = 1 e F(0) = 0

# Etapa 7: Chamada fibonacci(3) - segunda parte
# Com F(2) = 1 e F(1) = 1, temos: F(3) = F(2) + F(1) = 1 + 1 = 2

# Etapa 8: Chamada fibonacci(4) - segunda parte
# Com F(3) = 2 e F(2) = 1, temos: F(4) = F(3) + F(2) = 2 + 1 = 3

# Etapa 9: Chamada fibonacci(5)
# Com F(4) = 3 e F(3) = 2, temos: F(5) = F(4) + F(3) = 3 + 2 = 5

print("Resultado de Fibonacci de 5:", resultado_f5)  # Exibe o resultado final, que é 5

"""
A árvore de chamadas recursivas para calcular 𝐹(5)
 
F(5)
│
├─ F(4)
│  ├─ F(3)
│  │  ├─ F(2)
│  │  │  ├─ F(1) = 1
│  │  │  └─ F(0) = 0
│  │  └─ F(1) = 1
│  └─ F(2)
│     ├─ F(1) = 1
│     └─ F(0) = 0
└─ F(3)
   ├─ F(2)
   │  ├─ F(1) = 1
   │  └─ F(0) = 0
   └─ F(1) = 1

"""
