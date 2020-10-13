
# on considère la suite 
# u_n = 1/0! + 1/1! + 1/2! + ... + 1/n!
# on a le résultat suivant (admis):
# quand n tend vers l'infini, u_n tend vers e (exponentielle(1))
# pour avoir e en python: math.exp(1)

# quelle est la tâche effectuée par la fonction `rang` ci dessous ?

import math

def rang(p):
    u = 1
    n = 0
    while abs(math.exp(1) - u) >= 10**(-p):
        n = n + 1
        u = u + 1 / math.factorial(n)
        print(u)
    return n

print(rang(10))


