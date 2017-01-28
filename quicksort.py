#Kullanmak için dosyayı programınızla aynı klasöre indirip import ettikten sonra 
#quicksort.hizli(liste) şeklinde kullanmanız yeterli
#from quicksort import hizli şeklinde import etmeniz durumunda
#hizli(liste) şeklinde kullanabilirsiniz.
def hizli(liste):
    if len(liste)<=1:
        return liste
    ornek=liste[0]
    a1,a2,a3=[],[],[]
    for i in liste:
        if i<ornek:
            a1.append(i)
        elif i==ornek:
            a2.append(i)
        else:
            a3.append(i)
    return hizli(a1)+a2+hizli(a3)
