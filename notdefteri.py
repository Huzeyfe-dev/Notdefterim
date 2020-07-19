# yazar: Huzeyfe Çağılcı

import os

# Dosyalama işlemleri için sınıflar -----------------------------------------

# Dosya sınıfı asıl dosyalama sınıfıdır. ------------------------------------

class Dosya:
    sembol="+"
    çıkış="---"
    başlık_sembol="> "

    def oku(yol):
        if os.path.isfile(yol):
            try:
                f = open(yol, "r")
                sayfa = f.readlines()
                
                print("\n%s %s\n" %(Dosya.başlık_sembol,yol))
                
                for satır in sayfa:
                    print(Dosya.sembol, satır, end="")
                
                f.close()
                return sayfa
            except Exception as e: print("!! Hata:", e)
        
        else:
            print("\n>> Dosya bulunamadı: %s" %(yol))        
    
    def yaz(yol):
        if os.path.isfile(yol):
            f = open(yol, "a")
            
            while True:
                yazı=input(Dosya.sembol + " ")
                if yazı=="__sil__":
                	os.remove(yol)
                	print("\n>> Dosya silindi.") 
                	break          

                if yazı=="__yenile__" or yazı=="-y":
                	os.remove(yol)
                	Dosya.aç(yol)
                	break

                if yazı.split(",")[0]=="__aç__":
                	Dosya.aç(yazı.split(",")[1])
                	break

                if yazı==Dosya.çıkış or yazı=="__bitir__": break
                f.write(yazı +"\n")
            
            f.close()
        else:
            print("Dosya bulunamadı: %s" %(yol))

    # shutil ile dosya kopyalar
    def kopyala(kaynak, hedef):
        dosya_adı = os.path.split(kaynak)[1]
        yol = hedef +os.sep+ dosya_adı
        if os.path.isfile(kaynak) and \
           os.path.isdir(hedef):
            
            if shutil.copy(kaynak, yol):
                print("\n>> %s , %s dizinine kopyalandı." %(kaynak, hedef))
        
        else:
            print("Hata")
    
    def sil(yol):
        if os.path.isfile(yol):
           os.remove(yol) 

    def aç(yol):
        if not os.path.isfile(yol):
            f = open(yol, "w")
            f.close()
        Dosya.oku(yol)
        Dosya.yaz(yol)
    
# Dosya sınıfı içindeki komutlara input ile erişim sağlar. ----------------

class Dosya_Input:    
    
    def aç():
        dosya_=input("\n>> Dosya adı: ")
        Dosya.aç(dosya_) 

    def nano():
        dosya_=input("\n>> Dosya adı: ")
        os.system("nano "+dosya_)

    def oluştur():
        yol = input("\n>> Dosya adı: ")                
        f = open(yol, "w")
        f.close()
        print("\n>> Oluşturuldu: %s" %(yol))
        
    def sil():
        yol = input("\n>> Dosya adı: ")
        if os.path.isfile(yol):
            if not os.remove(yol):
                print("\n>> Silindi: %s" %(yol))
    
    def kopyala():
        kaynak=input("\n>> Kaynak dosya: ")
        hedef=input("\n>> Hedef dizin: ")
        Dosya.kopyala(kaynak, hedef)

def main():
	while True:
		komut=input("\n>> Komut: ")

		if komut=="çık":
			exit()
		elif komut=="aç":
			Dosya_Input.aç()
		elif komut=="sil":
			Dosya_Input.sil()
		elif komut=="nano":
			Dosya_Input.nano()
		elif komut=="yardım":
			print("""
--- Yardım ---

çık, aç, sil ,nano, yardım komutları tanınır.

""")

if __name__ == '__main__':
	main()
