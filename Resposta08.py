# Sequência a)
def sequencia_a():
    sequencia = [1, 3, 5, 7]
    proximo = sequencia[-1] + 2
    sequencia.append(proximo)
    return sequencia

# Sequência b)
def sequencia_b():
    sequencia = [2, 4, 8, 16, 32, 64]
    proximo = sequencia[-1] * 2
    sequencia.append(proximo)
    return sequencia

# Sequência c)
def sequencia_c():
    sequencia = [0, 1, 4, 9, 16, 25, 36]
    proximo = (len(sequencia)) ** 2
    sequencia.append(proximo)
    return sequencia

# Sequência d)
def sequencia_d():
    sequencia = [4, 16, 36, 64]
    proximo = (len(sequencia) * 2) ** 2
    sequencia.append(proximo)
    return sequencia

# Sequência e)
def sequencia_e():
    sequencia = [1, 1, 2, 3, 5, 8]
    proximo = sequencia[-1] + sequencia[-2]
    sequencia.append(proximo)
    return sequencia

# Sequência f)
def sequencia_f():
    sequencia = [2, 10, 12, 16, 17, 18, 19]
    proximo = sequencia[-1] + 1
    sequencia.append(proximo)
    return sequencia

# Imprimindo os resultados
print("Sequência a):", sequencia_a())
print("Sequência b):", sequencia_b())
print("Sequência c):", sequencia_c())
print("Sequência d):", sequencia_d())
print("Sequência e):", sequencia_e())
print("Sequência f):", sequencia_f())
