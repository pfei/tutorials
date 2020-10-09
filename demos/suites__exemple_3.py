# http://mathaoutils.blogspot.com/2017/10/code-en-python-suite-recurrente.html

# on importe tout d'abord la librairie de maths
# le "as np" permet d'appeler une fonction de numpy en écrivant np seulement
# par exemple np.sin est pour le sinus
import numpy as np

# on importe la librairie de dessin
import matplotlib.pyplot as plt


# on définit notre fonction f
def f(x):
    return np.cos(x)


# on définit la suite u, ce sera un "array", u[0]=1.4 pour le moment
u = [1.4]
# on définit le nombre de point de récurrence
n = 10

# on calcule maintenant les n itérations de la suite avec une boucle
# attention range(0,n) va de 0 à n-1.
for i in range(0, n):
    # les boucles les if et le reste sont fait avec des retraits (un tab)
    # avec u.append, on ajoute à l'array u un nouvel élément.
    # au premier tour on a u[1] qui est donné par f(u[0])
    # plus généralement, la commande u[i] va bien donner le i-ème terme de la suite
    u.append(f(u[i]))

    # on imprime les termes au fur et à mesure. Le vert est du texte et le noir
    # est de la donnée
    print('u[', i, ']=', u[i])

# on définit les points d'abcisses qui vont servir pour tracer les fonctions
# on va de 0 à pi/2 (le np.pi appelle pi qui est dans la librairie numpy)
# et 0.01 est le pas
x = np.arange(0, np.pi / 2, 0.01)

# on trace x-> f(x) en b pour blue et - pour le choix du trait
# puis on trace x->x en r pour red et - pour le choix du trait
# en changeant le pas on rend le tracer de la fonction plus ou moins linéraire par morceaux
plt.plot(x, f(x), 'b-', x, x, 'r-')

# Ici on fait des axes jolis
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# on trace maintenant les traits: noir k correspond à black
for i in range(0, n - 1):
    plt.plot([u[i], u[i + 1]], [u[i + 1], u[i + 1]], 'k-')
    plt.plot([u[i + 1], u[i + 1]], [u[i + 1], u[i + 2]], 'k-')
    # dans la ligne suivante, on trace une ligne entre
    # (u[i],0) et u[i, u[i+1]]. Les "x" sont tous dans le premier crochet
    # et les "y" dans le deuxième
    # on met -- pour avoir un trait en pointillé
    plt.plot([u[i], u[i]], [0, u[i + 1]], 'k--')

# il manque le dernier trait alors on le rajoute à la main
plt.plot([u[n - 1], u[n - 1]], [0, u[n]], 'k--')

# on rajoute des commentaires sur le graphe
plt.annotate(
    '$u_0$',
    xy=(u[0], 0),
    xytext=(u[0] + .1, .1),
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

plt.annotate(
    '$u_1$',
    xy=(u[1], 0),
    xytext=(u[1] + .1, .1),
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

# on met un titre, on peut taper en latex!
plt.title('exemple de $u_{n+1}=f(u_n)$\n ici $u_{n+1}= \cos (u_n)$ avec $u_0 = 1.4$')

# on affiche le dessin
plt.show()
