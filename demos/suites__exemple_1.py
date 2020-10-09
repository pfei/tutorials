
import matplotlib.pyplot as plt
import numpy as np

# tracé de la suite
x = list(range(15))
print(x)
y1 = np.sin(x)
print(y1)
plt.plot(x, y1, 'bo')
# y2 = [np.sin(e/2) for e in x] 
# plt.plot(x, y2, 'ro')


# tracé de la fonction sinus
x = np.linspace(0,14,100)
plt.plot(x, np.sin(x), '--',  color = 'pink', label= "sin(x)")


plt.grid(alpha = 0.4, linestyle = '--')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.title('$u_n = \sin (n)$')
# plt.savefig("figure1.png")
plt.show()