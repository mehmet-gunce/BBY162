print("aşağıdaki sorulara 'D' ya da 'Y' olarak cevaplayınız.")

sorular= ['1.soru: Güneş’e en yakın gezegen merkürdür.[D/Y]',\
          '2.soru: Türkiye’nin en büyük ovası çukurovadır.[D/Y]',\
          '3.soru: Türkiye’nin en büyük 2.Gölü tuz gölüdür.[D/Y]',\
          '4.soru: Kendisine bağlı yakın adalarla birlikte geniş alan kaplayan kara parçalarına kıta denir.[D/Y]',\
          '5.soru: Yer katmanlarında oluşan bir sarsıntının dalgalar halinde çevreye yayılmasına orojenez denir.[D/Y]',]
cevaplar = ['D','Y','D','D','y']
puan = 0
#Soru 1
cevap = input((sorular[0]))
if cevaplar[0]==cevap.upper():
    print("Tebikler cevabınız doğru")
    puan+=1
else:
    print("Malesef yanlış cevap verdiniz.")
#soru 2
cevap = input((sorular[1]))
if cevaplar[1]==cevap.upper():
    print("Tebikler cevabınız doğru")
    puan+=1
else:
    print("Malesef yanlış cevap verdiniz.")
# soru 3
cevap = input((sorular[2]))
if cevaplar[2]==cevap.upper():
    print("Tebikler cevabınız doğru")
    puan+=1
else:
    print("Malesef yanlış cevap verdiniz.")
# soru 4
cevap = input((sorular[3]))
if cevaplar[3]==cevap.upper():
    print("Tebikler cevabınız doğru")
    puan+=1
else:
    print("Malesef yanlış cevap verdiniz.")
# soru 4
cevap = input((sorular[4]))
if cevaplar[4] == cevap.upper():
        print("Tebikler cevabınız doğru")
        puan += 1
else:
        print("Malesef yanlış cevap verdiniz.")
#sonuç
print("Bütün soruları cevapladınız. Puanınız: "+str(puan*20))