#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import os
import time
pi=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596
def rad(derece):
    return derece*(pi/180)
def fact(n):
    fac=1
    for i in range(2,n+1):
        fac*=i
    return fac
def sin(x,rady=0,a=85):
    sine=0
    if rady==0 and x==360:
        x=0
    elif rady==0 and 180>=x>90:
        x=180-x        
    if rady==0:
        x=rad(x)
    for i in range(a):
        sine+=(((-1)**i)*(x**(2*i+1)))/fact(2*i+1)
    return "%.8f" % round(sine,8)
def cos(x,rady=0,a=85):
    cose=0
    if rady==0 and x==360:
        return 1.00000000
    elif x==90 or x==270:
        return 0.00000000
    if rady==0:
        x=rad(x)
    for i in range(a):
        cose+=(((-1)**i)*(x**(2*i)))/fact(2*i)
    return "%.8f" % round(cose,8)
def imza(a="Canberk Turan",b="Trigonemetri Hesaplayıcı"):
    print("#"*30)
    print("#"+" "*round((28-len(b))/2)+b+" "*(round((28-len(b))/2))+"#")
    print("#"+"  "+"Developer:"+a+"   "+"#")
    print("#"*30)
def main():
    imza()
    try:
        a=float(input("Lütfen Açıyı Derece Cinsinden Giriniz: "))
        if (float("%.2f" % round(a,2)).is_integer()):
            b=int(a)
            a=b
        else:
            b="%.2f" % round(a,2)
        a=a%360
        print("Açı      :",b)
        print("Sin({})  :".format(b),"%.8f" % round(float(sin(a)),8))
        print("Cos({})  :".format(b),"%.8f" % round(float(cos(a)),8))
        print("Tan({})  :".format(b),"%.8f" % round(float(sin(a))/float(cos(a)),8))
        print("Cot({})  :".format(b),"%.8f" % round(float(cos(a))/float(sin(a)),8))
        print("Sec({})  :".format(b),"%.8f" % round(1/float(cos(a)),8))
        print("Csc({})  :".format(b),"%.8f" % round(1/float(sin(a)),8))
    except ZeroDivisionError:
        if round(float(sin(a)),5)==0:
            print("Cot({})  :".format(a),"tanımsız")
            print("Sec({})  :".format(b),"%.8f" % round(1/float(cos(a)),8))
            print("Csc({})  :".format(b),"tanımsız")
        elif cos(a)==0:
            print("Tan({})  :".format(a),"tanımsız")
            print("Cot({})  :".format(a),"%.8f" % round(float(cos(a))/float(sin(a)),8))
            print("Sec({})  :".format(b),"tanımsız")
            print("Csc({})  :".format(b),"%.8f" % round(1/float(sin(a)),8))
    except ValueError:
        print("Hatalı Değer Girdiniz")
        print("Program Yeniden Başlatılıyor..")
        time.sleep(1.5)
        os.system('clear')
        print("Program Yeniden Başlatıldı")
        main()
        return 0
    sorgu=input("Tekrar?(E/H)")
    if sorgu.lower()==("e" or "evet" or "y" or "yes"):
        os.system('clear')
        print("Program Yeniden Başlatıldı!")
        main()
        return 0
    else:
        os.system('clear')
        print("Programı Kullandığınız İçin Teşekkürler")
        os.system('exit')
        
os.system('clear')
main()
    