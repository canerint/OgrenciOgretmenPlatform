import tkinter
from tkinter import *
import time


bilgiler = ("admin", "123456")
denemeHakki = 3
zaman = 0

def girisYap():
    global denemeHakki, zaman

    if denemeHakki <= 0:
        if time.time() - zaman >= 5:
            denemeHakki = 3
        else:
            sonuc.config(text=u"Lutfen 5 saniye bekleyiniz.")
            return False

    kAdi = isim.get()
    parola = sifre.get()

    print(kAdi+" - "+parola)
    print("Kontrol ediliyor ...")

    if kAdi == bilgiler[0] and parola == bilgiler[1]:
        print("Bilgiler dogru!")
        sonuc.config(text=u"Oturum acma islemi basarili.")
        ekraniTemizle()
    else:
        print("Bilgiler yanlis!")

        denemeHakki -= 1
        if denemeHakki == 0:
            zaman = time.time()
        sonuc.config(text=u"Bilgiler yanlis. Kalan deneme hakki: %d" % denemeHakki)


def ekraniTemizle():
    karsilama.config(text=u"Hosgeldiniz...")
    isimSor.destroy()
    isim.destroy()
    sifreSor.destroy()
    sifre.destroy()
    buton.destroy()

    def show_marks():
        mark_window = Toplevel(pencere)
        mark_window.geometry("500x500")
        mark_window.title("Not Görünteleme")

        f=open("notlar.txt","r")
        f2=open("ogrenciler.txt","r")
        f3=open("finaller.txt","r")

        marks = f.read().replace("\n","-").split("-")
        students = f2.read().replace("\n","-").split("-")
        marks2 = f3.read().replace("\n","-").split("-")
        std=""
        mrk=""
        mrk2=""

        f.close()
        f2.close()
        f3.close()

        for i in range(len(students)):
            std+= students[i]+"\n"
            mrk+= marks[i]+"\n"
            mrk2+= marks2[i]+"\n"

        #print(std_marks)
        std_label = Label(mark_window,text="Öğrenciler",font=20).place(x=62,y=20)
        midterm_exam = Label(mark_window,text="Vize",font=20).place(x=190,y=20)
        final_exam = Label(mark_window,text="Final",font=20).place(x=320,y=20)
        student = Label(mark_window,text=std).place(x=20,y=50)
        mark = Label(mark_window, text=mrk).place(x=195,y=50)
        mark2 = Label(mark_window, text=mrk2).place(x=325,y=50)

    def std_list():
        std_window = Toplevel(pencere)
        std_window.geometry("400x400")
        std_window.title("Öğrenci Listeleme")

        f=open("ogrenciler.txt","r")
        students=f.read()
        f.close()

        #Yazı stilini kalın yapıyoruz font içindeki argumanlarla.
        std_label = Label(std_window, text="Öğrenciler",font=('Times',20,'bold')).place(x=45,y=20)
        student = Label(std_window,text=students).place(x=40,y=70)

    def go_mark():
        entry_window = Toplevel(pencere)
        entry_window.geometry("400x400")
        entry_window.title("Not Girme")

        nameText = tkinter.StringVar()
        surnameText = tkinter.StringVar()
        midtermText = tkinter.StringVar()
        finalText = tkinter.StringVar()

        def enter_mark():
            nameString = nameText.get()
            surnameString = surnameText.get()
            full_name = "\n"+nameString + " " + surnameString
            midtermString = midtermText.get()
            midtermString2 = "\n"+midtermString
            finalString = finalText.get()
            finalString2 = "\n"+finalString

            f = open("ogrenciler.txt","a")
            f1 = open("notlar.txt","a")
            f2 = open("finaller.txt","a")

            f.write(full_name)
            f1.write(midtermString2)
            f2.write(finalString2)

            f.close()
            f1.close()
            f2.close()

            mark_label.destroy()
            name_entry.destroy()
            mark2_label.destroy()
            surname_entry.destroy()
            mark3_label.destroy()
            midterm_exam.destroy()
            mark4_label.destroy()
            final_exam.destroy()
            confirm_button.destroy()

            new_label = Label(entry_window, text="Öğrenci notu başarıyla eklendi !", font=('Times', 15, 'bold')).place(x=50, y=50)

        mark_label = Label(entry_window, text="İsim", font=15)
        mark_label.place(x=40, y=37)
        name_entry = Entry(entry_window, width=25, textvariable=nameText)
        name_entry.place(x=40, y=60)
        mark2_label = Label(entry_window, text="Soyisim", font=15)
        mark2_label.place(x=40, y=85)
        surname_entry = Entry(entry_window, width=25, textvariable=surnameText)
        surname_entry.place(x=40, y=108)
        mark3_label = Label(entry_window, text="Vize", font=15)
        mark3_label.place(x=40, y=133)
        midterm_exam = Entry(entry_window, width=25, textvariable=midtermText)
        midterm_exam.place(x=40, y=156)
        mark4_label = Label(entry_window, text="Final", font=15)
        mark4_label.place(x=40, y=181)
        final_exam = Entry(entry_window, width=25, textvariable=finalText)
        final_exam.place(x=40, y=204)
        confirm_button = Button(entry_window, width=20, text="Onayla", command=enter_mark)
        confirm_button.place(x=40, y=259)

    def list_less():
        lesson_window = Toplevel(pencere)
        lesson_window.geometry("400x400")
        lesson_window.title("Ders Listeleme")

        f=open("dersler.txt","r")
        lessons=f.read().replace("\n","-").split("-")
        ls=""
        f.close()

        for i in range(len(lessons)):
            ls+=lessons[i]+"\n"

        mark_label = Label(lesson_window, text="Dersler",font=('Times',20,'bold')).place(x=60,y=20)
        lesson = Label(lesson_window,text=ls).place(x=20,y=55)

    def logout():
        not_gor.destroy()
        ogr_list.destroy()
        not_gir.destroy()
        ders_list.destroy()
        log_out.destroy()
        karsilama.destroy()

        mark_label = Label(pencere, text="Çıkış yapılıyor...").place(x=100, y=100)
        time.sleep(1)
        exit(0)

    not_gor = Button(pencere,width=15,text="Not Görüntüleme",command=show_marks)
    not_gor.place(x=40,y=100)
    ogr_list = Button(pencere,width=15,text="Öğrenci Listeleme",command=std_list)
    ogr_list.place(x=40, y=130)
    not_gir = Button(pencere,width=15,text="Not Gir",command=go_mark)
    not_gir.place(x=40,y=160)
    ders_list = Button(pencere,width=15,text="Ders Listele",command=list_less)
    ders_list.place(x=40,y=190)
    log_out = Button(pencere,width=15,text="Çıkış Yap",command=logout)
    log_out.place(x=40,y=220)


pencere = Tk()

pencere.title(u"ÖĞRENCİ ÖĞRETMEN PLATFORMU")
pencere.geometry("500x500")

karsilama = Label(pencere)
karsilama.config(text=u"Hoşgeldiniz, lütfen giriş yapınız.")
karsilama.pack()

isimSor = Label(pencere)
isimSor.config(text=u"Kullanici Adi:")
isimSor.pack()

isim = Entry(pencere)
isim.pack()

sifreSor = Label(pencere)
sifreSor.config(text=u"Sifreniz:")
sifreSor.pack()


sifre = Entry(pencere,show='*')
sifre.pack()



buton = Button(pencere)
buton.config(text=u"Giris yap!", command=girisYap)
buton.pack()

sonuc = Label(pencere)
sonuc.config(text=u"Giris yapilmadi.")
sonuc.pack()

mainloop()