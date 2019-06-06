##### Manipulation des chaines de caractères

str1 = 'Bonjour'  # unicode 
str2 = "Bonjour"  # utf8


##---> L'echappement permet d'afficher des signes utilisés pour coder
#\' \"


##---> Retour chariot, a mettre a la fin de la ligne
#\n\
## retour chariot facile :
# str3 = """ texte sur
# plusieurs lignes """


##---> Concatenation de plusieurs chaines
str4 = "a"+"b"+"c"


##---> Repetition d'une chaine
str5 ="abc" * 3


##---> Imprime une partie de la chaine de caractères
str6 = "Langage : Python"
print (str6[2])        ##n
print (str6[0:2])      ##La
print (str6[:4] )      ##Lang
print (str6[4:] )      ##age : Python



##---> Modifier un chaine de caractère
print ()
# Les chaines de caractères ne sont pas modifiable directement -->TypeError: object doesn't support item assignment
# Il faut ruser avec cette methode
salut = 'bonjour à tous'
salut = 'B' + salut[1:]
print (salut)


##---> Cherche un caractère :
# Retourne False si "h" n'est pas dans str. S'il y est, affiche True
str7 = "Langage : Python"
print ("h" in str7)
# Cherche la lettre et renvoie son index
print (str7.index("h"))


##---> Cherche un mot ou plus dans la chaine de caractère :
foin = "Cette leçon vaut bien deux fromages, dont un fromage râpé ?"
aiguille = "fromage"
print (foin.rfind(aiguille))


##---> Minuscules ou Majuscules ?
print ()
# Minuscules
print (foin.lower())
# Majuscules
print (foin.upper())
# Premier caractere en majuscule
print (foin.capitalize())


##---> Remplacer un ou plusieurs caracteres
#replace(old, new)
phrase = "Si ce n'est toi c'est donc ton frère"
print (phrase.replace(" ","_"))
#Si_ce_n'est_toi_c'est_donc_ton_frère
