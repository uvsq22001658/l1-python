def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """


    suite = []
    while n != 1 :    
        if n % 2 == 0 :
            n = n // 2
        else:
            n = 3 * n + 1
        suite.append(n)


    return(suite)


print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(2, n_max) :
        syracuse(i)


    return(True)


print(testeConjecture(10000))