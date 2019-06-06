#coaching ---> Si tu n'es pas sur d'avoir compris = reformule ce que j'ai dit

####### algorithme
#-->  Un algorithme est une suite finie et non ambiguë d'opérations ou d'instructions permettant de résoudre une classe de problèmes



######### L'affectation
#--> C'est le fait de donner une valeur a une variable
# Ca peut symboliser de cette facon
#  chinois  <----- "chinois"
chinois = "chinois"
francais = russe = "Gerard Depardieu"

####### constante
#--> Variable qui a toujours la meme valeur
chinois = "chinois"

####### variable
#--> Variable qui peut changer de valeur
amis_du_voyageur = "chinois"
amis_du_voyageur = "américain"
amis_du_voyageur = "Westerossien" # RIP Daeneris



####### Afficher du texte et des variables a l'écran
#--> les print
print("")
print(amis_du_voyageur)
print("amis_du_voyageur")
print("Le voyageur a été avec des ", amis_du_voyageur )

##print('We are the {0} who say "{1}!"'.format('knights', 'Ni'))
##We are the knights who say "Ni!"

##animals = 'eels'
##print(f'My hovercraft is full of {animals}.')
##My hovercraft is full of eels.

# Ou print 

## Demander a l'utilisateur d'entrée une valeur
#--> l'input
#valeur_utilisateur = input()



print("")
print("")
####### expression conditionnelle et plus généralement booléenne…
qui_est_a_la_porte = "le chien du voisin"
if qui_est_a_la_porte == "le chien du voisin" :
    print ("OK, rentre le chien")
if qui_est_a_la_porte != "le chien du voisin" :
    print ("Les chiens ne sont pas autorisés à la maison")
    
ton_mec = True
if ton_mec == True :
    print ("OK, rentre")
if ton_mec :
    print ("OK, rentre")
# Si on est pas sur de la condition, on vérifie avec un message du genre   
    print ("Test_1 réussi")



print("")
print("")
##L'affectation récursive
#--> C'est le fait de donner changer la valeur d'une variable pour sortir d'une boucle
le_chien_du_voisin_parle = True
i = 0
while le_chien_du_voisin_parle :
    i = i + 1
    print (le_chien_du_voisin_parle)
    if i == 10:
        le_chien_du_voisin_parle = False





print("")
print("")
####### identifiant
#--> C'est le titre d'une fonction/procédure

####### fonction                                                 -- A pratiquer
#--> renvoit une valeur
def ou_est_drogon():
    position_de_drogon = "Meereen"
    
    return position_de_drogon

return_de_la_fonction = ou_est_drogon()
print ("Drogon est a", return_de_la_fonction)

####### procédure
#--> ne renvoit pas de valeur
def ou_est_drogon():
    print ("Selon les experts et les bergers en colère, Drogon est a Meereen")   
ou_est_drogon()






print("")
print("")
####### modularité
#--> Découper son code en petit bouts qui peuvent être réutilisés. Ils doivent être mis avant la fonction qui les appelle. 
def pot_casse_1():
    print ("Le pot casse 2 ment")
def pot_casse_2():
    print ("Le pot casse 1 dis la vérité")
    
def Le_rassembleur_de_pot_casse():
    pot_casse_1()
    pot_casse_2()
    
Le_rassembleur_de_pot_casse()

##finitude
#--> Donner un fin a des boucles _for et _while_ et aux fonctions qui s'appellent elles-meme

