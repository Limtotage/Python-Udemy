import json
def Oranlari_Yukle(Dosya:str)-> dict[str,dict]:
    with open(Dosya,"r") as dsy:
        return json.load(dsy)    
def Cevir(Miktar:float, Paratipi:str, hedefparabirimi:str,oranlar:dict[str,dict])->float:
    FParatipi:str=Paratipi.lower()
    Fhedefparabirimi:str=hedefparabirimi.lower()
    Kaynak_Orani:dict| None = oranlar.get(FParatipi)
    Hedef_Orani:dict| None = oranlar.get(Fhedefparabirimi)
    try:
        if Paratipi=="try":
            return Miktar*Hedef_Orani["rate"]
        else:
            return Miktar*(Hedef_Orani["rate"]/Kaynak_Orani["rate"])
    except TypeError as e:
        print(f"Gecerli olmayan para birimi. Gecerli para birimleri alttadir.")
        for x in oranlar:
            print(x)
        return 0
def main()-> None:
    Oranlar:dict[str,dict]=Oranlari_Yukle("ParaBirimleri.json")
    miktarim:float=60
    paratipim:str="try"
    hedefim:str="krw"
    sonuc:float=Cevir(miktarim,paratipim,hedefim,Oranlar)
    print(f"{miktarim} {paratipim} = {sonuc} {hedefim}.")
if __name__=="__main__":
    main()