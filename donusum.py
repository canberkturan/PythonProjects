#!usr/bin/python3
#-*-coding:utf-8;-*-
import imza
__author__ = "Canberk Turan"

birler=['',"bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"," "]
onlar=['',"on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
katlar=["katrilyon","trilyon","milyar","milyon","bin"," "]
yuzler=[i+"yüz" for i in birler if i!='bir']
def donusum(n):
    isaret=''
    if n==0:
        return "sıfır"
    elif n<0:
        isaret='eksi '
        n=-n
    i=-1
    uclu=[]
    n="{:,}".format(int(n))
    uclu=n.split(",")
    for j in uclu:
        a=int(j)
        if j=='000':
            uclu[uclu.index(j)]='x'
        elif j=='00{:d}'.format(a):
            uclu[uclu.index(j)]=str(a)
        elif j=='0{}'.format(str(a)):
            uclu[uclu.index(j)]=str(a)
    for i in range(len(uclu)-1,-1,-1):
        uclu.insert(-i,katlar[-i-1])
    uclu.remove(' ')
    
    for i in uclu:
        if len(i)==3 and i.isnumeric():
            uclu[uclu.index(i)]=yuzler[int(i[0])-1]+onlar[int(i[1])]+birler[int(i[2])]
        elif len(i)==2:
            uclu[uclu.index(i)]=onlar[int(i[0])]+birler[int(i[1])]
        elif len(i)==1 and i.isnumeric():
            uclu[uclu.index(i)]=birler[int(i)]
    
    i=0
    while i<len(uclu)-2:
        if uclu[i]=="x":
            uclu.pop(i)
            uclu.pop(i)
        elif uclu[i]=="bir" and uclu[i+1]=="bin":
            uclu.pop(i)
        i+=1
    if 'x' in uclu:
        uclu.remove('x')
    return isaret+' '.join(uclu)
def main():
    imza.imza(__author__,"Sayı-Metin Dönüştürücü")
    a=input("Lütfen Metne Dönüştürmek İstediğiniz\nSayıyı Giriniz: ")
    print(donusum(int(a)))
if __name__=="__main__":
    main()