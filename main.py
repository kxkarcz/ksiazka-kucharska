import io
import json

class Baza_danych:
    def __init__(self,nazwa_pliku):
        self.nazwa_pliku=nazwa_pliku
    def zapis(self):
        pass
    def odczyt(self):
        pass


class Przepis:
    def __init__(self,nazwa,skladnik,opis):
        self.nazwa=nazwa
        self.skladnik=skladnik
        self.opis=opis
    def wypisz(self):
        print(self.nazwa)
        for i in self.skladnik:
            print(i)
        print("")
        for i in self.opis:
            print(i)
        print("")
    def zmien_opis(self,nowy_opis):
        self.opis=nowy_opis


class Ksiazka_kucharska(Baza_danych):
    def __init__(self):
        super(Ksiazka_kucharska, self).__init__("baza.txt")
        self.przepisy=self.odczyt()

    def zapis(self):
        text=""
        d=len(self.przepisy)
        j=0
        for i in self.przepisy:
            tmp={"tytul":i.nazwa,"opis":i.opis,"skladniki":i.skladnik}
            text+=json.dumps(tmp)
            if (j<d-1):
                text+="\n"
            j+=1
        with io.open(self.nazwa_pliku, 'w', encoding='utf8') as f:
            f.write(text)
    def odczyt(self):
        tmp_przepisy=[]
        with io.open(self.nazwa_pliku, 'r', encoding='utf8') as f:
            text = f.read()
            text=text.split("\n")
            for i in text:
                print(i)
                tmp=json.loads(i)
                tmp_przepisy.append(Przepis(tmp["tytul"],tmp["skladniki"],tmp["opis"]))
        return tmp_przepisy
    def wypisz_wszystko(self):
        for i in self.przepisy:
            i.wypisz()
    def wyszukaj(self,nazwa_przepisu):
        with io.open(self.nazwa_pliku, 'r', encoding='utf8') as f:
            text = f.read()
            text = text.split("\n")
            dlugosc=nazwa_przepisu.__len__()
            for i in text:
                dl= len(i)
                if (i[11:(-dl+11+dlugosc)]==nazwa_przepisu):
                    print(i)

    def dodaj_przepis(self):
        with io.open(self.nazwa_pliku, 'r', encoding='utf8') as f:
            text = f.read()
            tytul=input("Podaj tytuł: ")
            print("Podaj skladniki, jeśli to wszystkie napisz koniec: ")
            skladniki=[]
            while(True):
                a=input()
                if (a=="koniec" or a=="Koniec"):
                    break
                else:
                    skladniki.append(a)
            print("Podaj kroki, jeśli to wszystkie napisz koniec: ")
            kroki=[]
            while(True):
                a=input()
                if (a=="koniec" or a=="Koniec"):
                    break
                else:
                    kroki.append(a)
            przepis={"tytul":tytul,"opis":kroki,"skladniki":skladniki}
            napis=""
            napis+=str(text)
            napis+="\n"+str(przepis)
            with io.open(self.nazwa_pliku, 'w', encoding='utf8') as f:
                f.write(str(napis))

    def usun_przepis(self,nazwa_przepisu):
        with io.open(self.nazwa_pliku, 'r', encoding='utf8') as f:
            text = f.read()
            text = text.split("\n")
            dlugosc=nazwa_przepisu.__len__()
            napis=""
            for i in text:
                dl= len(i)
                a=i.split("\n")
                for k in a:
                    if (k[11:(-dl + 11 + dlugosc)] == nazwa_przepisu):
                        continue
                    else:
                        napis+=k
            with io.open(self.nazwa_pliku, 'w', encoding='utf8') as f:
                f.write(napis)




ksiaz_kucharska=Ksiazka_kucharska()
ksiaz_kucharska.zapis()
ksiaz_kucharska.wyszukaj("jajecznica")
ksiaz_kucharska.dodaj_przepis()
ksiaz_kucharska.usun_przepis("platki")