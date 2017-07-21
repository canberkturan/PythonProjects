import os
from sayilar import*
class TicTacToe:
    ihtimal=[[1,2,3],[4,5,6],[7,8,9],
    [1,4,7],[2,5,8],[3,6,9],
    [1,5,9],[3,5,7]]
    def __init__(self):
        self.tahta=[None for i in range(1,10)]
    def bitti_mi(self):
        boslar=[i for i in self.tahta if i==None]
        if len(boslar)==0:
            return True
        if self.kazanan()!=None:
            return True
        return False
    def kazanan(self):
        for oyuncu in (1,-1):
            for iht in TicTacToe.ihtimal:
                if self.tahta[iht[0]-1]==self.tahta[iht[1]-1] and self.tahta[iht[1]-1]==self.tahta[iht[2]-1] and self.tahta[iht[0]-1]==oyuncu:
                    return oyuncu
        if len([i for i in self.tahta if i==None])==0:
            return 0
        return None
    def mumkunHamleler(self):
        return [i for i in range(1,10) if self.tahta[i-1]==None]   
    def hamleYap(self,konum,oyuncu):
        self.tahta[konum-1]=oyuncu
    def minimax(self,oyuncu):
        rakip=-1*oyuncu
        if self.kazanan()!=None:
            return self.kazanan(),None
        enIyiHamle=None
        enIyiDeger=-100000
        for hamle in self.mumkunHamleler():
            self.hamleYap(hamle,oyuncu)
            deger=self.minimax(rakip)[0]
            self.hamleYap(hamle,None)
            if deger*oyuncu>enIyiDeger:
                enIyiDeger=deger*oyuncu
                enIyiHamle=hamle
        return (enIyiDeger*oyuncu,enIyiHamle)
    def ekranaBas(self,oyuncular):
        for i in range(9):
            if i%3==0:
                print("\n|",end="")
            if self.tahta[i]==None:
                print(i+1,end="|")
            else:
                print(oyuncular[self.tahta[i]],end="|")
        print()
    def yazdir(self,oyuncular):
        tablo={"x":X,"o":O}
        liste=[[bir,iki,uc],[dort,bes,alti],[yedi,sekiz,dokuz]]
        for k in range(9):
            if self.tahta[k]!=None:
                liste[int(k/3)][k%3]=tablo[oyuncular[self.tahta[k]]]
        for i in liste:
            for j in range(7):
                print(i[0][j*13:(j*13)+13]+i[1][j*13:(j*13)+13]+i[2][j*13:j*13+13])
def OyuncuVsAI():
    oyun=TicTacToe()
    os.system('clear')
    xo=input("X misiniz O musunuz?")
    karakterSeti=[" "]
    if xo.lower()=="x":
        karakterSeti.extend(["o","x"])
    else:
        karakterSeti.extend(["x","o"])
    while not oyun.bitti_mi():
        oyun.yazdir(karakterSeti)
        olasi=oyun.mumkunHamleler()
        print("Hamleniz-->",end="")
        hamle=input()
        try:
            if int(hamle) in olasi:
                oyun.hamleYap(int(hamle),-1)
                os.system('clear')
            else:
                os.system('clear')
                print("Lütfen 1-9 arası bir sayı giriniz!")
                continue
        except ValueError:
            os.system('clear')
            print("--Lütfen Bir Tamsayı Giriniz--")
            continue
        os.system('clear')
        oyun.yazdir(karakterSeti)
        try:
            oyun.hamleYap(oyun.minimax(1)[1],1)
        except:
            continue
        os.system('clear')
    oyun.yazdir(karakterSeti)
    sonuc=oyun.kazanan()
    if sonuc==0:
        print("Berabere")
        return
    print("{} kazandı!".format(karakterSeti[sonuc].upper()))
def AIvsAI():
    oyun=TicTacToe()
    os.system('clear')
    karakterSeti=[" ","x","o"]
    while not oyun.bitti_mi():
        os.system('clear')
        oyun.yazdir(karakterSeti)
        try:
            oyun.hamleYap(oyun.minimax(1)[1],1)
        except:
            continue
        os.system('clear')
        oyun.yazdir(karakterSeti)
        try:
            oyun.hamleYap(oyun.minimax(-1)[1],-1)
        except:
            continue
        
    os.system('clear')
    oyun.yazdir(karakterSeti)
    sonuc=oyun.kazanan()
    if sonuc==0:
        print("Berabere")
        return
    print("{} kazandı!".format(karakterSeti[sonuc]))
def OyuncuVsOyuncu():
    oyun=TicTacToe()
    sira=1
    karakterSeti=[" ","x","o"]
    olasi=[1,2,3,4,5,6,7,8,9]
    os.system('clear')
    while not oyun.bitti_mi():
        oyun.yazdir(karakterSeti)
        olasi=oyun.mumkunHamleler()
        print("{}--Hamleniz-->".format(karakterSeti[sira].upper()),end="")
        hamle=input()
        try:
            if int(hamle) in olasi:
                oyun.hamleYap(int(hamle),sira)
                sira=sira*(-1)
                os.system('clear')
            else:
                print("Lütfen 1-9 arası bir sayı giriniz!")
        except ValueError:
            os.system('clear')
            print("--Lütfen Bir Tamsayı Giriniz--")
    sonuc=oyun.kazanan()
    oyun.yazdir(karakterSeti)
    if sonuc==0:
        print("Berabere")
        return
    print("{} Kazandı!".format(karakterSeti[sonuc]))
def menu():
    oyunlar={'1':'OyuncuVsOyuncu()',
             '2':'OyuncuVsAI()',
             '3':'AIvsAI()',
             '4':'print("Çıkış Yapıldı")'}
    print("1-İki Kişilik")
    print("2-Bilgisayara Karşı")
    print("3-Bilgisayar-Bilgisayar")
    print("4-Çıkış Yap")
    secim=input("Seçiminiz-->")
    try:
        komut=oyunlar[secim]
        exec(komut)
    except:
        os.system('clear')
        print("Hatalı Giriş Yaptınız")
        print("Tekrar Deneyin")
        menu()
if __name__=='__main__':
    menu()