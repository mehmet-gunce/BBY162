#mehmet GÜNÇE
# for döngüsü kullanılarak hazırlanan kısa sınav
#09.04.2019
print("Coğrafya Testi")
sorular= ['Türkiye’nin en büyük ihracat limanı hangisidir?',\
          'Rüzgar tarafından taşınan topraklara ne ad verilir?',\
          'Kışın kuzeybatıdan esen soğuk kuru rüzgarın adı nedir?',\
          'Portekiz ve İspanya’nın bulunduğu yarımadaya ne ad verilir?',\
          'Türkiye’de hangi tarihten sonra gündüzler kısalmaya başlar?',]
cevaplar= ['B', 'A','D','A','A',]

cevapA=['PSÖDOMAKİ','LÖS','MAKİ','İBERİK','21 HAZİRAN']
cevapB=['İZMİR','İSTANBUL','MERSİN','SİNOP','GİRESUN']
cevapC=['DEPREM','GÖLLER','AKARSULAR','RÜZGARLAR','DALGA']
cevapD=['POYRAZ','SAMYELİ','KARAYEL','İKLİM','YER ŞEKİLLERİ']
toplamPuan =  0
for eleman in  range(len(sorular)):
    print ( " Soru "  +  str(eleman + 1 ) + " : " + sorular[eleman])
    print ( " A:) "  + cevapA [eleman])
    print ( " B:) "  + cevapB [eleman])
    print( " C:) "  + cevapC [eleman])
    print( " D:) "  + cevapD [eleman])
    cevap =input( "Lütfen cevabınızı giriniz: " )
    if cevaplar [eleman] == cevap.upper ():
        print("Tebrikler evabınız doğru")
        toplamPuan += 1
print( "Sınavımız sona erdi. Lütfen toplam puanınızı kontrol ediniz. " )
print ( "Puanınız: " + str ( int((toplamPuan/len(sorular)) * 100)))