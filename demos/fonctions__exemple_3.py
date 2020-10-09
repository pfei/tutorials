

# https://towardsdatascience.com/data-visualisation-with-matplotlib-13aaf4787b30


import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(0,10,100)

plt.figure(figsize=(10,10))

plt.title(r"$\mathrm{sin}(x) \ vs\  \mathrm{sin}(\frac{x}{2})$")
plt.plot(x, np.sin(x), color = 'blue', label= "sin(x)")
plt.plot(x, np.sin(x/2), color = '#FFA500', label=r"$\mathrm{sin}(\frac{x}{2})$")
plt.grid(alpha = 0.4, linestyle = '--')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()

plt.annotate('Point 1',xy=(0,0), xytext=(0,-0.25), arrowprops=dict(arrowstyle='->'))
plt.annotate("Point 2", xy=(2/3*math.pi,math.sin(2/3*math.pi)), xytext=(3,0.75), arrowprops=dict(facecolor="yellow",arrowstyle="-|>"),fontsize=16)
plt.annotate("Point 3", xy=(2*math.pi,math.sin(2*math.pi)), xytext=(7,0), arrowprops=dict(facecolor="r",arrowstyle="fancy"),fontsize=12)

plt.savefig("figure2.png")
plt.show()