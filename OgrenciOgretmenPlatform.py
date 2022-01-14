list_of_stdmat = {"caner": 90, "kürşat": 92, "kamil": 10, "yasin": 69}
list_of_stdprog1 = {"caner": 60, "kürşat": 57, "kamil": 85, "yasin": 35}
list_of_stdprog2 = {"caner": 70, "kürşat": 45, "kamil": 65, "yasin": 56}
list_of_stdmantik = {"caner": 54, "kürşat": 69, "kamil": 87, "yasin": 98}


cnrNot = []
krstNot = []
kmlNot = []
ysnNot = []

cnrmatNot = []
krstmatNot = []
kmlmatNot = []
ysnmatNot = []

cnrprog1Not = []
kmlprog1Not = []
ysnprog1Not = []
krstprog1Not = []

cnrprog2Not = []
krstprog2Not = []
kmlprog2Not = []
ysnprog2Not = []

cnrmantkNot = []
krstmantkNot = []
kmlmantkNot = []
ysnmantkNot = []

def ekle(liste,Not):
    liste.extend([Not])
    return

ekle(cnrmatNot,list_of_stdmat["caner"])
ekle(cnrprog1Not,list_of_stdprog1["caner"])
ekle(cnrprog2Not,list_of_stdprog2["caner"])
ekle(cnrmantkNot,list_of_stdmantik["caner"])

ekle(cnrNot,cnrmatNot)
ekle(cnrNot,cnrprog1Not)
ekle(cnrNot,cnrprog2Not)
ekle(cnrNot,cnrmantkNot)

ekle(krstmatNot, list_of_stdmat["kürşat"])
ekle(krstprog1Not, list_of_stdprog1["kürşat"])
ekle(krstprog2Not, list_of_stdprog2["kürşat"])
ekle(krstmantkNot, list_of_stdmantik["kürşat"])

ekle(krstNot, krstmatNot)
ekle(krstNot, krstprog1Not)
ekle(krstNot, krstprog2Not)
ekle(krstNot, krstmantkNot)

ekle(kmlmatNot, list_of_stdmat["kamil"])
ekle(kmlprog1Not, list_of_stdprog1["kamil"])
ekle(kmlprog2Not, list_of_stdprog2["kamil"])
ekle(kmlmantkNot, list_of_stdmantik["kamil"])

ekle(kmlNot, kmlmatNot)
ekle(kmlNot, kmlprog1Not)
ekle(kmlNot, kmlprog2Not)
ekle(kmlNot, kmlmantkNot)

ekle(ysnmatNot, list_of_stdmat["yasin"])
ekle(ysnprog1Not, list_of_stdprog1["yasin"])
ekle(ysnprog2Not, list_of_stdprog2["yasin"])
ekle(ysnmantkNot, list_of_stdmantik["yasin"])
ekle(ysnNot, ysnmatNot)
ekle(ysnNot, ysnprog1Not)
ekle(ysnNot, ysnprog2Not)
ekle(ysnNot, ysnmantkNot)



list_of_lessons = ["matematik","java","pyhton","mantık devreleri"]

girisHakki = 5

tchrUserName = "hoca"
tchrName = "Hoca"
tchrPassword = "12345"

cnrUserName = "cnr123"
cnrName = "Caner"
cnrPassword = "12345"

krstUserName = "krst123"
krstName = "Kürşat"
krstPassword = "12345"

kmlUserName = "kml123"
kmlName = "Kâmil"
kmlPassword = "12345"

ysnUserName = "ysn123"
ysnName = "Yasin"
ysnPassword = "12345"

def harfNotuHesapla():

    vize = input("Vize: ")
    final = input("Final: ")
    sonuc = int(vize)*(4/10) + int(final)*(6/10)
    if(sonuc >=90):
        print("Harf Notu: AA")
    elif(sonuc>=85):
        print("Harf Notu: BA")
    elif(sonuc>=80):
        print("Harf Notu: BB")
    elif(sonuc>=75):
        print("Harf Notu: CB")
    elif(sonuc>=70):
        print("Harf Notu: CC")
    elif(sonuc>=65):
        print("Harf Notu: DC")
    elif(sonuc>=60):
        print("Harf Notu: DD")
    else:
        print("Harf Notu: FF")

    print ("Ortalama: " + str(sonuc))





def not_degistir(list_of_std,ogrenciName, notDegis):
    list_of_std[ogrenciName] = notDegis
    return


while True:
    print("""********************************************************
    ÖĞRETMEN - ÖĞRENCİ BİLGİ PLATFORMUNA HOŞ GELDİNİZ...

    Öğretmen Girişi İçin 1,

    Öğrenci Girişi İçin 2,

    Çıkmak için q'ya basınız...
    yazınız.

    ********************************************************""")
    islem = input("İşlem giriniz: ")
    if islem == "q":
        print("Çıkış yapılıyor...")
        break
    while True:

        if girisHakki == 0:
            print("Giriş hakkınız kalmadı. Daha sonra tekrar deneyiniz...")
            break



        elif islem == "1":
            ogrtmnUserName = input("Öğretmen kullanıcı adı: ")
            ogrtmnPassword = input("Öğretmen parola: ")

            if (tchrUserName == ogrtmnUserName) & (tchrPassword == ogrtmnPassword):
                print("Giriş Başarılı...\nHoşgeldin " + tchrName + "!")
                while True:

                    print("1: Öğrenci notlarını görüntüle.\n2: Öğrenci notlarını gir.")
                    print("3: Çıkış")
                    islem1 = input("Yapmak istediğiniz işlemi seçiniz: ")

                    if islem1 == "1":
                        while (True):
                            ders = input("Hangi dersin notlarını görmek istiyorsunuz?: ")
                            if ders == "matematik":
                              print(list_of_stdmat)
                              break
                            elif ders=="java":
                                print(list_of_stdprog1)
                                break
                            elif ders == "python":
                                print(list_of_stdprog2)
                                break
                            elif ders == "mantık devreleri":
                               print(list_of_stdmantik)
                               break
                            else:
                              print("Lütfen bir ders giriniz.")

                    elif islem1 == "2":
                        while(True):
                            stdName = input("Notunu değiştirmek istediğiniz dersi giriniz:")

                            list_of_std =""
                            if stdName == "matematik":
                                stdName = list_of_stdmat
                                list_of_std = stdName

                                break
                            elif stdName == "java":
                                stdName = list_of_stdprog1
                                list_of_std = stdName
                                break
                            elif stdName == "python":
                                stdName = list_of_stdprog2
                                list_of_std = stdName
                                break
                            elif stdName == "mantık devreleri":
                                stdName = list_of_stdmantik
                                list_of_std = stdName
                                break
                            else:
                                print("Lütfen geçerli bir ders giriniz.")
                        ogrenciName = input("Girmek istediğiniz öğrencinin adını giriniz: ")
                        stdNot = int(input(ogrenciName + " adlı öğrencinin yeni notunu giriniz: "))

                        not_degistir(list_of_std,ogrenciName,stdNot)
                        print(ogrenciName +" adlı öğrencinin notu " + str(stdNot) + " olarak değiştirildi.")
                    elif islem1== "3":
                        print("Hesaptan çıkış yapılıyor...")
                        break


            elif (tchrUserName == ogrtmnUserName) & (tchrPassword != ogrtmnPassword) | (
                    tchrUserName != ogrtmnUserName) & (tchrPassword == ogrtmnPassword) | (
                    tchrUserName != ogrtmnUserName) & (tchrPassword != ogrtmnPassword):
                print("Kullanıcı adı veya Parola hatalı...\nLütfen Tekrar deneyiniz...")
                girisHakki -= 1
                print("Kalan giriş hakkı: ", girisHakki)




        elif islem == "2":

            ogrncUserName = input("Öğrenci kullanıcı adı: ")
            ogrncPassword = input("Öğrenci parola: ")

            if (krstUserName =="krst123") & (krstUserName == ogrncUserName) & (krstPassword == ogrncPassword):

                print("Giriş Başarılı...\nHoşgeldin " + krstName + "!")
                while True:

                    print("1: Derslerimi görüntüle.\n2: Notlarımı görüntüle.\n3: Ortalama hesapla.")
                    print("4: Çıkış")
                    islem1 = input("Yapmak istediğiniz işlemi seçiniz: ")

                    if islem1 == "1":
                        print(list_of_lessons)

                    elif islem1 == "2":
                        print("Matematik: " + str(krstNot[0][0]))
                        print("Java: " + str(krstNot[1][0]))
                        print("Python: " + str(krstNot[2][0]))
                        print("Mantık Devreleri: " + str(krstNot[3][0]))
                    elif islem1 == "3":
                        harfNotuHesapla()
                    elif islem1 == "4":
                        print("Hesaptan çıkış yapılıyor...")
                        break

            elif (cnrUserName == "cnr123") & (cnrUserName == ogrncUserName) & (cnrPassword == ogrncPassword):

                print("Giriş Başarılı...\nHoşgeldin " + cnrName + "!")
                while True:

                    print("1: Derslerimi görüntüle.\n2: Notlarımı görüntüle.\n3: Ortalama hesapla.")
                    print("4: Çıkış")
                    islem1 = input("Yapmak istediğiniz işlemi seçiniz: ")

                    if islem1 == "1":
                        print(list_of_lessons)

                    elif islem1 == "2":
                        print("Matematik: " + str(cnrNot[0][0]))
                        print("Java: " + str(cnrNot[1][0]))
                        print("Python: " + str(cnrNot[2][0]))
                        print("Mantık Devreleri: " + str(cnrNot[3][0]))
                    elif islem1 == "3":
                        harfNotuHesapla()
                    elif islem1 == "4":
                        print("Hesaptan çıkış yapılıyor...")
                        break

            elif (kmlUserName == "kml123") & (kmlUserName == ogrncUserName) & (kmlPassword == ogrncPassword):

                print("Giriş Başarılı...\nHoşgeldin " + kmlName + "!")
                while True:

                    print("1: Derslerimi görüntüle.\n2: Notlarımı görüntüle.\n3: Ortalama hesapla.")
                    print("4: Çıkış")
                    islem1 = input("Yapmak istediğiniz işlemi seçiniz: ")

                    if islem1 == "1":
                        print(list_of_lessons)

                    elif islem1 == "2":
                        print("Matematik: " + str(kmlNot[0][0]))
                        print("Java: " + str(kmlNot[1][0]))
                        print("Python: " + str(kmlNot[2][0]))
                        print("Mantık Devreleri: " + str(kmlNot[3][0]))
                    elif islem1 == "3":
                        harfNotuHesapla()
                    elif islem1 == "4":
                        print("Hesaptan çıkış yapılıyor...")
                        break

            elif (ysnUserName == "ysn123") & (ysnUserName == ogrncUserName) & (ysnPassword == ogrncPassword):

                print("Giriş Başarılı...\nHoşgeldin " + ysnName + "!")
                while True:

                    print("1: Derslerimi görüntüle.\n2: Notlarımı görüntüle.\n3: Ortalama hesapla.")
                    print("3: Çıkış")
                    islem1 = input("Yapmak istediğiniz işlemi seçiniz: ")

                    if islem1 == "1":
                        print(list_of_lessons)

                    elif islem1 == "2":
                        print("Matematik: " + str(ysnNot[0][0]))
                        print("Java: " + str(ysnNot[1][0]))
                        print("Python: " + str(ysnNot[2][0]))
                        print("Mantık Devreleri: " + str(ysnNot[3][0]))
                    elif islem1 == "3":
                        harfNotuHesapla()
                    elif islem1 == "4":
                        print("Hesaptan çıkış yapılıyor...")
                        break


                print("--------------------------------------------------")


            elif (krstUserName == ogrncUserName) & (krstPassword != ogrncPassword) | \
                    (cnrUserName == ogrncUserName) & (cnrPassword != ogrncPassword) |\
                    (kmlUserName == ogrncUserName) & (kmlPassword != ogrncPassword) |\
                    (ysnUserName == ogrncUserName) & (ysnPassword != ogrncPassword) |\
                    (krstUserName != ogrncUserName) & (krstPassword == ogrncPassword) |\
                    (cnrUserName != ogrncUserName) & (
                    cnrPassword == ogrncPassword) |(ysnUserName != ogrncUserName) & (
                    ysnPassword == ogrncPassword) |(kmlUserName != ogrncUserName) & (
                    kmlPassword == ogrncPassword) | (krstUserName != ogrncUserName) & (krstPassword != ogrncPassword)| \
                    (cnrUserName != ogrncUserName) & (cnrPassword != ogrncPassword)| (ysnUserName != ogrncUserName) & \
                    (ysnPassword != ogrncPassword)| (kmlUserName != ogrncUserName) & (kmlPassword != ogrncPassword):
                print("Kullanıcı adı veya Parola hatalı...\nLütfen Tekrar deneyiniz...")
                girisHakki -= 1
                print("Kalan giriş hakkı: ", girisHakki)


        else:
            print("Geçersiz işlem...")
            break
        break
