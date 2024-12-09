import random

class EntitateEcosistem:
    def __init__(self, nume, energie, x, y, rata_supravietuire):
        self.nume = nume
        self.energie = energie
        self.x = x
        self.y = y
        self.rata_supravietuire = rata_supravietuire

    def actioneaza(self):
        raise NotImplementedError("Trebuie implementat în subclase.")

class Planta(EntitateEcosistem):
    def __init__(self, nume, energie, x, y, rata_crestere, rata_reproducere):
        super().__init__(nume, energie, x, y, rata_supravietuire=1.0)
        self.rata_crestere = rata_crestere
        self.rata_reproducere = rata_reproducere

    def actioneaza(self):
        self.energie += self.rata_crestere
        if random.random() < self.rata_reproducere:
            return Planta("Noua Planta", energie=5, x=self.x + random.randint(-1, 1), y=self.y + random.randint(-1, 1),
                          rata_crestere=self.rata_crestere, rata_reproducere=self.rata_reproducere)

class Animal(EntitateEcosistem):
    def __init__(self, nume, energie, x, y, viteza, tip_hrana):
        super().__init__(nume, energie, x, y, rata_supravietuire=0.8)
        self.viteza = viteza
        self.tip_hrana = tip_hrana

    def deplaseaza(self):
        self.x += random.randint(-self.viteza, self.viteza)
        self.y += random.randint(-self.viteza, self.viteza)

    def mananca(self, tinta):
        if isinstance(tinta, Planta) and self.tip_hrana in ("erbivor", "omnivor"):
            self.energie += tinta.energie
            return True
        elif isinstance(tinta, Animal) and self.tip_hrana in ("carnivor", "omnivor"):
            self.energie += tinta.energie
            return True
        return False

    def actioneaza(self):
        self.deplaseaza()

class Erbivor(Animal):
    def __init__(self, nume, energie, x, y, viteza):
        super().__init__(nume, energie, x, y, viteza, tip_hrana="erbivor")

class Carnivor(Animal):
    def __init__(self, nume, energie, x, y, viteza):
        super().__init__(nume, energie, x, y, viteza, tip_hrana="carnivor")

class Omnivor(Animal):
    def __init__(self, nume, energie, x, y, viteza):
        super().__init__(nume, energie, x, y, viteza, tip_hrana="omnivor")

class Ecosistem:
    def __init__(self, dimensiune_harta):
        self.dimensiune_harta = dimensiune_harta
        self.entitati = []

    def adauga_entitate(self, entitate):
        self.entitati.append(entitate)

    def elimina_entitate(self, entitate):
        self.entitati.remove(entitate)

    def afiseaza_harta(self):
        harta = [["." for _ in range(self.dimensiune_harta)] for _ in range(self.dimensiune_harta)]
        for entitate in self.entitati:
            if 0 <= entitate.x < self.dimensiune_harta and 0 <= entitate.y < self.dimensiune_harta:
                simbol = "P" if isinstance(entitate, Planta) else "A"
                harta[entitate.y][entitate.x] = simbol
        for linie in harta:
            print(" ".join(linie))
        print()

    def simuleaza_pas(self):
        noi_entitati = []
        for entitate in self.entitati[:]:
            rezultat = entitate.actioneaza()
            if isinstance(rezultat, EntitateEcosistem):
                noi_entitati.append(rezultat)
            if entitate.energie <= 0:
                self.elimina_entitate(entitate)
        self.entitati.extend(noi_entitati)

if __name__ == "__main__":
    ecosistem = Ecosistem(dimensiune_harta=10)

    ecosistem.adauga_entitate(Planta("Planta1", energie=10, x=2, y=3, rata_crestere=2, rata_reproducere=0.3))
    ecosistem.adauga_entitate(Erbivor("Iepure", energie=15, x=4, y=5, viteza=2))
    ecosistem.adauga_entitate(Carnivor("Lup", energie=20, x=7, y=8, viteza=3))
    ecosistem.adauga_entitate(Omnivor("Urs", energie=25, x=6, y=6, viteza=1))

    for i in range(10):
        print(f"Pasul {i + 1}:")
        ecosistem.afiseaza_harta()
        ecosistem.simuleaza_pas()
