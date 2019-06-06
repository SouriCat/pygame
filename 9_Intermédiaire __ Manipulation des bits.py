a = bin(12)
print (a) # 0b dans la réponse veut dire que le nombre est en binaire

b = int('0b11001',2) # int(chiffre_binaire, base)
print (b)
print ("")

# BONUS --> Pour l'hexadecimal, c'est hex()
##################################################################
###             Manipulation des données en python             ###
#c    0001 0100 1111 1111
c = 0b1001010011111111
print ("Voici c :", bin(c))
#d    1000 0000 0100 1001
d = 0b1000000001001001
print ("Voici d :", bin(d))
print ("")


### ET BOOLEEN &
###--> Pour chaque colonne, si un les deux valeurs sont a 1, le resultat sera 1. Sinon, c'est 0.

result1 = c & d
print ("Le résultat du ET boolen est : ", bin(result1))

### OU BOOLEEN |
###--> Pour chaque colonne, s'il y a un 1 sur une des deux chaines, le résultat sera 1. Si les 2 sont à 0, c'est 0

result2 = c | d
print ("Le résultat du OU boolen est : ", bin(result2))

### OU EXCLUSIF BOOLEEN ^
###--> Pour chaque colonne, si les deux chaines ont un nombre identique, c'est 0. S'ils sont différents, c'est 1
result3 = c ^ d
print ("Le résultat du OU EXCLUSIF boolen est : ", bin(result3))

### LES DECALAGES
###--> Déplace tous les bits vers la gauche ou vers la droite

result4 = c >> 4
print ("Les bits ont été décalé vers la droite : ", bin(result4))
result5 = d << 2
print ("Les bits ont été décalé vers la dgauche : ", bin(result5))

### Le complément
###--> Tous les bits 0 passent a 1, et tous les bits 1 passent a 0.

result6 = ~c
print ("Les bits ont été inversés : ", bin(result6))

# http://izeunetit.fr/ISN/binaire_python.php
# http://public.iutenligne.net/informatique/algorithme-et-programmation/priou/LangageC/47_oprateurs_de_manipulation_de_bits__masques_et_bit__bit_dcalage.html
