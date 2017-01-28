#!usr/bin/python3
#-*-coding:utf8;-*-
def sqrt(x):
    if x<0:
        return "Negatif Sayıların Karekökü Alınamaz"
    elif x==0:
        return 0.0
    n=1
    for i in range(10000):
         n=(x/n+n)/2
    return n
def main():
    a=int(input("Karekökü Alınacak Sayı: "))
    print(sqrt(a))
if __name__=="__main__":
    main()
