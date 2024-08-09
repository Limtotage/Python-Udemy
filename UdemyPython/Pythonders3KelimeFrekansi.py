from collections import Counter
import re

def Kelime_frekansi(metin:str) -> list[tuple[str,int]]:
    hepsikucuk_metin: str= metin.lower()
    kelimeler : list[str]=re.findall(r"\b\w+\b",hepsikucuk_metin)
    kelime_sayilari : Counter = Counter(kelimeler)
    return kelime_sayilari.most_common()
def main() ->None:
    Dosya: str = input("Dosyanin Adini Uzantisiyla Giriniz:(.txt/.pdf...) ")
    try:
        dsym=open(Dosya,"r")
        Satirlar:list[str]=dsym.readlines()
        Metin : str= Satirlar[0]
        a : int = 0
        for Satir in Satirlar:
            if a==0:
                a+=1
                continue
            else:
                Metin+=Satir
    except IOError:
        print("Dosya Bulunamadi")
    finally:
        dsym.close()
    kelime_frekanslari:list[tuple[str,int]] = Kelime_frekansi(Metin)
    for kelime,adeti in kelime_frekanslari:
        print(f"{kelime}: {adeti}")
if __name__=="__main__":
    main()