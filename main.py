kullanicilar = [
    {
        "username": "ebrar",
        "password": "123456",
        "bakiye": 100000
    },

    {
        "username": "turan",
        "password": "123",
        "bakiye": 150000
    }
]

giris_yapan_kullanici = None

while True:

    print("\n=== BANKA SİSTEMİ ===")
    print("1 - Kayıt Ol")
    print("2 - Giriş Yap")
    print("3 - Çıkış")

    secim = input("Seçiminiz: ")

    
    if secim == "1":

        yeni_username = input("Kullanıcı adı: ")
        yeni_password = input("Şifre: ")

        kullanici_varmi = False

        for kullanici in kullanicilar:

            if kullanici["username"] == yeni_username:
                kullanici_varmi = True

        if kullanici_varmi == True:
            print("Bu kullanıcı adı zaten var")

        else:

            yeni_kullanici = {
                "username": yeni_username,
                "password": yeni_password,
                "bakiye": 0
            }

            kullanicilar.append(yeni_kullanici)

            print("Kayıt başarılı")

   
    elif secim == "2":

        username = input("Kullanıcı adı: ")
        password = input("Şifre: ")

        giris_basarili = False

        for kullanici in kullanicilar:

            if (
                kullanici["username"] == username
                and
                kullanici["password"] == password
            ):

                giris_basarili = True
                giris_yapan_kullanici = kullanici

        if giris_basarili:
            print("Giriş başarılı")

            
            while True:

                print("\n=== KULLANICI PANELİ ===")
                print("1 - Bakiye Görüntüle")
                print("2 - Para Yatır")
                print("3 - Para Çek")
                print("4 - Çıkış Yap")

                kullanici_secim = input("Seçiminiz: ")

                
                if kullanici_secim == "1":

                    print("Bakiyeniz:",
                          giris_yapan_kullanici["bakiye"])

                
                elif kullanici_secim == "2":

                    miktar = int(input("Yatırılacak miktar: "))

                    giris_yapan_kullanici["bakiye"] += miktar

                    print("Para yatırıldı")
                    print("Yeni bakiye:",
                          giris_yapan_kullanici["bakiye"])

                
                elif kullanici_secim == "3":

                    miktar = int(input("Çekilecek miktar: "))

                    if miktar > giris_yapan_kullanici["bakiye"]:

                        print("Yetersiz bakiye")

                    else:

                        giris_yapan_kullanici["bakiye"] -= miktar

                        print("Para çekildi")
                        print("Yeni bakiye:",
                              giris_yapan_kullanici["bakiye"])

                
                elif kullanici_secim == "4":

                    print("Çıkış yapıldı")
                    break

                else:
                    print("Geçersiz seçim")

        else:
            print("Kullanıcı adı veya şifre yanlış")

    
    elif secim == "3":

        print("Program kapatıldı")
        break

    else:
        print("Geçersiz seçim")

        None
