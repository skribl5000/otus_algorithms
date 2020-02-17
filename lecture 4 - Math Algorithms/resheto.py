# решето эратосфена - возвращает dict с пометкой простое(True) или нет(False) число
def eratosfen(n):
    resheto = {}
    for m in range(1,n+1):
        resheto[m] = True
    for m in range(2,n+1):
        for i in range(m*m, n+1, m):
            resheto[i] = False
    return resheto

print(eratosfen(100500))
