

# https://towardsdatascience.com/data-visualisation-with-matplotlib-13aaf4787b30


import matplotlib.pyplot as plt
import numpy as np
import math



x = np.linspace(0,10,100)

plt.title(r"$\mathrm{sin}(x) \ vs\  \mathrm{sin}(\frac{x}{2})$")
plt.plot(x, np.sin(x), color = 'blue', label= "sin(x)")
plt.plot(x, np.sin(x/2), color = '#FFA500', label=r"$\mathrm{sin}(\frac{x}{2})$")
plt.grid(alpha = 0.4, linestyle = '--')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()

plt.axvspan(2, 6, facecolor='red', alpha=0.3) #highlight along x-axis
plt.axhspan(0.75, 1, facecolor='blue', alpha=0.3) #highlight along y-axis

plt.savefig("figure3.png")
plt.show()