class BankBil:
    def __init__(self, isim, soyisim, hesap_turu):
        self.isim = isim
        self.soyisim = soyisim
        self.hesap_turu = hesap_turu


class Sifre:
    def __init__(self):
        self.deneme = 3
        self.bakiye = 12000
        self.sifre = 1234

    def giris_yap(self):
        while self.deneme > 0:
            try:
                girdi = int(input("Şifrenizi giriniz: "))
                if self.sifre == girdi:
                    print("Giriş başarılı!")
                    return True  # Başarılı giriş
                else:
                    self.deneme -= 1
                    if self.deneme > 0:
                        print(f"Yanlış şifre, lütfen tekrar deneyiniz. Kalan deneme: {self.deneme}")
                    else:
                        print("Hesap size ait değil.")
                        return False  # Başarısız giriş
            except ValueError:
                print("Lütfen geçerli bir şifre giriniz.")
                continue


class Hesap(BankBil, Sifre):
    def __init__(self, isim, soyisim, hesap_turu, bakiye):
        BankBil.__init__(self, isim, soyisim, hesap_turu)
        Sifre.__init__(self)
        self.bakiye = bakiye

    def bakiyeyi_goster(self):
        print("Eğer bakiyenizi dolar olarak görmek istiyorsanız 1 giriniz")
        print("Eğer bakiyenizi euro olarak görmek istiyorsanız 2 giriniz")
        print("Eğer bakiyenizi Türk lirası olarak görmek istiyorsanız 3 giriniz")
        try:
            tip = int(input("Tercihinizi giriniz: "))
            if tip == 1:
                print("Hesabınızda", self.bakiye / 34, "dolar var.")
            elif tip == 2:
                print("Hesabınızda", self.bakiye / 35, "euro var.")
            elif tip == 3:
                print("Hesabınızda", self.bakiye, "TL var.")
            else:
                print("Seçiminiz geçersiz.")
        except ValueError:
            print("Lütfen geçerli bir seçenek giriniz.")


class Islem(Sifre):
    def __init__(self, bakiye):
        super().__init__()
        self.bakiye = bakiye

    def paralar(self):
        if self.deneme > 0:
            print("Yapılacak işlemi seçiniz:")
            print("Para çekmek için 1, yatırmak için 2 seçin")
            a = input()

            if a == '1':  # Para çekme işlemi
                try:
                    cek = float(input("Çekilecek para miktarını giriniz: "))
                    if cek > self.bakiye:
                        print("Yetersiz bakiye.")
                    else:
                        self.bakiye -= cek
                        print(f"Yeni bakiye: {self.bakiye}")
                except ValueError:
                    print("Lütfen geçerli bir miktar giriniz.")
            elif a == '2':  # Para yatırma işlemi
                try:
                    yatir = float(input("Yatırılacak parayı giriniz: "))
                    self.bakiye += yatir
                    print(f"Yeni bakiye: {self.bakiye}")
                except ValueError:
                    print("Lütfen geçerli bir miktar giriniz.")
            else:
                print("Geçersiz işlem.")
        else:
            print("Hesabınızla giriş yapamadınız, işlem yapılamaz.")


# Örnek kullanım
giris = Hesap("Berkay", "Erdoğan", "Faizli Dolar", 12000)
if giris.giris_yap():  # Şifre doğru girilirse, bakiye işlemleri yapılabilir.
    giris.bakiyeyi_goster()
    hesap = Islem(12000)  # Başlangıç bakiyesi 12000 TL
    hesap.paralar()  # Para çekme veya yatırma işlemi




