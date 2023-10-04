# Écrire un programme qui va trouver le plus grand nombre parmi 3 nombres saisis a partir du clavier

a= input("veullez entrer permier nombre\n")
b= input("veullez entrer 2eme nombre \n")
c= input("veullez entrer permier nombre\n")

if a>b and a>c :
     print( "le plus grand nombre est " ,a)
elif b>c:
     print("le plus grand nombre est " ,b)
else:
    print("le plus grand nombre est " ,c)
