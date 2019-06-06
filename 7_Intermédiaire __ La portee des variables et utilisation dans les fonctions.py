## Fonctionnement normal d'une fonction et des variables
##--> la variable locale est Dispo dans tous le documents, mais les fonctions doivent l'avoir en parametre pour l'utiliser
var1 = "parametre1"
var2 = "parametre2"


def fonction(parametre1, parametre2):
    print (parametre1, "a bien été passé dans la fonction")
    print (parametre2, "a bien été passé dans la fonction")
    
    variable_locale = parametre1 + parametre2
    return variable_locale

retour_de_la_variable_locale = fonction(var1, var2)


print ()
##--> La portée des variables. Certaines variables peuvent être disponible dans tout le document : les tableaux, les var globale et les tuples

    # La fausse variable locale
variable_locale_racine =  "variable simple "
    # Le tableau naturellement global
tableau = [10,10,10]
    # Les tuples sont des variables globales que l'on ne peut modifier 
tuple1 = (10, 20, 30, 40) 

def fonction_2():
    # Variables superglobales
    global variable_locale_racine     # Va chercher la variable dans les fonctions parentes, sans qu'elle passe par les paramètres
    variable_locale_racine += " avec un texte ajouté avec la fonction -fonction-"

    # Le tableau est utilisable partout. Une modif ici affecte l'ensemble
    tableau[0] += 5

    # Utilisation des tuples. 
    variable_tuple = tuple1[2]
    variable_tuple += 1
    print ("tuple", variable_tuple)
    
fonction_2()

print (variable_locale_racine)
print (tableau)
