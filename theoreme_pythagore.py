import math

""" Pour calculer la mesure de l'hypotenuse avec Pythagore on a besoin
de connaitre les deux cotés de l'angle droit """

"""Soit un triangle [ABC] , triangle rectangle en A, l'hypotenuse est le coté opposer a l'angle droit """

"""si triangle ABC rectangle en A, les mesures connues sont le plus souvent sont """

"""[AB] et [AC] donc mesure a trouver a [BC]"""

# j'ai besoin d'avoir la premiere mesure
premiere_mesure=int(input("Quelle est la premiere mesure ? :"))

# j'ai également besoin d'avoir une seconde mesure
seconde_mesure=int(input("Quelle est la seconde mesure ? :"))

print(f"la premiere mesure est de {premiere_mesure} et la seconde mesure est de {seconde_mesure}")

# maintenant que j'ai mes deux mesures connues , je vais devoir les convertir en carré 

carre_premiere_mesure=premiere_mesure*premiere_mesure

carre_seconde_mesure=seconde_mesure*seconde_mesure

print(f"la premiere mesure {premiere_mesure} au carre est egale à {carre_premiere_mesure} et la seconde mesure {seconde_mesure} au carre est egale a {carre_seconde_mesure} ")

troisieme_mesure=carre_premiere_mesure+carre_seconde_mesure
print(f"la troisieme mesure est {troisieme_mesure} car {carre_premiere_mesure} + {carre_seconde_mesure} est egale a {carre_premiere_mesure+carre_seconde_mesure}" )

resultat_hypothenuse=math.sqrt(troisieme_mesure)
print(f"le resultat de l'hypothenuse est {round(resultat_hypothenuse)}")

