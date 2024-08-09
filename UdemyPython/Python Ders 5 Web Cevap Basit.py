import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict

def Durum_Kontrol(url:str)->None:
    try:
        Cevap:Response = requests.get(url)
        Durum_Kodu: int = Cevap.status_code
        headers: CaseInsensitiveDict[str]=Cevap.headers
        Icerik_tipi:str= headers.get("Content-Type","Unknown")
        Sunucu:str=headers.get("Server","Unknown")
        Cevap_suresi:float= Cevap.elapsed.total_seconds()
        print(f"URL: {url}")
        print(f"Durum Kodu: {Durum_Kodu}")
        print(f"Icerik tipi: {Icerik_tipi}")
        print(f"Sunucu: {Sunucu}")
        print(f"Cevap Suresi: {Cevap_suresi:.2f} saniye")
    except RequestException as re:
        print(f"Baglanti Hatasi {re}")
def main():
    Test_urlsi:str="https://www.google.com"
    Durum_Kontrol(url=Test_urlsi)
if __name__=="__main__" :
    main()