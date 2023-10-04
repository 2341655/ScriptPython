#Écrire un programme qui va demander à l'utilisateur deux nombres, et lui retourner la somme et le produit des deux nombres

nombre = int(input("Veuillez entrer un premier nombre : "))

nombre2 = int(input("Veuillez entrer un deuxieme nombre : "))

sommeNombre = nombre + nombre2
produitNombre= nombre * nombre2
print("La somme est : " + str (sommeNombre))
print("Le produit est : " + str (produitNombre))

print("La somme est : " , sommeNombre)
print("Le produit est : " , produitNombre)

print("La somme est : " , nombre+nombre2)
print("Le produit est : " , nombre*nombre2)