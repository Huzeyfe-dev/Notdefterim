# yazar: Huzeyfe Çağılcı

import os

try: import şifrele
except: 
			print("!! [şifrele] modülü bulunamadı.")
			input()
			exit()



türler={"sezar": şifrele.sezar}


class Şifreli:
    tür="sezar"
    sembol="+"
    çıkış="---"
    başlık_sembol=">"
    şifrele=türler[tür]
    
    def oku(yol, key=5):
        if os.path.isfile(yol):
            f = open(yol, "r")
            sayfa = f.readlines()
            print("\n%s %s\n" %(Şifreli.başlık_sembol,yol))
            sayfa_=[]
            for satır in sayfa:
                yazı=Şifreli.şifrele(satır, -key)
                print(Şifreli.sembol, yazı)
                sayfa_.append(yazı)
            
            f.close()
            return sayfa_
        
        else:
            print("\n>> Dosya bulunamadı: %s" %(yol))        
    
    def yaz(yol, key=5):
        if os.path.isfile(yol):
            f = open(yol, "a")
            while True:
                yazı=input(Şifreli.sembol + " ")
                if yazı=="__sil__":
                	os.remove(yol)
                	print("\n>> Dosya silindi.") 
                	break          

                if yazı=="__yenile__" or yazı=="-y":
                	os.remove(yol)
                	Şifreli.aç(yol)
                	break

                if yazı.split(",")[0]=="__aç__":
                	Şifreli.aç(yazı.split(",")[1])
                	break

                if yazı==Şifreli.çıkış or yazı=="__bitir__": break
                f.write(Şifreli.şifrele(yazı, key) +"\n")
            
            f.close()
        else:
            print("Dosya bulunamadı: %s" %(yol))

    def aç(yol, key=5):
        if not os.path.isfile(yol):
            f = open(yol, "w")
            f.close()
        Şifreli.oku(yol, key)
        Şifreli.yaz(yol, key)


if __name__=="__main__":
    Şifreli.aç("metin.txt")
