morse_kodlari:dict[str,str] = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'Ç': '-.-..',  'D': '-..',    'E': '.',      
    'F': '..-.',   'G': '--.',    'Ğ': '--.-.', 
    'H': '....',   'I': '..',     'İ': '..',    
    'J': '.---',   'K': '-.-',    'L': '.-..', 
    'M': '--',     'N': '-.',     'O': '---',  
    'Ö': '---.',   'P': '.--.',   'Q': '--.-',  
    'R': '.-.',    'S': '...',    'Ş': '...-',  
    'T': '-',      'U': '..-',    'Ü': '..--',  
    'V': '...-',   'W': '.--',    'X': '-..-',  
    'Y': '-.--',   'Z': '--..',
    '1': '.----',  '2': '..---',  '3': '...--', 
    '4': '....-',  '5': '.....',  '6': '-....', 
    '7': '--...',  '8': '---..',  '9': '----.', 
    '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.',  '-': '-....-',  '(': '-.--.', 
    ')': '-.--.-'
}
def morsa_cevirici(metin:str)->str:
    return " ".join(morse_kodlari.get(karakter.upper(),"")for karakter in metin)
def Metine_donusuturucu(metin:str)->str:
    Sonucumuz:str=""
    for p in metin.split():
        for x,y in morse_kodlari.items(): 
            if y==p:
                Sonucumuz+=x 
    return Sonucumuz
def main()->None:
    veri_giris:str=input("Metni Griniz: ")
    output:str=morsa_cevirici(veri_giris)
    deneme:str=Metine_donusuturucu(output)
    print(output)
    print(deneme)
if __name__=="__main__":
    main()