from difflib import SequenceMatcher
from datetime import datetime
class sohbetbotu:
    def __init__(self,Isim:str,Cevaplar:dict[str,str]) -> None:
        self.isim =Isim
        self.cevaplar=Cevaplar
    @staticmethod
    def benzerlik_hesabi(giris_cumlesi:str,cevap_cumlesi:str)->float:
        cumle:SequenceMatcher=SequenceMatcher(a=giris_cumlesi,b=cevap_cumlesi)
        return cumle.ratio()
    def En_iyi_Cevap(self,giris_cumlesi:str)-> tuple[str,float]:
        en_yuksek_benzerlik:float = 0.0
        en_iyi_eslesme:str="Uzgunum, Anlayamadim."
        for cevap in self.cevaplar:
            benzerlik:float=self.benzerlik_hesabi(giris_cumlesi=giris_cumlesi,cevap_cumlesi=cevap)
            if benzerlik > en_yuksek_benzerlik:
                en_yuksek_benzerlik=benzerlik
                en_iyi_eslesme:str=self.cevaplar[cevap]
        return en_iyi_eslesme, en_yuksek_benzerlik
    def calistir(self)->None:
        print(f"Selam! Benim adim {self.isim}, Nasil yardimci olabilirim?")
        while True:
            Kullanici_girisi:str=input("Siz: ")
            cevap,benzerlik=self.En_iyi_Cevap(Kullanici_girisi)
            if benzerlik<0.5:
                print(f"{self.isim}: Uzgunum, Anlayamadim")
                continue
            if cevap=="ZAMAN":
                cevap=f"Zaman Suan: {datetime.now():%H:%M}"
            print(f"{self.isim}: {cevap} Benzerlik: {benzerlik:.2%}")
            if cevap=="Gorusuruz! Iyi Gunler":
                break   
def main()->None:
    Cevaplar:dict[str,str]={
        "Selam":"Selam! Bugun Nasil Yardimci Olabilirim?",
        "Nasilsin?": "Harika,Tesekkurler! Siz Nasilsiniz?",
        "Saat Kac?": "ZAMAN",
        "bay bay":"Gorusuruz! Iyi Gunler"
    }
    chatbot:sohbetbotu=sohbetbotu(Isim="Eva",Cevaplar=Cevaplar)
    chatbot.calistir()
if __name__=="__main__":
    main()