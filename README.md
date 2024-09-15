# Labs_OOP

class Telefon:
    def __init__(self, marca, model, culoarea):
        self.marca = marca
        self.model = model
        self.culoarea = culoarea

    def afiseaza_detalii(self):
        print(f" Telefon: {self.marca} {self.model} \n Culoarea: {self.culoarea}")
    
    @classmethod
    def creeaza_telefon(cls):
        marca = input("Introduceți marca telefonului: ")
        model = input("Introduceți modelul telefonului: ")
        culoarea = input("Introduceți culoarea telefonului: ")
        return cls(marca, model, culoarea)

class Magazin:
    def __init__(self):
        self.telefoane = []  

    def adauga_telefon(self, telefon):
        self.telefoane.append(telefon)
        print(f"Telefonul {telefon.marca} {telefon.model} a fost adăugat în magazin.")

    def sterge_telefon(self, model):
        for telefon in self.telefoane:
            if telefon.model == model:
                self.telefoane.remove(telefon)
                print(f"Telefonul {telefon.marca} {telefon.model} a fost șters din magazin.")
                return
        print(f"Telefonul cu modelul {model} nu a fost găsit.")

    def afiseaza_telefoane(self):
        if len(self.telefoane) == 0:
            print("Nu există telefoane disponibile în magazin.")
        else:
            print("Telefoanele disponibile în magazin:")
            for telefon in self.telefoane:
                telefon.afiseaza_detalii()
                print("---")

def adauga_telefon_magazin(magazin):
    telefon = Telefon.creeaza_telefon()
    magazin.adauga_telefon(telefon)

def sterge_telefon_magazin(magazin):
    model = input("Introduceți modelul telefonului pe care doriți să-l ștergeți: ")
    magazin.sterge_telefon(model)

def afiseaza_telefoanele_din_magazin(magazin):
    magazin.afiseaza_telefoane()

def meniu():
    magazin = Magazin() 
    
    while True:
        print("\n--- Meniu ---")
        print("1. Adaugă telefon")
        print("2. Șterge telefon")
        print("3. Afișează telefoanele din magazin")
        print("4. Ieșire")
        
        optiune = input("Alegeți o opțiune: ")

        if optiune == "1\n":
            adauga_telefon_magazin(magazin)
        elif optiune == "2\n":
            sterge_telefon_magazin(magazin)
        elif optiune == "3\n":
            afiseaza_telefoanele_din_magazin(magazin)
        elif optiune == "4\n":
            print("Ieșire din program.")
            break
        else:
            print("Opțiune invalidă. Vă rugăm să alegeți din nou.")

meniu()
