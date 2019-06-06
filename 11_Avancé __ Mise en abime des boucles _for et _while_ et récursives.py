# L'indentation est ultra importante pour ne pas se perdre entre les 2 boucles

tableau_chiffre = ["un", "sept", "huit", "deux", "quatre", "zero", "cinq", "six", "trois", "neuf"]
tableau_a_2_niveau = [[0, 1, 2, 3,  4,  5],
                      [6, 7, 8, 9, 10, 11]]
i = 0
while tableau_chiffre[i] != "sept":
    print ("Ce chiffre n'est pas --sept--", tableau_chiffre[i])
    #||||||||||||||||||||||||||||||||||||||
    j = 0
    while tableau_chiffre[j] != "quatre":
        print ("Ce chiffre n'est pas --quatre--", tableau_chiffre[j])
        j += 1       
    #||||||||||||||||||||||||||||||||||||||
    i += 1


for ligne in tableau_a_2_niveau:
    print (ligne)
    #||||||||||||||||||||||||||||||||||||||
    for index in ligne:
        print (index)
    #||||||||||||||||||||||||||||||||||||||
    print ()


# Une fonction recursive a toujours un parametre appellé (ou une variable globale).
# Il/Elle permet d'arreter la recursivité.

def recursive(parametre_1):
    if parametre_1 > 0:
#        print (parametre_1)
        recursive(parametre_1 - 1)
#        print (parametre_1)

recursive(10)
