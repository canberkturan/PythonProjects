#!usr/bin/python3
#-*-coding:utf-8;-*-
import imza
imza.imza("Canberk Turan","Roma Rakamları")
rakamlar={0:'',
	  1:'I',
          5:'V',
          10:'X',
          50:'L',
          100:'C',
          500:'D',
          1000:'M'}
sayi={0:(0,0),
	     1:(1,0),
      2:(1,1),
      3:(1,1,1),
	     4:(1,5),
      5:(5,0),
      6:(5,1),
      7:(5,1,1),
      8:(5,1,1,1),
      9:(1,10)}
def parcala(n):
    liste=[]
    for i in str(n):
        liste.append(int(i))
    for j in liste:
        liste[liste.index(j)]=sayi[j]
    return liste
def donusum(n):
    sayi=''
    if n==4000:
        return "MMMM"
    elif n>4000 or n<1:
        print("Aralık Dışı")
        return
    else:
        for i in range(0,len(parcala(n))):
            a=''
            for j in parcala(n)[i]:
                a+=rakamlar[(10**(len(parcala(n))-i-1))*j]
            sayi+=a
    return sayi
n=int(input("Dönüştürmek istediğiniz sayı: "))
print(donusum(n))
