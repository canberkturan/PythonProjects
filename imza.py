#-*-coding:utf8;-*-
def imza(a="Geliştirici Adı",b="Program Adı"):
    kare=max(len(a+"Developer:"),len(b))+4    
    print("#"*kare)
    print("#{:^{}}#".format(b,kare-2))
    print("#{:^{}}#".format("Developer:"+a,kare-2))
    print("#"*kare)
if __name__=="__main__":
    imza("Canberk Turan","Trigonometri")
