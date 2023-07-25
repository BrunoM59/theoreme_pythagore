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

print(f"la premiere mesure est de {premiere_mesure} cm et la seconde mesure est de {seconde_mesure} cm")


# maintenant que j'ai mes deux mesures connues , je vais devoir les convertir en carré 

carre_premiere_mesure=premiere_mesure*premiere_mesure

carre_seconde_mesure=seconde_mesure*seconde_mesure

carre_troisieme_mesure=carre_premiere_mesure+carre_seconde_mesure

print(f"la premiere mesure {premiere_mesure} cm au carre est egale à {carre_premiere_mesure} et la seconde mesure {seconde_mesure} cm au carre est egale a {carre_seconde_mesure} ")
print(f"le carré de {premiere_mesure} est : {premiere_mesure}X{premiere_mesure} est egale à {premiere_mesure*premiere_mesure}")
print(f"le carré de {seconde_mesure} est : {seconde_mesure}X{seconde_mesure} est egale à {seconde_mesure*seconde_mesure}")

troisieme_mesure=carre_premiere_mesure+carre_seconde_mesure
print(f"la troisieme mesure est {troisieme_mesure} cm car {carre_premiere_mesure} + {carre_seconde_mesure} est egale a {carre_premiere_mesure+carre_seconde_mesure} cm" )

resultat_hypothenuse=math.sqrt(troisieme_mesure)
resultat_hypothenuse=int(resultat_hypothenuse)
print(f"le resultat de l'hypothenuse est de {round(resultat_hypothenuse)} cm , car la racine carre de {carre_troisieme_mesure} est {resultat_hypothenuse}")

addition_carre_premiere_and_seconde_mesure=carre_premiere_mesure+carre_seconde_mesure

if carre_troisieme_mesure != addition_carre_premiere_and_seconde_mesure:
    print("desolé votre triangle n'est pas un triangle rectangle")
else:
    print("Votre triangle est bien un triangle rectangle")
    print("la somme du carré de l'hypoténuse est égal à la somme des carrés des deux autres côtés ")
    print(f"La somme du carré de {resultat_hypothenuse} est égale a la somme de {carre_premiere_mesure} + {carre_seconde_mesure}")

 