## Les tuples est une variable qui a plusieurs valeurs.
## Elle s'appelle comme un tableau. Elle n'est pas modifiable


#---> Création d'un tuple
tuple1 = (5, 10, 15, 20, 25)
print (type(tuple1))

#---> Utilisation d'un tuple
variable_tuple = tuple1[2]
##tuple1[2] += 1
##TypeError: 'tuple' object does not support item assignment
variable_tuple += 1
print (variable_tuple)
