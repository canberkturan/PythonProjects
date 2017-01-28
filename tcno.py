#-*-coding:utf8;-*-
from imza import imza
imza("Canberk Turan","TC Kimlik No Algoritması")
def soniki(n):
    n=str(n)
    t=0
    s=0
    for i in range(1,10):
        if i%2==1:
            t+=int(n[i-1])
        else:
            s+=int(n[i-1])
    t=(t*7-s)%10
    s=0
    for i in n+str(t):
        s+=int(i)
    return str(t)+str(s%10)
def akraba(n,s):
    a=int(str(n)[:9])+29999*s
    return str(a)+soniki(a)
def main():
    print("Hangi işlemi yapmak istersiniz: ")
    print("(1)-Son iki hane kontrolü")
    print("(2)-Bir Önceki Kişinin TCKNO'su")
    print("(3)-Bir Sonraki Kişinin TCKNO'su")
    print("(4)-İstenilen sıradaki kişinin TCKNO'su")
    print("(5)-İstenilen Sayıda Kişi Listele")
    a=int(input("-->"))
    if a==1:
        s=int(input("Lütfen TCKNO ilk 9 hanesini giriniz: "))
        print(soniki(s))
        return
    elif a==2:
        tc=int(input("TCKNO: "))
        print(akraba(tc,1))
    elif a==3:
        tc=int(input("TCKNO: "))
        print(akraba(tc,-1))
    elif a==4:
        tc=int(input("TCKNO: "))
        sira=int(input("Sizin Sıra Numaranız: "))
        sira2=int(input("İstenilen Sıra no: "))
        print(akraba(tc,sira-sira2))
    elif a==5:
        tc=int(input("TCKNO: "))
        sayi=int(input("Kaç Kişi: "))
        yon=input("Öncekiler/Sonrakiler--(Ö/S)")
        if yon.lower()=='ö':        	    
            i=0
            while i<sayi:
                print(i,akraba(tc,i),sep='--')
                i+=1
        else:
            i=0
            while i>-sayi:
                print(i,akraba(tc,i),sep='--')
                i-=1
if __name__=="__main__":
    main()