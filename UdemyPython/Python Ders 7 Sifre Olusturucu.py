import secrets
import string
class Sifre:
    def __init__(self,uzunluk:int=12,BuyukHarfler:bool=True,Semboller:bool=True) -> None:
        self.uzunluk=uzunluk
        self.BuyukHarf=BuyukHarfler
        self.Sembol=Semboller
        
        self.temel_karakterler: str= string.ascii_lowercase+string.digits
        if self.BuyukHarf:
            self.temel_karakterler+=string.ascii_uppercase
        if self.Sembol:
            self.temel_karakterler+=string.punctuation
    def Olustur (self)->None:
        sifre: list[str]=[]
        for i in range(self.uzunluk):
            sifre.append(secrets.choice(self.temel_karakterler))
        return "".join(sifre)
    def buyukharf(self,gelen_sifre:list[str])->bool:
        BHYS:int=0#Buyuk Harf Yoktur Sayacı
        for x in gelen_sifre:
            try:
                i=string.ascii_uppercase.index(x)
                return True
            except ValueError:
                BHYS+=1  
        if len(gelen_sifre)==BHYS:
            return False
    def Sembolum(self,gelen_sifre:list[str])->bool:
        SYS:int=0#Sembol Yoktur Sayacı
        for x in gelen_sifre:
            try:
                i=string.punctuation.index(x)
                return True
            except ValueError:
                SYS+=1  
        if len(gelen_sifre)==SYS:
            return False  
    def Guc_Kontrol(self,gelen_sifre:list[str])->None:
        gs:int=0#Güç Sayacı
        Buyuk_harf_kontrol:bool=self.buyukharf(gelen_sifre)
        Sembol_kontrol:bool=self.Sembolum(gelen_sifre)          
        if len(gelen_sifre)>=16:
            print("Sifreniz 16 karakterden fazla eleman iceriyor.")
            gs+=1
        if Buyuk_harf_kontrol:
            print("Sifreniz Buyuk Harf iceriyor.")
            gs+=1
        if Sembol_kontrol:
            print("Sifreniz Sembol iceriyor.")    
            gs+=1
        if gs==3:
            print(f"{gelen_sifre}   -----   Sifreniz Gucludur.")
def main()->None:
    sifrem:Sifre=Sifre(uzunluk=20,Semboller=False)
    benimki=sifrem.Olustur()
    sifrem.Guc_Kontrol(benimki)
if __name__=="__main__":
    main()