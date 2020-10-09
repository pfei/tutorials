
# (sans représentation graphique) 

import numpy as np

def f(x):
    return np.cos(x)

u = [1.4]
n = 10

for i in range(0, n):
    u.append(f(u[i]))
    print('u[', i, ']=', u[i])