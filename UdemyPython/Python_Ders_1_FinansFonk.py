def finans_hesaplama(aylik_gider:float,aylik_gelir: float,vergi_orani:float,parabirimi:str)->None:
    aylik_vergi: float = aylik_gelir*(vergi_orani/100)
    aylik_net_gelir:float =aylik_gelir-aylik_vergi-aylik_gider
    yillik_maas: float = aylik_gelir*12
    yillik_gider:float = aylik_gider*12
    yillik_vergi:float= aylik_vergi*12
    yillik_net_gelir:float=yillik_maas-yillik_vergi-yillik_gider
    print("-----------------------------")
    print(f"Aylik Gelir: {aylik_gelir:,.2f}{parabirimi}")
    print(f"Vergi Orani: {vergi_orani:,.0f}%")
    print(f"Aylik Vergi: {aylik_vergi:,.2f}{parabirimi}")
    print(f"Aylik Net Gelir: {aylik_net_gelir:,.2f}{parabirimi}")
    print(f"Yillik Gelir: {yillik_maas:,.2f}{parabirimi}")
    print(f"Yillik Odenen Vergi: {yillik_vergi:,.2f}{parabirimi}")
    print(f"Yillik Net Gelir: {yillik_net_gelir:,.2f}{parabirimi}")
def typecheck(bilgi):
    try:
        val = float(bilgi)
        return val
    except ValueError:
        try:
            val2 = int(bilgi)
        except ValueError:
            print("Giris Tipi Hatasi")
            return 0
            
def main() ->None:
    AylikM_giris:float=float(typecheck(input("Aylik Maasinizi Giriniz:")))
    Vergi_OrGiris:float=float(typecheck(input("Vergi Oranini Giriniz:")))
    Aylik_Harcama:float=float(typecheck(input("Aylik Harcamanizi Giriniz:")))
    finans_hesaplama(Aylik_Harcama,AylikM_giris,Vergi_OrGiris,parabirimi=" TL")
if __name__=="__main__":
    main()
    
        