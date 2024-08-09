def Hesap_Bol(Hesap:float,Kisi_Sayisi: int,parabirimi:str)->None:
    if Kisi_Sayisi<=1:
        raise ValueError("Kisi Sayisi 1 den buyuk olmali")
    Kisibas_Hesap:float=Hesap/Kisi_Sayisi
    print("-----------------------------")
    print(f"Toplam Hesap: {Hesap:,.2f} {parabirimi}")
    print(f"Kisi Sayisi: {Kisi_Sayisi}")
    print(f"Kisi Basi Hesap: {Kisibas_Hesap:,.2f} {parabirimi}")
    print("-----------------------------")
def typecheck(bilgi):
    val = bilgi
    while True:
        try:
            val1 = float(val)
            return val1
        except ValueError:
            try:
                val1 = int(val)
                return val1
            except ValueError:
                print("Giris Tipi Hatasi")
                val=input("Lutfen rakamlari Kullaniniz ve Tekrar giriniz:")

def main()->None:
    ToplamHesap:float = float(typecheck(input("Toplam Hesabi Giriniz:")))
    KisiSay:int = int(typecheck(input("Kisi Sayisini Giriniz:")))
    Hesap_Bol(ToplamHesap,KisiSay,"TL")  
if __name__=="__main__":
    main()    
        