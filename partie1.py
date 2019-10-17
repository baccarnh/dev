print("ex1: Hello World")
print("Hello World")

print ("ex1 avec variable")
message= "Hello World"
print(message)

print("ex2: calcul divers")
print(3*3)

try: 12/0
except ZeroDivisionError:
    print("erreur de division par0")
print(4+9+78)
print(12-7)
print(5e4)

print("ex3: communiquer avec l'ordinateur")
##print("inserer votre nom")
nom = input("entrer votre nom")
print("bienvenue", nom)

print("ex4: Nom et prénom")
nom= "BACCAR"
prénom= "Nour Elhouda"
print ("Bonjour ",nom, prénom)

print("ex5: des caractères au nombre")
myNumber= "123"
myNumber=(int(myNumber))
print(type(myNumber))

print("ex6: Majuscules et miniscules")
mavariable=input("donner votre chaine de caratères")
print(mavariable. upper())
print(mavariable. lower())