cores = ['vermelho', 'preto', 'laranja']
print("\n\n", cores)

cores.append("amarelo")
print("\n\n append", cores)

cores.insert(2, "azul") 
print("\n\n insert", cores)

cores.pop(3)
print("\n\n pop3", cores)

cores.remove("preto")
print("\n\n remove", cores)

coresExtra = ['amarelo', 'preto', 'laranja']
cores.extend(coresExtra)
print("\n\n extend", cores)

for x in cores: 
    print(x)