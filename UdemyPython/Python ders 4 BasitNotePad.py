import tkinter as tk
from tkinter import filedialog
from tkinter import Tk,Text,Frame,Button

class Basit_word:
    def __init__(self,root:Tk) -> None:
        self.root=root
        self.root.title("Benim Wordum")
        self.Metin_Alani: Text = Text(self.root,wrap="word")
        self.Metin_Alani.pack(expand=True,fill="both")
        self.Buton_Cercevesi: Frame = Frame(self.root)
        self.Buton_Cercevesi.pack()
        self.kayit_butonu : Button= Button(self.Buton_Cercevesi,text="Kaydet",command=self.Dosyayi_Kaydet)
        self.kayit_butonu.pack(side=tk.LEFT)
        self.Yeni_butonu : Button= Button(self.Buton_Cercevesi,text="Yeni",command=self.Yeni_Dosya)
        self.Yeni_butonu.pack(side=tk.LEFT)
        self.kayitli_Yukle_butonu : Button= Button(self.Buton_Cercevesi,text="Yukle",command=self.Dosyayi_Yukle)
        self.kayitli_Yukle_butonu.pack(side=tk.LEFT)
        self.Anlik_Dosya:str=""
    
    def run(self)->None:
        self.root.mainloop()
    def Dosyayi_Kaydet(self)->None:
        if self.Anlik_Dosya !="":
            with open(self.Anlik_Dosya,"w")as Dosyam:
                Dosyam.write(self.Metin_Alani.get(1.0,tk.END))
            print(f"Dosya Basarili Bir Sekilde {self.Anlik_Dosya} Adresine Kaydedildi.")
        else:
            Dosya_Yolu: str = filedialog.asksaveasfilename(defaultextension=".txt",
                                                       filetypes=[("Metin Dpsyalari","*.txt")])
            with open(Dosya_Yolu,"w")as Dosyam:
                Dosyam.write(self.Metin_Alani.get(1.0,tk.END))
            print(f"Dosya Basarili Bir Sekilde {Dosya_Yolu} Adresine Kaydedildi.")
            self.Anlik_Dosya=Dosya_Yolu
    def Yeni_Dosya(self)->None:
        self.Metin_Alani.delete(1.0,tk.END)
        self.Anlik_Dosya=""
        print(f"Yeni Dosya Acildi.")
    def Dosyayi_Yukle(self)->None:
        Dosya_Yolu: str = filedialog.askopenfilename(defaultextension=".txt",
                                                       filetypes=[("Metin Dpsyalari","*.txt")])
        with open(Dosya_Yolu,"r")as Dosyam:
            Icerik:str=Dosyam.read()
            self.Metin_Alani.delete(1.0,tk.END)
            self.Metin_Alani.insert(tk.INSERT,Icerik)
        print(f"Dosya Basarili Bir Sekilde {Dosya_Yolu} Adresinden Yuklendi.")
        self.Anlik_Dosya=Dosya_Yolu
def main()->None:
    root:Tk =tk.Tk()
    app: Basit_word =Basit_word(root=root)
    app.run()
if __name__=="__main__":
    main()