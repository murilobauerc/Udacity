from random import randint

vetor = [randint(1,100) for x in range(10)]
# gera um lista com numeros aleatorios

def meuQuickSort(lista):
    if not lista:
        return []
    menores = meuQuickSort([x for x in lista if x < lista[0]])
    iguais = [x for x in lista if x == lista[0]]
    maiores = meuQuickSort([x for x in lista if x > lista[0]])

    return menores + iguais + maiores

print(meuQuickSort(vetor))