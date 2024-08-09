def Dosya_Ac(yol:str)->str:
    with open(yol,"r") as dosya:
        metin:str=dosya.read()
        return metin
def kelime_sayici(metin:str)->dict[str,int]:
    yeni_eleman:dict[str,int]={}
    for x in metin.split():
        s:int=metin.count(x)
        yeni_eleman.update({x:s})
    sirali_list:str = sorted(yeni_eleman.items(),key=lambda item:item[1],reverse=True)
    print(sirali_list)
    sirali_dict:dict[str,int]=dict(sirali_list)
    print(sirali_dict)
    return sirali_dict
        
def analiz_et(metin:str)->dict[str,int]:
    sonuc: dict[str,int] = {
        "toplam_karakter_bosluklu":len(metin),
        "toplam_karakter_bosluksuz":len(metin.replace(" ","")),
        "Bosluk Sayisi": metin.count(" "),
        "toplam_Kelime Sayisi":len(metin.split())
    }
    Ectek : dict[str:int]= kelime_sayici(metin=metin)
    a:int=0
    for x,y in Ectek.items():
        if a<5:
            print(f"{x} kelimesi {y} adet tekrar etmistir.")
            a+=1
    return sonuc
def main()->None:
    metnim:str=Dosya_Ac("Deneme.txt")
    analiz_sonucu:dict[str:int]=analiz_et(metnim)
    print(f"{metnim}")
    for veriadi,adeti in analiz_sonucu.items():
        print(f"{veriadi}  :  {adeti}")
if __name__=="__main__":
    main()