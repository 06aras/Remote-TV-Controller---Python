import random
import time

class Controller():


    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi = ["Trt","Atv","Show","KanalD","Star","Tv8","Fox"],kanal_durumu = "Show"):

        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.kanal_listesi = kanal_listesi

        self.kanal_durumu = kanal_durumu

    def tv_on(self):

        if (self.tv_durum == "Açık"):
            print("Televizyon zaten açık!")
        else:
            print("Televizyon Açılıyor...")
            time.sleep(1)
            print("Televizyon Açıldı.")

            self.tv_durum  = "Açık"

    def tv_off(self):

        if (self.tv_durum == "Kapalı"):
            print("Televizyon Zaten Kapalı..")
        else:
            print("Televizyon Kapanıyor....")
            time.sleep(1)
            print("Televizyon Kapandı.")

            self.tv_durum = "Kapalı"

    def ses(self):

        while True:
            ses_ayarı =  input("Sesi Azalt: '<'\nSesi Artır: '>'\nÇıkış : quit yaz")

            if (ses_ayarı == "<"):
                if (self.tv_ses != 0):

                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
            elif (ses_ayarı == ">"):
                if (self.tv_ses != 31):

                    self.tv_ses += 1

                    print("Ses:",self.tv_ses)
            elif (ses_ayarı == "quit"):
                print("İşlem Ekranına Yönlendiriliyor..")
                time.sleep(1)
                print("İşlem Ekranına Yönlendirildi.")

                break
            else:
                print("Hatalı İşlem Yaptınız!")
                time.sleep(1)
                print("İşlem Ekranına Yönlendiriliyor..")
                time.sleep(1)
                print("İşlem Ekranına Yönlendirildi.")


                break
    def kanal_ekle(self,kanal_ismi):

        print("Kanal ekleniyor....")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)

        print("Kanal Eklendi.")

    def kanal_cıkart(self,kanal_ismi):

        print("Kanal çıkartılıyor..")
        time.sleep(1)

        self.kanal_listesi.remove(kanal_ismi)

        print("Kanal Çıkartıldı.")
    def rastgele_kanal(self):

        rastgele = random.randint(0,len(self.kanal_listesi)-1)


        self.kanal = self.kanal_listesi[rastgele]

        print("Şu anki Kanal:" ,self.kanal)
    def __len__(self):

        return len(self.kanal_listesi)

    def __str__(self):

        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal_durumu)


kumanda = Controller()


print("""
**************************************************
Televizyon Uygulaması


1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Çıkartma

6. Kanal Sayısını Öğrenme

7. Rastgele Kanala Geçme

8. Televizyon Bilgileri

Çıkmak için 'q' ya basın.
**********************************************
""")


while True:

    işlem = input("İşlemi Seçiniz:")

    if (işlem == "q"):
        print("Program Sonlandırılıyor...")
        break

    elif (işlem == "1"):
        kumanda.tv_on()
    elif (işlem == "2"):
        kumanda.tv_off()

    elif (işlem == "3"):
        kumanda.ses()

    elif (işlem == "4"):
        print("Birden fazla kanal bilgisi girecekseniz  ',' ile ayırarak girin!")
        kanal_bilgisi = input("Kanal bilgisini girin:")

        kanal_listesi = kanal_bilgisi.split(",")

        for i in kanal_listesi:
            kumanda.kanal_ekle(i)

    elif (işlem=="5"):
        print("Birden fazla kanal ismi girecekseniz  ',' ile ayırarak girin!")
        kanal_ismi=input("Kanal isimini girin:")
        kanal_listesi = kanal_ismi.split(",")

        for i in kanal_listesi:
            kumanda.kanal_cıkart(i)

    elif (işlem == "6"):

        print("Kanal Sayısı:",len(kumanda))

    elif (işlem == "7"):
        kumanda.rastgele_kanal()
    elif (işlem == "8"):
        print(kumanda)

    else:
        print("Geçersiz İşlem!!")
        time.sleep(1)
        print("Lütfen Geçerli Bir İşlem Giriniz..")
        continue



