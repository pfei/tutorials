
# https://www.codingame.com/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/suites-numeriques

# https://matplotlib.org/3.1.1/tutorials/introductory/pyplot.html

import matplotlib.pyplot as plt
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()