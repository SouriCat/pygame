##-->Creation 
tableau = ["index_0", "index_1", "index_2", "index_3", "index_4", "index_5"]
dix_zeros_dans_un_tableau = [0]*10

##-->Utilisation 
element_du_tableau = tableau[0]
print (element_du_tableau)


##-->Tableau a deux dimensions 
sur_tableau = [ [0, 1, 2, 3],  #sous-tableau 1
                [4, 5, 6, "piège"] ] #sous-tableau 2

sous_tableau_1 = tableau[0]
sous_tableau_2 = tableau[1]

element = tableau[0][1]
element = tableau[1][2]
element = tableau[1][4]

sur_tableau.append("sous-tableau 3")



## Bonus facultatif
# Obtenir la taille d'un tableau
len(tableau)
# affiche tous les indexs compris entre le 1er et le 3eme. Le 3eme étant exclu 
print (tableau[1:3]) 
# Creation d'une liste de chiffres
range(0,4)
# Rassemblement de tableau
super_tableau = sous_tableau_1 + sous_tableau_2
