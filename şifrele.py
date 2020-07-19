# Yazıları şifrelemek için oluşturula bir modüldür.
# Henüz sadece sezar şifreleme yapabilir.
#
# yazar: Huzeyfe Çağılcı

"""örnek kullanım:

sezar("Huzeyfe")
Out: 'Mz\x7fj~kj'

sezar("Huzeyfe", 6)
Out: 'N{\x80k\x7flk'

sezar("N{\x80k\x7flk", 6, True)
Out: 'Huzeyfe'"""

def sezar(yazı, key=5, çöz=False):
    şifreli_yazı=""
    key=-key if çöz else key
    for harf in yazı:
        şifreli_yazı+=chr(ord(harf) + key)
	
    return şifreli_yazı

def artan_sezar(yazı, çöz=False):
    şifreli_yazı=""
    key=0
    for harf in yazı:
        if key>=10:
            key=0
        key+=1
        
        if çöz:
            şifreli_yazı+=chr(ord(harf) - key)
        else:
            şifreli_yazı+=chr(ord(harf) + key)
    
    return şifreli_yazı

ters_artan_sezar= lambda yazı, çöz=False: artan_sezar(yazı, çöz)[::-1] if çöz else artan_sezar(yazı[::-1])
ters_sezar= lambda yazı, key=5: sezar(yazı[::-1], key)

