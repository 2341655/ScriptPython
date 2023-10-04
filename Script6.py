#Écrire un programme qui va lire les données d'un employé à partir du clavier
#identifiant, nom, salaire, adresse, marié

identifiant = int(input("Veuillez entrer votre identifiant : "))
nom = input("Veuillez entrer votre nom : ")
salaire = float(input("Veuillez entrer votre salaire : "))
adresse = input("Veuillez entrer votre adresse : ")
status = bool(input("Etes vous marié ? [True|False]"))

print("Le nom de l'employé est : ", nom)
print("Le Id de l'employé est : ", identifiant)
print("Le salaire de l'employé est : ", salaire)
print("L'adresse de l'employé est : ", adresse)
print("est ce que l'employé est marié : ", status)