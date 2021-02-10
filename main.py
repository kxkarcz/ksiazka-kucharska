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
        pass
    def dodaj_przepis(self):
        pass
    def usun_przepis(self,nazwa_przepisu):
        pass
ksiaz_kucharska=Ksiazka_kucharska()
ksiaz_kucharska.zapis()