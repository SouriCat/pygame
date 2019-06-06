
tableau_chiffre = ["un", "sept", "huit", "deux", "quatre", "zero", "cinq", "six", "trois", "neuf"]
tableau_a_2_niveau = [0, 1, 2, 3,  4,  5]


## On utilise la boucle WHILE pour chercher une valeur.
## Dès qu'elle est trouvée, on sort de la boucle
i = 0
while tableau_chiffre[i] != "sept":
    print ("Ce chiffre n'est pas --sept--", tableau_chiffre[i])
    i += 1



## On utilise for pour parcourir plusieurs variables.
## Le parcours s'arrete une fois que toutes les variables ont été passées
## /!\ Supprimer une valeur lors d'un parcours causera un décalage d'index et donc erreur. Pour la corriger, il faut enlever un index apres la suppression.
for ligne in tableau_a_2_niveau:
    print (ligne)
    if ligne == 4 :
        print ("Cette valeur correspond a 4")
    

