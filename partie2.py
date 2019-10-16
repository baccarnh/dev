## ex1: True ou false?.
var1=input("entrer variable1")
var2=input("entrer variable2")
longueur_var1= len (var1)
longueur_var2= len (var2)
if longueur_var1==0 and longueur_var2==0:
    print("true")
else: print("false")

## ex2: calculer mon ãge
annéeactu= int(input("donner l'année actuelle"))
votreannée=int(input("votre année de naissance"))
votre_age=annéeactu-votreannée
print("votre age est:", votre_age)
annéeami=int(input("l'année de naissance de votre ami"))
age_ami=annéeactu-annéeami
print("la somme de vos deux ages est:",votre_age+age_ami)

##ex3: Problème de chaussures
prix1=70
prix2=59
prix3=20
achat=80*(prix1+prix2+prix3)/100
print("la somme des achats est:",achat, "euros")

##ex4: une calculatrice Python
nmb1=float(input("entrer un premier nombre"))
nmb2=float(input("entrer un premier nombre"))
somme=nmb2+nmb1
print("la somme est=",somme)

##ex5: travailler avec les propriétés
nom=input("entrer votre nom")
long_nom=len(nom)
lis_nom=list(nom)
i=long_nom-1
print((lis_nom[0].upper()), (lis_nom[i].upper()))

prenom=input("entrer votre prénom")
long_prenom=len(prenom)
lis_prenom=list(prenom)
i=long_prenom-1
print((lis_prenom[0].upper()), (lis_prenom[i].upper()))

print((lis_nom[0].upper()), (lis_nom[i].upper()),(lis_prenom[0].upper()), (lis_prenom[i].upper()))

age=input("donner votre age")
age1=(int(age)/33)
x=int(age1)
print(x)