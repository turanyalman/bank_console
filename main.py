print("\n=====pythone banka hoşgeldiniz======")
print("şifre girin ya da kaydolun")
bakiye=0
ghakki=3
zayifsifreler=("123","1234","123456")

kullaniciadi=input("kullanıcı adınızı giriniz :").lower().strip()
sifre=input("şifre girin :")

if sifre in zayifsifreler :
    print("şifre zayıf daha güçlü şifre deneyin !!")
else:
    print("kayıt başarılı ")

while ghakki >0 :
    girisadi=input("giriş için adınızı yazın :")
    girissifre=input("şifrenizi giriniz : ")

    if kullaniciadi == girisadi and sifre == girissifre :
        print ("giriş başarılı ")

        while True:
            print("\n=====yapmak istediğiniz işlemi seçin=====")
            print("\n 1-para yatırma ")
            print("\n 2- para çekme ")
            print("\n 3-bakiye göster")
            print("\n q-çıkış  ")

            secim=input("seçimizi giriniz:")          
            if secim not in ["1","2","3","q"]:
                print("geçerli seçim yapınız ")
            elif secim == "1":
                parayatırma=float(input("yatırmak istediğiniz miktarı giriniz:"))
                if parayatırma <=0 :    
                    print("hatalı işlem")
                else:
                    bakiye+=parayatırma
                    print("para yatırma başarılı güncel bakiyeniz ",bakiye)
                

            elif secim == "2":
                cekilmekistenentutar=float(input("çekmek istediğiniz mikatar:"))
            
                if cekilmekistenentutar <= 0:
                    print("geçersiz işlem ")
                elif cekilmekistenentutar > bakiye :
                    print("bakiye yetersiz ")
                else:
                    bakiye -= cekilmekistenentutar
                    print("işlem başarılı güncel bakiye",bakiye)
            elif secim == "3":
                print("güncel bakiyeniz ",bakiye)

            elif secim == "q":
                print("çıkış yapılıyor...")
                break    
            else:
                print("geçerli işlem seçiniz ")
        break 
    else:
        ghakki -= 1
        print("hatalı giriş kalan hak:", ghakki)

        if ghakki == 0:
            print("kart bloke edildi") 
